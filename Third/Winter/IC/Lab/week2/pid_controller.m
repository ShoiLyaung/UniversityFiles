clear all;
close all;
ts=0.001;
sys=tf(5.235e005,[1,87.35,1.047e004,0]); %Plant
dsys=c2d(sys,ts,'z');
[num,den]=tfdata(dsys,'v');
u_1=0;u_2=0;u_3=0;u_4=0;
y_1=0;y_2=0;y_3=0;
ei=0;
kp=0.96;ki=0.03;kd=0.01;
error_1=0;
for k=1:1:500
time(k)=k*ts;
yd(k)=1.0;
y(k)=-den(2)*y_1-den(3)*y_2-den(4)*y_3+num(1)*u_1+num(2)*u_2+num(3)*u_3+num(4)*u_4;
error(k)=yd(k)-y(k); % Calculating P
derror(k)=error(k)-error_1; % Calculating D
ei=ei+error(k)*ts;
u(k)=kp*error(k)+kd*derror(k)/ts+ki*ei; %PID Controller
u_4=u_3;u_3=u_2;u_2=u_1;u_1=u(k);
y_3=y_2;y_2=y_1;y_1=y(k);
error_1=error(k);
end
figure(1);
plot(time,yd,'b',time,y,'r','linewidth',2);
xlabel('time(s)');ylabel('r,y');
figure(2);
plot(time,yd-y,'r','linewidth',2);
xlabel('time(s)');ylabel('error');