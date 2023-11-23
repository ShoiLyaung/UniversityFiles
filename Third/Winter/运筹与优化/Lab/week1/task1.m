m = 3;
n = 8;

A = 10 * rand(m, n);
% disp('生成的矩阵 A:');
% disp(A);

I = eye(m, m);
% disp('生成的矩阵 I:');
% disp(I);

randIndex = randperm(size(A, 2));
% disp(randIndex);
A(:, randIndex(1:m)) = I;
disp('生成的矩阵 A:');
disp(A);


% 
% % 判断是否存在单位矩阵
% isUnitMatrix = isequal(A(:, randIndex(1:m)), I);
% 
% if isUnitMatrix
%     disp('存在单位矩阵');
%     % 给出所在列
%     columnIndices = randIndex(1:m);
%     disp('单位矩阵所在列：');
%     disp(columnIndices);
% else
%     disp('不存在单位矩阵');
% end

foundUnitMatrix = false;
columnIndices = [];

% % 仅靠考虑m*m
% for i = 1:(n - m + 1)
%     if isequal(A(:, i:(i+m-1)), I)
%         foundUnitMatrix = true;
%         columnIndices = i:(i+m-1);
%         break;
%     end
% end


% 考虑1*1和2*2
for i = 1:(n - m + 1)
    for j = 1:(m - 1)
        subMatrix = A(:, i:(i+j-1));
        
        % Check if the subMatrix is an identity matrix
        if isequal(subMatrix, eye(size(subMatrix)))
            foundUnitMatrix = true;
            columnIndices = i:(i+j-1);
            break;
        end
    end
    
    if foundUnitMatrix
        break;
    end
end

% 输出结果
if foundUnitMatrix
    disp('存在单位矩阵');
    disp('单位矩阵所在列：');
    disp(columnIndices);
else
    disp('不存在单位矩阵');
end
