#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<signal.h>

void f(int sig){
    printf("%d signal received\n",sig);
}

int main(){
    signal(30,f);
    signal(31,f);

    for(;;)
        pause();
}
