
```bash
❯ cat p.c
#include<stdio.h>
#include<stdlib.h>
int main()
{
        printf("Hello World!\n");
        return 123;
}
❯ gcc p.c
❯ ./a.out
Hello World!
❯ echo $?
123
```

- ``return``的值是八位（256）
```bash
❯ cat p.c
#include<stdio.h>
#include<stdlib.h>
int main()
{
        printf("Hello World!\n");
        return 123+256;
}
❯ gcc p.c
❯ ./a.out
Hello World!
❯ echo $?
123
```

```bash
❯ cat r.c
#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[])
{
        int i;
        for(i=0;i<argc;i++)
        {
                printf("%d%s\n",i,argv[i]);
        }
        return 0;
}
❯ ./a.out
0./a.out
❯ ./a.out 123 456 abc ddd
0./a.out
1123
2456
3abc
4ddd
```

```bash
❯ cat q.c
#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[],char **envp)
{
        int i;
        for(i=0;;i++)
        {
                if(envp[i]==NULL)
                        break;
                printf("%s\n",envp[i]);
        }
        return 0;
}
❯ gcc q.c
❯ ./a.out
HOSTTYPE=x86_64
LANG=C.UTF-8
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0/:/mnt/c/Windows/System32/OpenSSH/:/mnt/c/Program Files/Microsoft VS Code/bin:/mnt/c/Program Files/Git/cmd:/mnt/c/Users/d2596/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/d2596/AppData/Local/Programs/oh-my-posh/bin
TERM=xterm-256color
XDG_RUNTIME_DIR=/run/user/1000/
DISPLAY=:0
WAYLAND_DISPLAY=wayland-0
PULSE_SERVER=unix:/mnt/wslg/PulseServer
WSL2_GUI_APPS_ENABLED=1
WSLENV=WT_SESSION::WT_PROFILE_ID
WT_SESSION=b7bfcd5e-9cb8-489c-9e66-977062d6fc5c
WT_PROFILE_ID={51855cb2-8cce-5362-8f54-464b92b32386}
WSL_INTEROP=/run/WSL/397_interop
NAME=TABLET-U5TVFJBL
HOME=/home/sl
USER=sl
LOGNAME=sl
SHELL=/bin/zsh
WSL_DISTRO_NAME=Ubuntu
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
SHLVL=1
PWD=/home/sl/OS
OLDPWD=/home/sl
P9K_TTY=old
_P9K_TTY=/dev/pts/0
ZSH=/home/sl/.oh-my-zsh
PAGER=less
LESS=-R
LSCOLORS=Gxfxcxdxbxegedabagacad
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
P9K_SSH=0
_P9K_SSH_TTY=/dev/pts/0
_=/home/sl/OS/./a.out
```


```bash
❯ cat q.c
#include<stdio.h>
#include<stdlib.h>
int main(int argc,char *argv[])
{
        int i;
        for(i=0;i<argc;i++)
        {
                printf("%s      %s\n",argv[i],getenv(argv[i]));
        }
        return 0;
}
❯ ./a.out HOME PATH PWD
./a.out (null)
HOME    /home/sl
PATH    /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0/:/mnt/c/Windows/System32/OpenSSH/:/mnt/c/Program Files/Microsoft VS Code/bin:/mnt/c/Program Files/Git/cmd:/mnt/c/Users/d2596/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/d2596/AppData/Local/Programs/oh-my-posh/bin
PWD     /home/sl/OS
```




