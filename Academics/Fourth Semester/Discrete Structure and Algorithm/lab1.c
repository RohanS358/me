

#include <stdio.h>
#include <string.h>


struct date {
    int day;
    int month;
    int year;
};

struct student {
    char name[20];
    struct date DOB;
    int roll_no;
    int marks[5];
    float Average;
    float Percentage;
};

void greet ()  {
    printf("Hello, welcome to the student management system!\n");
}
struct student getInfo(struct student s1){
    printf("Enter name: ");
    scanf("%s", s1.name);
    printf("Enter date of birth (dd mm yyyy): ");
    scanf("%d %d %d", &s1.DOB.day, &s1.DOB.mont
        h, &s1.DOB.year);
    printf("Enter roll number: ");
    scanf("%d", &s1.roll_no);
    printf("Enter marks for 5 subjects: ");
    for(int i = 0; i < 5; i++){
        scanf("%d", &s1.marks[i]);
    }
    return s1;
}
struct date calculateAge(struct date current_date, struct student s1){
    int age_years = current_date.year - s1.DOB.year;
    int age_months = current_date.month - s1.DOB.month;
    int age_days = current_date.day - s1.DOB.day;

    if (age_days < 0) {
        age_months--;
        age_days += 30; 
    }
    if (age_months < 0) {
        age_years--;
        age_months += 12;
    }
    return (struct date){age_days, age_months, age_years};
    
}
float calculateAverage(struct student s1){
    float average = 0;
    for(int i = 0; i < 5; i++){
        average += s1.marks[i];
    }
    average /= 5;
   return average;
}
float calculatePercentage(struct student s1){
    float percentage = 0;
    for(int i = 0; i < 5; i++){
        percentage += s1.marks[i];
    }
    percentage = (percentage / 500) * 100;
    return percentage;
}
void displayResult(struct student s1,struct date current_date){
    printf("Name: %s\n", s1.name);
    struct date age = calculateAge(current_date, s1);
    printf("Age: %d years, %d months, %d days\n", age.year, age.month, age.day);
    printf("Date of Birth: %02d/%02d/%04d\n", age.day, age.month, age.year);
    printf("Roll Number: %d\n", s1.roll_no);
    printf("Marks: ");
    for(int i = 0; i < 5; i++){
        printf("%d ", s1.marks[i]);
    }
    printf("\n");
    printf("Average: %.2f\n", calculateAverage(s1));
    printf("Percentage: %.2f%%\n", calculatePercentage(s1));
    printf("\n");
}
void studentManagementSystem(){
    struct date current_date ={14,5,2025};
    struct student s1;
    greet();
    s1 = getInfo(s1);
    displayResult(s1,current_date);
}


void reverse(int arr[]){
    int i, j, temp;
    for (i = 0, j = 4; i < j; i++, j--) {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

void reverseArray (){
    int arr[5];
    printf("Enter 5 integers: ");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }
    reverse(arr);
    printf("Reversed array: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
}

void findMaxMin(int *arr,int size , int *max, int *min){
    *max = arr[0];
    *min = arr[0];
    for (int i = 1; i <size; i++) {
        if (arr[i] > *max) {
            *max = arr[i];
        }
        if (arr[i] < *min) {
            *min = arr[i];
        }
    }
}

void minmax (){
    int size = 5;
    int arr[size];
    int max,min;
    printf("Enter 5 integers: ");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }
    findMaxMin(arr,size,&max,&min);
    printf("Maximum: %d\n", max);
    printf("Minimum: %d\n", min);
}


void swapByReference(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
void swapByValue(int a, int b){
    int temp = a;
    a = b;
    b = temp;
}
void functionin (){
    printf("Choose an option:\n");
    printf("1. Swap by reference\n");
    printf("2. Swap by value\n");
    int option;
    scanf("%d", &option);
    switch (option)
    {
    case 1:
        int a,b;
        printf("Enter two integers: ");
        scanf("%d %d", &a, &b);
        printf("Before swap: a = %d, b = %d\n", a, b);
        swapByReference(&a, &b);
        printf("After swap by reference: a = %d, b = %d\n", a, b);
        break;
    case 2:
        int x, y;
        printf("Enter two integers: ");
        scanf("%d %d", &x, &y);
        printf("Before swap: x = %d, y = %d\n", x, y);
        swapByValue(x, y);
        printf("After swap by value: x = %d, y = %d\n", x, y);
        break;
    default:
        printf("Invalid option\n");
        break;
    }
    
    
}

void factIterative(int n){
    int fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    printf("Factorial of %d is %d\n", n, fact);
}
int factRecursive(int n){
    if (n == 0 || n == 1) {
        return 1;
    }
    return n * factRecursive(n - 1);
}
void factorial(){
    printf("Choose an option:\n");
    printf("1. Factorial Iterative\n");
    printf("2. Factorial Recursive\n");
    int option;
    scanf("%d", &option);
    switch (option)
    {
    case 1:
        int n;
        printf("Enter a number: ");
        scanf("%d", &n);
        factIterative(n);
        break;
    case 2:
        int m;
        printf("Enter a number: ");
        scanf("%d", &m);
        factRecursive(m);
        break;
        printf("Factorial of %d is %d\n", m, factRecursive(m));
        printf("Invalid option\n");
        break;
    }
}


void main (){
    printf("Hello fellas.....To Rohan's lab practicals\n");
    printf("----------------------------------------\n");
    printf("1. Student Management System\n");
    printf("2. Reverse an array\n");
    printf("3. Find max and min in an array\n");
    printf("4. Swap two numbers\n");
    printf("5. Factorial of a number\n");
    printf("6. Exit\n");
    printf("Enter your choice: ");
    int choice;
    scanf("%d", &choice);
    switch (choice) {
        case 1:
            printf("\033[2J\033[H");
            printf("You chose Student Management System\n");

            studentManagementSystem();
            break;
        case 2:
            printf("\033[2J\033[H");
            printf("You chose Reverse an array\n");

            reverseArray();
            break;
        case 3:
            printf("\033[2J\033[H");
            printf("You chose Find max and min in an array\n");
            
            minmax();
            break;
        case 4:
            printf("\033[2J\033[H");
            printf("You chose Swap two numbers\n");
            
            functionin();
            break;
        case 5:
            printf("\033[2J\033[H");
            printf("You chose Factorial of a number\n");
            
            factorial();
            break;
        case 6:
            printf("\033[2J\033[H");
            printf("Exiting...\n");

            break;
        default:
            printf("updating you system lol\n");
            
    }
    printf("/n");
    printf("Thank you for using the program!\n");
    printf("Goodbye!\n");
}