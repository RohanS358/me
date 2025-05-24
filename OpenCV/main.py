import cv2
import mediapipe as mp
import os
import math
import pyautogui
import time

# Initialize video capture
vid = cv2.VideoCapture(0)
vid.set(4, 760)  # Set height

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils
mp_draw_styles = mp.solutions.drawing_styles

# Track previous positions for gesture detection
prev_positions = {}
last_action_time = 0
action_cooldown = 0.5  # Cooldown in seconds to prevent repeated actions
speed= 0
# Track pinch and swipe state
left_pinch_start_time = 0
pinch_swipe_threshold = 0.3  # Time threshold for pinch+swipe detection (seconds)

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    success, frame = vid.read()
    if not success:
        print("Failed to capture video frame")
        break

    frame = cv2.flip(frame, 1)  # Flip frame horizontally
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Status text positions
    status_height = 30
    status_x = 10
    
    # Gesture states
    left_hand_middle_pinch = False  # Middle finger pinch
    right_hand_middle_pinch = False  # Middle finger pinch
    left_hand_index_pinch = False   # Index finger pinch
    left_hand_swipe = None
    right_hand_swipe = None
    left_pinch_and_swipe_direction = None  # New: Tracks swipe direction during pinch
    
    

    # Draw landmarks and detect gestures
    if results.multi_hand_landmarks and results.multi_handedness:
        current_time = time.time()
        h, w, c = frame.shape
        
        for hand_idx, (hand_landmarks, hand_info) in enumerate(zip(results.multi_hand_landmarks, results.multi_handedness)):
            # Get hand label (Left/Right)
            hand_label = hand_info.classification[0].label
            
            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_draw_styles.get_default_hand_landmarks_style(),
                mp_draw_styles.get_default_hand_connections_style()
            )
            
            # Extract important landmarks
            landmarks = {}
            
            # Get landmarks
            for landmark_id, landmark in enumerate(hand_landmarks.landmark):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                landmarks[landmark_id] = (cx, cy)
                
                # Mark important landmarks - thumb tip, index tip, middle tip
                if landmark_id == 4:  # thumb tip - red
                    cv2.circle(frame, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
                elif landmark_id == 8:  # index tip - blue (for swiping)
                    cv2.circle(frame, (cx, cy), 10, (255, 0, 0), cv2.FILLED)
                elif landmark_id == 12:  # middle tip - green (for pinching)
                    cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
            
            # Calculate hand size for adaptive threshold
            if 0 in landmarks and 5 in landmarks:
                # Distance between wrist and index finger MCP joint as hand size reference
                hand_size = calculate_distance(
                    landmarks[0][0], landmarks[0][1],
                    landmarks[5][0], landmarks[5][1]
                )
                
                # Adaptive pinch threshold based on hand size
                pinch_threshold = int(20 * (hand_size * 0.6 / 100)+6)
                
                # Ensure reasonable threshold bounds
                pinch_threshold = max(10, min(pinch_threshold, 40))
                
                # Display adaptive threshold
                cv2.putText(frame, f"Threshold: {pinch_threshold}", (landmarks[0][0]-50, landmarks[0][1]-60), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            else:
                # Default if landmarks not available
                pinch_threshold = 25
            
            # Track hand position
            hand_key = f"{hand_label}_{hand_idx}"
            if hand_key not in prev_positions:
                prev_positions[hand_key] = {}
            
            # Detect middle finger pinch gesture (thumb to MIDDLE finger)
            if 4 in landmarks and 12 in landmarks:
                thumb_tip = landmarks[4]
                middle_tip = landmarks[12]
                
                # Calculate distance between thumb and middle
                pinch_distance = calculate_distance(
                    thumb_tip[0], thumb_tip[1], 
                    middle_tip[0], middle_tip[1]
                )
                
                # Draw pinch line
                cv2.line(frame, thumb_tip, middle_tip, (255, 255, 0), 2)
                
                # Check for pinch
                if pinch_distance < pinch_threshold:
                    if hand_label == "Left":
                        left_hand_middle_pinch = True
                        
                        # Start tracking pinch time for swipe detection
                        if left_pinch_start_time == 0:
                            left_pinch_start_time = current_time
                        
                        # Track middle finger movement during pinch
                        if 12 in prev_positions[hand_key] and (current_time - left_pinch_start_time) > pinch_swipe_threshold:
                            prev_middle = prev_positions[hand_key][12]
                            dx = middle_tip[0] - prev_middle[0]
                            
                            # Detect swipe with minimum threshold
                            if abs(dx) > 10:
                                left_pinch_and_swipe_direction = "right" if dx > 0 else "left"
                                
                                # Draw swipe line during pinch
                                cv2.arrowedLine(
                                    frame, prev_middle, middle_tip, 
                                    (0, 255, 255), 3, tipLength=0.3
                                )
                        
                        cv2.putText(frame, "Middle Pinch!", (landmarks[0][0]-50, landmarks[0][1]-20), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                    elif hand_label == "Right":
                        right_hand_middle_pinch = True
                        cv2.putText(frame, "Middle Pinch!", (landmarks[0][0]-50, landmarks[0][1]-20), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                else:
                    # Reset pinch tracking when not pinching
                    if hand_label == "Left":
                        left_pinch_start_time = 0
            
            # Save middle finger position for next frame
            if 12 in landmarks:
                prev_positions[hand_key][12] = landmarks[12]
            
            # NEW: Detect index finger pinch gesture (thumb to INDEX finger)
            if 4 in landmarks and 8 in landmarks:
                thumb_tip = landmarks[4]
                index_tip = landmarks[8]
                
                # Calculate distance between thumb and index
                index_pinch_distance = calculate_distance(
                    thumb_tip[0], thumb_tip[1], 
                    index_tip[0], index_tip[1]
                )
                
                # Check for index finger pinch
                if index_pinch_distance < pinch_threshold:
                    if hand_label == "Left":
                        left_hand_index_pinch = True
                        cv2.putText(frame, "Index Pinch!", (landmarks[0][0]-50, landmarks[0][1]-40), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
                        # Draw index pinch line
                        cv2.line(frame, thumb_tip, index_tip, (255, 0, 255), 2)
            
            # Track INDEX finger for swipe detection (both hands)
            if 8 in landmarks:
                index_finger = landmarks[8]
                
                # Get previous position
                if 8 in prev_positions[hand_key]:
                    prev_index = prev_positions[hand_key][8]

                    # Calculate horizontal movement
                    dx = index_finger[0] - prev_index[0]
                    dy = index_finger[1] - prev_index[1]
                    # Detect swipe with minimum threshold
                    if abs(dx) > 20 and  abs(dx-dy) > 20: # Minimum swipe distance
                        
                        swipe_direction = "right" if dx > 0 else "left"
                        
                        # Draw swipe line
                        cv2.arrowedLine(
                            frame, prev_index, index_finger, 
                            (255, 0, 0), 2, tipLength=0.3
                        )
                        
                        if hand_label == "Left":
                            left_hand_swipe = swipe_direction
                        elif hand_label == "Right":
                            right_hand_swipe = swipe_direction
                    if abs(dy) > 60 and abs(dy-dx) > 20:
                        swipe_direction = "down" if dy > 0 else "up"
                        speed = int(dy/30)
                        cv2.arrowedLine( frame, prev_index, index_finger,(255,0,255),2,tipLength=0.3)
                        
                        left_hand_swipe = right_hand_swipe = swipe_direction
                # Save current position for next frame
                prev_positions[hand_key][8] = index_finger
                
                    
    # Perform actions with cooldown
    current_time = time.time()
    
    # Display status info
    info_y = 30
    cv2.putText(frame, f"Left middle pinch: {left_hand_middle_pinch}", (10, info_y), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    info_y += 30
    
    cv2.putText(frame, f"Pinch+Swipe: {left_pinch_and_swipe_direction}", (10, info_y), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    info_y += 30
    
    cv2.putText(frame, f"Left index pinch: {left_hand_index_pinch}", (10, info_y), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    info_y += 30
    
    cv2.putText(frame, f"Right swipe: {right_hand_swipe}", (10, info_y), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Execute actions with cooldown
    if current_time - last_action_time > action_cooldown:
        # Arrow keys based on left hand middle finger pinch + swipe direction
        if left_hand_middle_pinch :
                pyautogui.press("left")
                cv2.putText(frame, "LEFT ARROW", (w-200, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                last_action_time = current_time
        elif right_hand_middle_pinch :
                pyautogui.press("right")
                cv2.putText(frame, "RIGHT ARROW", (w-200, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                last_action_time = current_time
        
        # Desktop switching ONLY when left index finger is pinched AND right hand swipe detected
        if left_hand_index_pinch and right_hand_swipe:
            if right_hand_swipe == "right":
                os.system("wmctrl -s 0")
                cv2.putText(frame, "DESKTOP 1", (w//2-100, h//2), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                last_action_time = current_time
            elif right_hand_swipe == "left":
                os.system("wmctrl -s 1") 
                cv2.putText(frame, "DESKTOP 2", (w//2-100, h//2), 
                           cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
                last_action_time = current_time
            elif right_hand_swipe == "up":
                for i in range (0,int(dy/30)):
                    pyautogui.press("pgdn")
            elif right_hand_swipe == "down":
                for i in range (0,int(dy/30)):
                    pyautogui.press("pgup") 
        

    # Display the frame
    cv2.imshow("Hand Gesture Control", frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Properly release resources and exit
vid.release()
cv2.destroyAllWindows()
