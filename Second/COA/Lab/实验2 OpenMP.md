- psftp
	- `open [地址]`
	- `get [文件名]`
	- `put [文件名]`
- scp
	- ```scp root@[网络地址]:[文件地址] [文件地址]```
	- `scp [文件地址] root@[网络地址]:[文件地址]`
- OpenMP
	1. `echo |cpp -fopenmp -dM |grep -i openmp`
	2. `gcc hello.c -o hello -fopenmp`
	3. `export OMP_NUM_THREADS=16`
	4. `./hello`
	5.  `gcc matrix_multiply.c -o matrix_multiply -fopenmp`
	6. `export OMP_NUM_THREADS=16`
