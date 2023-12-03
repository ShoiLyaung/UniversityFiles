function [xs, Bs, x_num] = BFS(A, b)
    [m, n] = size(A);
    
    % 初始化 xs、Bs 和 x_num
    xs = [];
    Bs = [];
    % 检查行数和列数关系
    if m < n
        x_num = inf;
        disp('约束矩阵行数小于列数，存在无穷多解。');
        disp('x_num=');
        disp(x_num);
    else
        I = eye(m);
    
        % 初始基矩阵
        Bs = I(:, 1:n);
        
        % 初始基本可行解
        xs = zeros(n, 1);
        
        % 检查约束是否满足
        if rank(Bs) == m
            xs = Bs\b;
            x_num = 1;
            % 显示结果
            disp('基本可行解:');
            disp(xs);
            disp('对应的基矩阵:');
            disp(Bs);
            disp('基本可行解的数量:');
            disp(x_num);
        else
            x_num = 0;
            disp('基本可行解的数量:');
            disp(x_num)
        end
    end
    disp('-----------------------');
end
