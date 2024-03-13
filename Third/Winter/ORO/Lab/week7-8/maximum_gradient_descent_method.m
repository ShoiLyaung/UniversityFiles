% 调用函数接口
[xstar,fxstar,iter] = SteepDescent(@Myexam1,[1,1]',1e-3)

% testing data
function [f,g]=Myexam1(x)     
%%%%调用[f,g] = feval(f_name,xk);
f=x(1)^2+2*x(2)^2; 
g=[2*x(1);4*x(2)];
end

% SteepDescent
function [xstar,fxstar,iter] = SteepDescent(f_name,x0,eps)
iter=0;
[~,g]=Myexam1(x0);
x=x0;
dk=-g;
while norm(g)>eps
    iter=iter+1;
    [b] = Trial(@Myexam1,x,dk,1,0.1,eps);   % 确定搜索区间
    [lamda]=S618(@Myexam1,x,dk,[0,b],eps);  % 0.618法搜索步长
    x_0=x;
    x=x_0+lamda*dk;
    [~,g]=Myexam1(x);
    dk=-g; 
    s1 =sqrt((x - x_0)'*(x - x_0));
    if s1 <= eps
        break;
    end
end
xstar=x;
[fxstar,~]=Myexam1(xstar);
end

% 确定区间右端点
function [b] = Trial(f_k,xk,dk,a0,h0,eps)
f0 = feval(f_k,xk+a0*dk);
a1 = a0 + h0;
f1 = feval(f_k,xk+a1*dk);
while abs(f1-f0)<eps
    a1 = a1 + h0;
    f1 = feval(f_k,xk+a1*dk);
end
b=a1;
while f1<=f0
    a1=a1+ h0;
    f1=feval(f_k,xk+a1*dk);
end
b=a1;
end

% 0.618法搜索步长
function [x] = S618(f_name,xk,dk,range,e)
% xk: 当前搜索点
% dk: 当前搜索方向
% e: 精度要求
a = range(1);b = range(2);
flag = 0;
while flag==0
    u = a+0.382*(b-a); 
    v = a+0.618*(b-a);
    m = feval(f_name,xk+u*dk); 
    n = feval(f_name,xk+v*dk);
    if m>n
        if b-u<e
            x = v; 
            flag = 1;
        else
            a = u;
            flag = 0;
        end
    else
        if v-a<e
            x = u; 
            flag = 1;
        else
            b=v;
            flag = 0;
        end
    end
end
end