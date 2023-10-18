#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main(int argc,char *argv[],char **envp){
    int p[2];
    pipe(p);            //create pipe

    if(fork()==0){      //child process
        close(0);       //
        dup(p[0]);      //connect standard input to pipe input port
        close(p[0]);    //close pipe input port
        close(p[1]);    //close pipe output port
        execlp("sort","sort",NULL);
    }
    else{               //parent process
        close(1);       //
        dup(p[1]);      //connect standard input to pipe input port
        close(p[0]);    //close pipe input port
        close(p[1]);    //close pipe output port
        execlp("ls","ls",NULL);
    }
}