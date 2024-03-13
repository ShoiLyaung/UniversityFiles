A = [1;0.5];
B = [0.1,0.5,1];
C = [0.2,1];
%A和B的直积
AB = zeros(2, 3);
for i = 1:2
    for j = 1:3
        AB(i,j)=min(A(i),B(j));
    end
end
%转为列向量
T1=[];
for i = 1:2
    for j =1:3
        T1=[T1;AB(i,j)];
    end
end
%求R
for i = 1:6
    for j = 1:2
        R(i,j)=min(T1(i),C(j));
    end
end

A1 = [0.8;0.1];
B1 = [0.5,0.2,0];
AB1 = zeros(2, 3);
for i = 1:2
    for j = 1:3
        AB1(i,j)=min(A1(i),B1(j));
    end
end

T2 =[];
for i = 1:2
    for j =1:3
        T2=[T2,AB1(i,j)];
    end
end

for i = 1:6
    for j = 1:2
        D(i,j) = min(T2(i),R(i,j));
        C1(j) = max(D(:,j));
    end
end
disp(C1)