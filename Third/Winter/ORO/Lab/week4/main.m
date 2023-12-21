A = [-1, -2, -1, 1, 0,;
     -2,  1, -3, 0, 1,];
b = [-3; -4];
c = [-2; -3; -4; 0; 0];

[x_opt, fx_opt, iter] = DualSimplex_eye(A, b, c);
disp('最优解:');
disp(x_opt);
disp('最优函数值:');
disp(fx_opt);
disp('迭代次数:');
disp(iter);
