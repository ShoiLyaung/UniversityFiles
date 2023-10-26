1. 启动nfs服务器，并使其成为开机启动项：
	1. `systemctl start rpcbind nfs-server`
	2. `systemctl enable rpcbind nfs-server`
2. 创建目录
	1. `vi /etc/exports`
	2. `[目录]:/home/sl/Documents/COA/Lab/lab3 客户端地址:192.168.1.6`
	3. `[/home开始目录] [客户端地址](rw,sync,no_root_squash,no_subtree_check)`
3. 配置与防火墙
	1. `sudo exportfs -a`
	2. `firewall-cmd --permanent --zone=public --add-service=nfs`
	3. `firewall-cmd --permanent --zone=public --add-service=mountd`
	4. `firewall-cmd --permanent --zone=public --add-service=rpc-bind`
	5. `firewall-cmd --reload`
	6. `systemctl restart nfs`
4. 客户端
	1. `[服务端地址]：192.168.1.5 [目录]:/home/sl/Documents/COA/Lab/lab3`
	2. `showmount -e [服务端地址]`
	3. `rpcinfo -p [服务端地址]`
	4. `mount [服务端地址]:[服务端目录] [客户端目录]`
5. 检查文件夹信息：`df -h`
