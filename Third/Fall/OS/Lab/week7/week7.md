- `fork()`：duplicate，创建子进程，与父进程同时进行
- `exec()`：改变进程图像，执行其它语言程序
- `signal()`：处理信号
	- 单步、断点
	- 程序异常退出
	- 特殊：信号丢失
- `kill`：send signal
- `pause()`

```bash
❯ screen
[detached from 7460.pts-6.TABLET-U5TVFJBL]
❯ cat p.c
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
❯ ps -a |grep a.out
   7532 pts/5    00:00:00 a.out
❯ kill -30 7532
❯ kill -31 7532
❯ screen -r
[detached from 7460.pts-6.TABLET-U5TVFJBL]

```

```bash
❯ ./a.out
30 signal received
31 signal received

```
