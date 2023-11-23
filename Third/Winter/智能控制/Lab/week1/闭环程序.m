clc;
clear;
Ra=1; Km=10;J=2;b=0.5;Kb=0.1;Ka=54;Kt=1;
num1=[1];den1=[J,b];sys1=tf(num1,den1);
num2=[Ka*Kt];den2=[1];sys2=tf(num2,den2);
num3=[Kb];den3=[1];sys3=tf(num3,den3);
num4=[Km/Ra];den4=[1];sys4=tf(num4,den4);
sysa=parallel(sys2,sys3);
sysb=series(sysa,sys4);
sys_c=feedback(sys1,sysb);
sys_c=-sys_c
[yc,T]=step(sys_c);
plot(T,yc);
title('Closed-loop Disturbance Step Response')
xlabel('Time(sec)'),ylabel('\omega_c(rad/sec)'),grid
yc(length(T))