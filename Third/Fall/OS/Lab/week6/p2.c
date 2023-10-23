#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main(int argc,char *argv[],char **envp){
    int status;
    if (fork()==0){
        execl("/bin/bash","bash","my_shell",
        "abc","def","ghi","123","456",NULL);
    }
    else{
        wait(&status);
        printf("Program terminated %d\n",WEXITSTATUS(status));
    }
    return 0;
}
