// t
// to
// tom
// toma
// tomat
// tomato 
#include <stdio.h>
void main(){
    char str[20];
    printf("Enter a string: ");
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        for(int j = 0; j <= i; j++){
            printf("%c", str[j]);
        }
        printf("\n");
    }
}