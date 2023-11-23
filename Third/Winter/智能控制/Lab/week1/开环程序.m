clc;
clear;
Ra=1; Km=10;J=2;b=0.5;Kb=0.1;
num1=[1];den1=[J,b];sys1=tf(num1,den1);
num2=[Km*Kb/Ra];den2=[1];sys2=tf(num2,den2);
sys_o=feedback(sys1,sys2);
sys_o=-sys_o
[yo,T]=step(sys_o);
plot(T,yo);
title('Open-loop Disturbance Step Response')
xlabel('Time(sec)'),ylabel('\omega_o'),grid
yo(length(T))