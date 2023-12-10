function [x_opt, fx_opt, iter] = Simplex_eye(A, b, c)
    % 初始化
    [m, n] = size(A);
    c_b = zeros(1, m); % 基变量对应的目标函数系数
    B = eye(m); % 基矩阵
    x_b = b; % 基变量的取值
    
    % 计算初始解
    x = zeros(n, 1);
    x(find(ismember(1:n, find(x_b > 0)))) = x_b(x_b > 0);
    z = c * x;

    % 主循环
    iter = 0;
    while true
        % 计算单纯形法表
        tableau = [c - c_b * inv(B) * A, c_b * inv(B) * b; A - B * A, b - B * b];

        % 检查是否达到最优解
        if all(tableau(1, 1:n) >= 0)
            x_opt = x;
            fx_opt = z;
            return;
        end

        % 选择进基变量
        entering_index = find(tableau(1, 1:n) < 0, 1);

        % 选择出基变量
        ratios = tableau(2:m + 1, n + 1) ./ tableau(2:m + 1, entering_index);
        exiting_index = find(ratios > 0, 1) + 1;

        % 更新基矩阵和基变量
        B(exiting_index - 1, :) = A(:, entering_index);
        x_b(exiting_index - 1) = x(entering_index);

        % 更新基变量对应的目标函数系数
        c_b = c(ismember(1:n, find(x_b > 0)));

        % 更新解和目标函数值
        x = zeros(n, 1);
        x(find(ismember(1:n, find(x_b > 0)))) = x_b(x_b > 0);
        z = c * x;

        iter = iter + 1;
    end
end
