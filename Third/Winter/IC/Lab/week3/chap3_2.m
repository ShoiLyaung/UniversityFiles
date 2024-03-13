% 典型隶属函数仿真程序:chap3_2.m
% Membership function
clear; 
close all;

M=3;

if M==1
    x=0:0.01:10;
    y=gaussmf(x,[2 5]);
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
    title('Gaussian membership function');
elseif M==2     % Generalized bell membership function
    x=0:0.1:10;
    y=gbellmf(x,[2 4 6]);
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
    title('Generalized bell membership function');
elseif M==3     % Sigmoid membership function
    x=0:0.1:10;
    y=sigmf(x,[-2 4]);
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
    title('Sigmoid membership function');
elseif M==4     % Trapezoidal membership function
    x=0:0.1:10;
    y=trapmf(x,[1 5 7 8]);
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
    title('Trapezoidal membership function');
elseif M==5     % Triangular membership function
    x=0:0.1:10;
    y=trimf(x,[3 6 8]);
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
    title('Triangular membership function');
elseif M==6     % Z-shaped membership function
    x=0:0.1:10;
    y=zmf(x,[3 7]);
    plot(x,y,'k');
    xlabel('x');
    ylabel('y');
    title('Z-shaped membership function');
end
