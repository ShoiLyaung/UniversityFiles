A = [2, -3, 2, 1, 0; 1/3, 1, 5, 0, 1];
b = [15; 20];
c = [1, 2, 1, 0, 0];

[x_opt, fx_opt, iter] = Simplex_eye(A, b, c);
disp('最优解:');
disp(x_opt);
disp('最优函数值:');
disp(fx_opt);
disp('迭代次数:');
disp(iter);
