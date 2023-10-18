#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>

int main()
{
    int pid,status;
    if((pid=fork())==0){
        execl("./child","abc","def", "efg","123","456",NULL);
        return 123;
    }else{
        wait(&status);
        printf("main return %d\n",WEXITSTATUS(status));
    }
    return 0;
}
