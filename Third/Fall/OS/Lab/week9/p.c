#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<fcntl.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<sys/mman.h>

int main(){
    int fd=open("./p.c",O_RDONLY);
    off_t len=lseek(fd,SEEK_END,0);                     //取得文件长度
    char *p=mmap(NULL,len,PROT_READ,MAP_SHARED,fd,0);   //文件地址映射
    printf("%s\n",p);
    munmap(p,len);
    close(fd);
    return 0;
}
