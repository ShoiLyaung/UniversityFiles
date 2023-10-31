- 虚地址空间中放的是进程图像

```bash
❯ gcc p.c
❯ ./a.out
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>

int main(){
    int fd;
    fd=open("./p.c",O_RDONLY);
    off_t len=lseek(fd,0,SEEK_END);
    lseek(fd,0,SEEK_SET);
    char *buffer=malloc(len);
    read(fd,buffer,len);
    printf("%s\n",buffer);
    free(buffer);
    close(fd);

    return 0;
}


```


