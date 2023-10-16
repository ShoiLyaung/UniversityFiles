# ls
- 文件类型

| 文件类型 |              |              |
| -------- | ------------ | ------------ |
| `-`      | regular      | 正规文件     |
| `d`      | directory    | 目录         |
| `l`      | link         | 符号链接     |
| `c`      | character    | 字符设备文件 |
| `b`      | block        | 块设备文件   |
| `p`      | pipe         | 管道         |
| `s`      | socket       | 套接字文件   |

- 设备
	- 只有输入输出设备
	- 通过文件访问设备
- 管道
	- 可执行文件之间的相接方式 -> **用小程序实现大功能**

# echo
注意 \` 与 \' 的区别
```bash
❯ abc='ls'
❯ echo $abc
ls
❯ abc=`ls`
❯ echo $abc
cuda-repo-ubuntu2204-12-2-local_12.2.0-535.54.03-1_amd64.deb
cudnn_samples_v8
Desktop
Documents
Downloads
MC
Music
Pictures
Programs
Public
quick_start.sh
Templates
Videos
```

```bash
❯ echo 'aall!'
aall!
❯ echo "aall\!"
aall!
❯ echo "aall!"
dquote>
```

# env

# if []; then ; fi ;

