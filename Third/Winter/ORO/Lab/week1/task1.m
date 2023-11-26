m = 3;
n = 8;

flag = 0;
while flag < m
    A = insertUnitMatrices(m, n);
    for level = 1:m
        unitMatrices = eye(level);
        for i = 1:(n-level+1)
            for j = 1:(m-level+1)
                submatrix = A(j:j+level-1, i:i+level-1);
                % 检查是否为单位矩阵
                if isequal(submatrix, unitMatrices)
                    disp(['在列 ', num2str(i), ' 发现阶数为 ', num2str(level), ' 的单位矩阵']);
                    flag = max(flag, level);
                end
            end
        end
    end
end

function [A] = insertUnitMatrices(m, n)
    A = 10 * rand(m, n);
    I = eye(m, m);
    randIndex = randperm(size(A, 2));
    A(:, randIndex(1:m)) = I;
    disp('生成的矩阵 A:');
    disp(A);
end
