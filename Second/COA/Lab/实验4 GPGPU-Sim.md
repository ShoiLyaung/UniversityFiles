1. 编译
	- 在`~/cuda/sdk/4.2/C/src/vectorAdd`文件夹下`make`
2. 运行
	- `./run_gpgpu-sim.sh ~/cuda/sdk/4.2/C/bin/linux/release/vectorAdd`
3. 运行结果信息：`/home/gpgpu-sim/GTX480_rundir`
	1. `stdout.txt`：
		- gpu_sim_cycle记录了在该GPU中执行该程序所需的周期数量。$执行时间=周期数×时钟周期（时钟周期由具体硬件决定，为常量）$
		- gpu_sim_insn记录了该程序编译后一共包含的指令数量
		- 由指令数量与周期数量的对比，可以看出GPU对该程序实现了较高的加速。
	2. 在C语言代码（vectorAdd.cu）中修改程序参数：==线程数`threadsPerBlock`==与==向量大小`N`==
	3. GTX480硬件配置文件在`gpgpusim.config`：
		- 在配置文件中修改以下参数的值（其它参数不要修改）：
			- ==`gpgpu_n_cores_per_cluster`==表示每个GPU节点中所包含的streaming multiprocessor的数量

