#include<stdio.h>
#include<time.h>

void linear(int size){

    for (int i=0;i<size;i++){}
}

void loga(int size){

    for (int i=size;i>0;i=i/2){}
}

void quadratic(int size){

    for(int i=0;i<size;i++){
        for (int j=0;j<size;j++) {}
    }
}

int main (){
    
    int n=100000;
    clock_t lin_start=clock();
    linear(n);
    clock_t lin_end=clock();
    printf("the linear time complexity is %f\n",(double)( lin_end-lin_start )/CLOCKS_PER_SEC);
    
    clock_t log_start=clock();
    loga(n);
    clock_t log_end=clock();
    printf("the logarithmic time complexity is %f\n",(double)( log_end-log_start)/CLOCKS_PER_SEC);
    
    clock_t quad_start=clock();
    quadratic(n);
    clock_t quad_end=clock();
    printf("the quadratic time complexity is %f\n",(double)( quad_end-quad_start )/CLOCKS_PER_SEC);
    
    return 0;
}