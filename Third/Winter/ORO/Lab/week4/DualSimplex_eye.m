function [x_opt, fx_opt, iter] = DualSimplex_eye(A, b, c)
    col = size(A,2);
    c1 = c';
    x(4,:) = b(1, :);
    x(5,:) = b(2, :);%初始化解矩阵
    x_opt = x;
    fx_opt = c1 * x_opt;
    iter = 0;
    idx_b = [4, 5];%基变量序号
    idx_nb = setdiff(1:col, idx_b);%非基变量
    cb = [0, 0];%基变量的价值系数
    while(true)  
        if(all(b(:)>=0))
            break
        end
        iter = iter + 1;%找出基
        temp1 = b;
        [~,q] = min(temp1);
        sigma = c1 - cb * A;
        s2 = sigma ./ A(q,:);
        temp2 = s2;
        temp2(temp2 <= 0) =inf;
        [~, p] = min(temp2);%p入基
        q = idx_b(q);
        idx_b(idx_b == q) = p;
        idx_nb = setdiff(1:col, idx_b);
        tmp = A(:, idx_b);
        A = inv(A(:, idx_b)) * A;
        b = tmp\b;
        x_opt(idx_b, :) = b;%构造最后的解
        x_opt(idx_nb, :) = 0;
        cb = c1(idx_b);
        fx_opt = c1 * x_opt;
        A(:, idx_b) = eye(2, 2);
    end
%     disp(x_opt);
%     disp(fx_opt);
%     disp(iter);
end
