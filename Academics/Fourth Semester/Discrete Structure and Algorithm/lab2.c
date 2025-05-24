//PRORAM TO CONVERT INFIX OPERATION TO POSTFIX OPERATION 

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
            return 1;
        case '*':
            return 2;
        case '/':
            return 3;
        case '^':
            return 4;
        case '-':
            return 0;
    }
}
void reverse(char *str) {
    int n = strlen(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - i - 1];
        str[n - i - 1] = temp;
    }
}
void main(){
    char expression[50];
    printf("enter the operation you want to perform\n");
    scanf("%s", expression);
    reverse(expression);
    for (int i = 0; i < strlen(expression); i++) {
            if (isOperator(expression[i])){
                switch (precedence(expression[i])){
                    case 1:
                        int a = pop();
                        int b = pop();
                        int result = a + b;
                        push(result);
                        break;
                    case 2:
                        int c = pop();
                        int d = pop();
                        int result2 = c * d;
                        push(result2);
                        break;
                    case 3:
                        int e = pop();
                        int f = pop(); 
                        int result3 = e / f;
                        push(result3);
                        break;
                    case 4:
                        int g = pop();
                        int h = pop(); 
                        int result4 = g ^ h;
                        push(result4);
                        break;
                    case 0:
                        int i = pop();
                        int j = pop(); 
                        int result5 = i - j;
                        push(result5);
                        break;
                    default:
                        printf("Invalid operator\n");
                        break;
                        
                }
                }else {
                    push(expression[i] - '0');

            }
    }
    printf("Result: %d\n", pop());
    printf("\n");
}
