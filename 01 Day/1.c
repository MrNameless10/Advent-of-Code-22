#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fp;
    char line[100];
    int sum = 0;
    int num = 0;
    int max = 0;
    fp = fopen("input1.txt", "r");
    while(fgets(line, 100, fp) != NULL){
        if(line[0] == '\n'){
            if (sum > max){
                max = sum;
            }
            sum = 0;
        }
        else{
            num = atoi(line);
            sum += num;
        }
    }
    printf("%d", max);
    fclose(fp);
    return 0;
}
