function [x_opt,fx_opt,iter]=Simplex_eye(A,b,c)
    %% 初始化
    format rat
    [m,n]=size(A); 
    x_opt=[A,b];
    c_j=c; %记录检验数
    c_n=c_j(1:n);  %记录非基变量的价值系数矩阵
    c_b=c_j(n-m+1:n); %记录基变量的价值系数矩阵
    theta=zeros(1,n); %θ规则
    id_B=(n-m+1:n); %基变量的索引
    id_N=(1:n);  %非基变量的索引
    k=0;%换入变量下标
    l=0;%换出变量下标
    iter=0;
    flag=0; % flag记录解的情况 1是无界解
    %% 进入迭代
    while ~all(c_j<=0)
        iter=iter+1;
        %% 判断是否为无界解
        for i=1:n
            if c_n(i)>0
                if all(x_opt(:,id_N(i))<=0) 
                    disp('该线性规划问题有无界解');
                    flag=1;
                    break
                end      
            end
        end 
        if flag
            break
        else
        %% 根据检验数中最大值所在列找到换入变量
        k=find(c_j==max(c_j));
        g=find(x_opt(:,k)>0);
        %% 确定换出变量
        theta=(b(g,1)./x_opt(g,k));
        theta
        l=g(theta==min(theta));
        %% 换入变量替换换出变量 非基变量与出基变量索引的对换
        id_N(id_N==k)=id_B(l);
        id_B(l)=k;
        %% 确定主元素坐标(l,k) 进行矩阵变换 
        m= size(x_opt,1); 
        b = x_opt(l,k); 
        x_opt(l,:)=x_opt(l,:)/b;
        for i = [1:l-1,l+1:m]  
            x_opt(i,:)= x_opt(i,:)-x_opt(i,k)*x_opt(l,:); % 把对应列的其他数化为0
        end
        x_opt
        %% 新的资源系数
        b=x_opt(:,n+1);
        %% 价值系数矩阵的变化以及检验数的变化   
        c_b=c_j(id_B);%记录基变量的价值系数
        c_n=c_j(id_N); %记录非基变量的价值系数矩阵
        c_j(id_B)=zeros(1,m);
        c_j(id_N)=c_n-c_b*x_opt(:,id_N);
        c_j
        end
    end
    c_n=c_j(id_N); %得到最后一次的非基变量的价值系数矩阵用于判断
    c_b=c(id_B); %得到最后一次的基变量的价值系数矩阵用于求最优值
    %% 无穷多最优解
    if ~all(c_n<0) && flag~=1
        disp('此线性规划问题有无穷多解')
        flag=2;
    end
     %% 最优解唯一的情况
     if flag==0
         disp('此线性规划问题有唯一的最优解')
     end
   fx_opt=c_b*b;
end