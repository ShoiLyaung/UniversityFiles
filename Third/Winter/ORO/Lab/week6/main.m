A = [-1 3 1 0; 7 1 0 1]; 
b = [6 35]'; 
c = [7 9 0 0]';
[xstar,fxstar] = BranchBound(A, b, c);