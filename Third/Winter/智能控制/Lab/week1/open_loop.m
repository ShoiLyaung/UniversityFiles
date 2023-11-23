clc;
clear;
% 定义系统参数
Ra=1; Km=10;J=2;b=0.5;Kb=0.1;

% 创建系统传递函数 sys1: G(s) = 1 / (Js + b)
num1=[1];den1=[J,b];sys1=tf(num1,den1);
% 创建系统传递函数 sys2: H(s) = Km * Kb / Ra
num2=[Km*Kb/Ra];den2=[1];sys2=tf(num2,den2);
% 反馈组合系统：sys_o = G(s) / (1 + G(s) * H(s))
sys_o=feedback(sys1,sys2);

% 将闭环系统反转符号
sys_o=-sys_o

% 分析阶跃响应
[yo,T]=step(sys_o);

% 绘制阶跃响应曲线
plot(T,yo);
title('Open-loop Disturbance Step Response')
xlabel('Time(sec)'),ylabel('\omega_o'),grid

% 输出阶跃响应的最终值
yo(length(T))

% 生成单位阶跃输入信号
t_input = linspace(0, max(T), length(T));
u_step = ones(size(t_input));
% 计算实际输出
actual_value=u_step+yo;

% 绘制阶跃响应曲线和单位阶跃输入信号
plot(t_input, actual_value,t_input, u_step,  '--', 'LineWidth', 2);
legend('System Response', 'Actual Value');