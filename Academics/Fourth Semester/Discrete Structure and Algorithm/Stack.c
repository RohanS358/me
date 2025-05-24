#include <stdio.h>

void main (){
    int arr[5]={1,2,3,4,5};
    printf("array %")
}


#include <stdio.h>
#include <string.h>

char stack[50];
int top = -1;
void push(char c) {
    if (top < 49) {
        stack[++top] = c;
    } else {
        printf("Stack overflow\n");
    }
}
char pop() {
    if (top != -1) {
        return stack[top--];
    } else {
        printf("Stack underflow\n");
        return '\0';
    }
}
bool isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}
int precedence(char c) {
    switch (c) {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
        case '^':
            return 3;
        default:
            return 0;
    }
}


void main (){
    char expression[50];

    printf("enter the operation you want to perform\n");
    scanf("%s", expression);
    for (int i = 0; i < strlen(expression); i++) {
        if (expression[i] == '(') {
            push(expression[i]);
        } else if (expression[i] == ')') {
            while (stack[top] != '(') {
                printf("%c", pop());
            }
            pop(); // Pop the '('
        } else if (isOperator(expression[i])) {
            while (top != -1 && precedence(stack[top]) >= precedence(expression[i])) {
                printf("%c", pop());
            }
            push(expression[i]);
        } else {
            printf("%c", expression[i]);
        }
    }
    while (top != -1) {
        printf("%c", pop());
    }
    printf("\n");
    
}