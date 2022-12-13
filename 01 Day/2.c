#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *fp;
    char line[100];
    int sum = 0;
    int num = 0;
    int arr[1000];
    int i = 0;
    fp = fopen("input1.txt", "r");
    while(fgets(line, 100, fp) != NULL){
        if(line[0] == '\n'){
            arr[i] = sum;
            i++;
            sum = 0;
        }
        else{
            num = atoi(line);
            sum += num;
        }
    }
    arr[i] = sum;
    i++;
    int temp = 0;
    for(int j = 0; j < i; j++){
        for(int k = j + 1; k < i; k++){
            if(arr[j] < arr[k]){
                temp = arr[j];
                arr[j] = arr[k];
                arr[k] = temp;
            }
        }
    }
    int sum_3 = 0;
    for(int j = 0; j < 3; j++){
        sum_3 += arr[j];
    }
    printf("%d", sum_3);
    fclose(fp);
    return 0;
}


    








