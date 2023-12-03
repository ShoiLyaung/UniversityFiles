num_tests = 10; % 测试次数

size = 5;
% size = 100000;
A_range = 30;
% A_range = 3000000;
b_range = 30;
% b_range = 3000000;


for i = 1:num_tests
    % 生成随机的线性规划问题
    m = randi([2, size]); % 随机生成约束的数量
    n = randi([2, size]); % 随机生成变量的数量
    
    A = randi([-A_range, A_range], m, n); % 包括负数的取值范围
    b = randi([-b_range, b_range], m, 1); % 包括负数的取值范围
    
    disp('约束矩阵 A:');
    disp(A);
    disp('约束向量 b:');
    disp(b);
    % 求解线性规划问题
    [xs, Bs, x_num] = BFS(A, b);
end
