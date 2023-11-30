%Expert PID Controller
clear all;
clc;
close all;
ts=0.001;  %采样时间

sys=tf(5.235e005,[1,87.35,1.047e004,0]);  %被控对象传递函数
dsys=c2d(sys,ts,'z'); %z变换，离散化
[num,den]=tfdata(dsys,'v');  %获得离散化模型的分子分母多项式系数。

u_1=0;u_2=0;u_3=0;   %控制变量u(k-1), u(k-2), u(k-3)初值
y_1=0;y_2=0;y_3=0;   %输出变量y(k-1), y(k-2), y(k-3)初值

x=[0,0,0]';          %误差，误差微分项，误差积分项
x2_1=0;

kp=0.6;
ki=0.03;     
kd=0.01;
% 上面是利用常规方法整定的PID参数值
error_1=0;  %误差e(k-1)初始值
for k=1:1:500
time(k)=k*ts;    %第k步的时间
   
r(k)=1.0;                    %输入为单位阶跃信号

u(k)=kp*x(1)+kd*x(2)+ki*x(3); %PID Controller

%Expert control rule
if abs(x(1))>0.8      %Rule1:误差特别大时开环控制（分段定值控制）
   u(k)=0.45;
elseif abs(x(1))>0.40        
   u(k)=0.40;
elseif abs(x(1))>0.20    
   u(k)=0.12; 
elseif abs(x(1))>0.01 
   u(k)=0.10;   
end   

if x(1)*x(2)>0|(x(2)==0)       %Rule2：误差绝对值增加时
   if abs(x(1))>=0.05
      u(k)=u_1+2*kp*x(1);       %误差较大时控制规则
   else
      u(k)=u_1+0.4*kp*x(1);     %误差较小时控制规则
   end
end
                                                                                                                                                                                                                                                                                                                                                                                                              
if (x(1)*x(2)<0&x(2)*x2_1>0)|(x(1)==0)   %Rule3：误差绝对值减小时，保持不变
    u(k)=u(k);
end

if x(1)*x(2)<0&x(2)*x2_1<0   %Rule4：误差处于极值状态时
   if abs(x(1))>=0.05
      u(k)=u_1+2*kp*error_1;  %误差极值较大时
   else
      u(k)=u_1+0.6*kp*error_1;  %误差极值较小时
   end
end

if abs(x(1))<=0.001   %Rule5:误差小于要求时，采用PI控制调节稳态误差
   u(k)=0.5*x(1)+0.010*x(3);
end

%Restricting the output of controller
if u(k)>=10
   u(k)=10;
end
if u(k)<=-10
   u(k)=-10;
end

%下面为离散化的被控对象模型
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(1)*u(k)+num(2)*u_1+num(3)*u_2+num(4)*u_3;
error(k)=r(k)-y(k);

%----------Return of parameters------------%
u_3=u_2;u_2=u_1;u_1=u(k);  %更新控制变量
y_3=y_2;y_2=y_1;y_1=y(k);  %更新输出变量
   
x(1)=error(k);                % 比例分量x(1)=e(k)
x2_1=x(2);                    %更新误差变化率
x(2)=(error(k)-error_1)/ts;   % 微分分量x(2)=e(k)-e(k-1)
x(3)=x(3)+error(k)*ts;        % 积分分量x(3)=Σe(k)

error_1=error(k);             %更新误差e(k-1):e(k-1)=e(k)
end
figure(1);
plot(time,r,'b',time,y,'r');
xlabel('time(s)');ylabel('r,y');
figure(2);
plot(time,r-y,'r');
xlabel('time(s)');ylabel('error');