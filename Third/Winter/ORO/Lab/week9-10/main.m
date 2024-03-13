syms x1 x2
penalty_func=(x1-2)^2+(x2-1)^2;
g=[-0.25*x1^2-x2^2+1];%修改成大于等于形式
h=[x1-2*x2+1];

x0=[2 2];
eps=1e-3;

[xstar, fxstar, iter] = penalty(penalty_func, g,h, x0, eps)

function [xstar, fxstar, iter] = penalty(penalty_func, g,h, x0, eps)
M=0.01;
C=3;
[xstar,fxstar, iter]=waidian_hunhe(penalty_func,g,h,x0,M,C,eps,100)
end


function [x,result,n]=waidian_hunhe(f,g,h,x0,M,C,eps,k)
% f 目标函数
% g 不等式约束函数矩阵
% h 等式约束函数矩阵
% x0 初始值
% M 初始惩罚因子
% C 罚因子放大倍数
% eps 退出容差
% 循环次数
 
CF=sum(h.^2);  %chengfa
n=1;
while n<k
    %首先判断是不是在可行域内
    gx=double(subs(g,symvar(g),x0));%计算当前点的约束函数值
    index=find(gx<0);%寻找小于0的约束函数
    F_NEQ=sum(g(index).^2);
    F=matlabFunction(f+M*F_NEQ+M*CF);
    x1=Min_Newton(F,x0,eps,100);
    x1=x1'
    if norm(x1-x0)<eps
        x=x1;
        result=double(subs(f,symvar(f),x));
        break;
    else
        M=M*C;
        x0=x1;
    end
    n=n+1;
end
end

%牛顿法
function [X,result]=Min_Newton(f,x0,eps,n)
%f为目标函数
%x0为初始点
%eps为迭代精度
%n为迭代次数
TiDu=gradient(sym(f),symvar(sym(f)));% 计算出梯度表达式
Haisai=jacobian(TiDu,symvar(sym(f)));
Var_Tidu=symvar(TiDu);
Var_Haisai=symvar(Haisai);
Var_Num_Tidu=length(Var_Tidu);
Var_Num_Haisai=length(Var_Haisai);
TiDu=matlabFunction(TiDu);
flag = 0;
if Var_Num_Haisai == 0  %也就是说海塞矩阵是常数
    Haisai=double((Haisai));
    flag=1;
end
%求当前点梯度与海赛矩阵的逆
f_cal='f(';
TiDu_cal='TiDu(';
Haisai_cal='Haisai(';
for k=1:length(x0)
    f_cal=[f_cal,'x0(',num2str(k),'),'];
    
    for j=1: Var_Num_Tidu
        if char(Var_Tidu(j)) == ['x',num2str(k)]
            TiDu_cal=[TiDu_cal,'x0(',num2str(k),'),'];
        end
    end
    
    for j=1:Var_Num_Haisai
        if char(Var_Haisai(j)) == ['x',num2str(k)]
            Haisai_cal=[Haisai_cal,'x0(',num2str(k),'),'];
        end
    end
end
Haisai_cal(end)=')';
TiDu_cal(end)=')';
f_cal(end)=')';
switch flag
    case 0
        Haisai=matlabFunction(Haisai);
        dk='-eval(Haisai_cal)^(-1)*eval(TiDu_cal)';
    case 1
        dk='-Haisai^(-1)*eval(TiDu_cal)';
        Haisai_cal='Haisai';
end
i=1;
while i < n 
    if abs(det(eval(Haisai_cal))) < 1e-6
        disp('逆矩阵不存在！');
        break;
    end
    x0=x0(:)+eval(dk);
    if norm(eval(TiDu_cal)) < eps
        X=x0;
        result=eval(f_cal);
        return;
    end
    i=i+1;
end
disp('无法收敛！');
X=[];
result=[];
end