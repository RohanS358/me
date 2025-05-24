import cv2
import time
import numpy as np
import pyautogui
import math
from scipy.interpolate import CubicSpline
from collections import deque
import threading

# Initialize video capture and set resolution
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Increased resolution for better face details
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
vid.set(cv2.CAP_PROP_FPS, 30)

# Load Haar Cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Screen dimensions
screen_width, screen_height = pyautogui.size()

# Variables for smoothing detection results
looking_at_screen = False
confidence_score = 0.5  # Range: 0-10
last_detection_time = time.time()
detection_cooldown = 0.1  # Seconds

# Function to determine if eyes are facing forward
def is_looking_at_screen(eyes, face_width):
    if len(eyes) < 2:
        return False, 0  # Not enough eyes detected
    
    # Sort eyes by x-position
    eyes = sorted(eyes, key=lambda e: e[0])
    
    # Calculate eye width ratio (should be similar for both eyes when facing forward)
    left_eye_width = eyes[0][2]
    right_eye_width = eyes[1][2]
    width_ratio = min(left_eye_width, right_eye_width) / max(left_eye_width, right_eye_width)
    
    # Calculate distance between eye centers
    left_eye_center_x = eyes[0][0] + eyes[0][2] // 2
    right_eye_center_x = eyes[1][0] + eyes[1][2] // 2
    eye_distance = right_eye_center_x - left_eye_center_x
    
    # Calculate eye distance ratio (should be ~0.4-0.5 of face width when facing forward)
    eye_distance_ratio = eye_distance / face_width
    
    # Calculate confidence score (0-10)
    width_confidence = min(10, width_ratio * 10)  # Eyes should be similar size
    distance_confidence = 10 - abs(eye_distance_ratio - 0.45) * 20  # Ideal eye distance ~45% of face
    distance_confidence = max(0, min(10, distance_confidence))
    
    confidence = (width_confidence + distance_confidence) / 2
    
    return confidence > 6, confidence  # Looking at screen if confidence > 6

while True:
    success, frame = vid.read()
    if not success:
        print("Failed to capture video frame")
        break

    # Flip and preprocess frame
    frame = cv2.flip(frame, 1)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Face detection
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    current_time = time.time()
    looking_status = "Not detected"
    status_color = (0, 0, 255)  # Red
    
    # Process the largest face (closest to camera)
    if len(faces) > 0:
        # Get the largest face by area
        largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
        x, y, w, h = largest_face
        
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Region of interest for the face
        roi_gray = gray_frame[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Eye detection within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangles around the eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        
        # Check if looking at screen (only if we detect at least 2 eyes)
        if len(eyes) >= 2 and current_time - last_detection_time > detection_cooldown:
            is_looking, new_confidence = is_looking_at_screen(eyes, w)
            
            # Smooth the confidence score
            confidence_score = 0.7 * confidence_score + 0.3 * new_confidence
            looking_at_screen = confidence_score > 6
            last_detection_time = current_time
            
        # Update status message
        if looking_at_screen:
            looking_status = f"Looking at screen ({confidence_score:.1f})"
            status_color = (0, 255, 0)  # Green
        else:
            if len(eyes) >= 2:
                looking_status = f"Not looking at screen ({confidence_score:.1f})"
                status_color = (0, 165, 255)  # Orange
            else:
                looking_status = f"Eyes not detected ({len(eyes)})"
                status_color = (0, 0, 255)  # Red
    
    # Display status
    cv2.putText(frame, looking_status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
    
    # Display number of faces detected
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    # Display the frame
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
vid.release()
cv2.destroyAllWindows()
