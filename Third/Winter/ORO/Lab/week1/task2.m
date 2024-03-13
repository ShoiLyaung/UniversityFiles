A = [1 2 3; -1 3 7; 9 0 3];
b = [1 4 7]';
x = gauss_elim(A, b);
disp(x);

function x = gauss_elim(A, b)
    % 确保A是方阵
    [m, n] = size(A);
    if m ~= n
        error('输入矩阵A必须是方阵');
    end

    % 将增广矩阵合并
    Ab = [A, b];

    % 高斯消元
    for i = 1:n
        % 将当前列的主元调整为非零
        if Ab(i, i) == 0
            [~, max_row] = max(abs(Ab(i:end, i)));
            max_row = max_row + i - 1;
            Ab([i, max_row], :) = Ab([max_row, i], :);
        end

        % 将当前列的其他元素消为零
        for j = i+1:n
            factor = Ab(j, i) / Ab(i, i);
            Ab(j, :) = Ab(j, :) - factor * Ab(i, :);
        end
    end

    % 回代得到解x
    x = zeros(n, 1);
    for i = n:-1:1
        x(i) = (Ab(i, end) - Ab(i, i+1:end-1) * x(i+1:end)) / Ab(i, i);
    end
end
