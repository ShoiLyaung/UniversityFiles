function [xstar,fxstar,iter] = Gomory(A,b,c)
format rat

iter=0;
while true
    [m,n]=size(A);
    if min(b)>=0
        [x_opt,fx_opt,CA,Cb]=Simplex_eye(A,b,c);
    else
        [x_opt,fx_opt,CA,Cb]=DSimplex_eye(A,b,c);
    end
    flag=1;
    for pos_x = 1:m
        if abs(round(x_opt(pos_x))-x_opt(pos_x))>=1e-3
            flag=0;
            break;
        end
    end
    if flag==1 
        xstar=x_opt;
        fxstar=fx_opt;
        break;
    end
    iter=iter+1;
    sub=0;
    row=0;
    
    for r=1:m
        t=abs(floor(x_opt(r))-x_opt(r));
        if t>sub
            sub=t;
            row=r;
        end
    end
    n=n+1;
    m=m+1;
    iter=iter+1;
    temp_A=zeros(m,n);
    temp_b=zeros(m,1);
    temp_c=zeros(1,n);
    for i=1:m-1
        for j=1:n-1
            temp_A(i,j)=CA(i,j);
        end
        temp_b(i,1)=Cb(i,1);
    end
    temp_b(m,1)=floor(Cb(row,1))-Cb(row,1);
    temp_A(m,n)=1;
    for i =1:n-1
        temp_c(1,i)=c(i);
    end
    for i=1:n-1
        if temp_A(row,i)==0
            temp_A(m,i)=0;
        else
            temp_A(m,i)=floor(temp_A(row,i))-temp_A(row,i);
        end
    end
    A=temp_A;
    b=temp_b;
    c=temp_c;
end         
end

function [x_opt,fx_opt,A,b] = Simplex_eye(A,b,c)
format rat

[m,n]=size(A); 
v=nchoosek(1:n,m);
for i=1:size(v,1)
    if A(:,v(i,:))==eye(m)
        XB=v(i,:);
    end
end

Y=setdiff(1:n, XB);
ST=[];
iter=0;
while true
    x_opt=zeros(n,1);
    x_opt(XB)=b;
    cB=c(XB);
    S=zeros(1,n);
    S(Y)=c(Y)-cB*A(:,Y);
    [~, k]=max(S);
    T=b./A(:,k);
    T(T<=0)=10000;
    [~, q]=min(T);
    el=XB(q);
    vals=[cB',XB',b,A,T];
    vals=[vals; NaN, NaN, NaN, S, NaN];
    ST=[ST; vals];
    disp(ST);
    if all(S<=0)   
        x_opt=x_opt;
        fx_opt=c*x_opt;
        return
    end
    if all(A(:,k)<=0)
        x_opt=[];
        break
    end
    XB(XB==el)=k;
    Y=setdiff(1:n, XB);
    A(:,Y)=A(:,XB)\A(:,Y);
    b=A(:,XB)\b;
    A(:,XB)=eye(m,m);
    iter=iter+1
end
end

function [x_opt,fx_opt,A,b] = DSimplex_eye(A,b,c)
format rat
[m,n]=size(A);
XB=has_ones(A);
Y=setdiff(1:n,XB); 

while true
    x_opt=zeros(n,1);
    x_opt(XB)=b;
    cB=c(XB);
    if ~any(b<0)   
        x_opt=x_opt;
        fx_opt=c*x_opt;
        return
    end
    index=find(b<0);
    for i=1:numel(index)
        if all(A(index(i),:)>=0)
            x_opt=[];
            fx_opt=[];
            return
        end
    end
    S=zeros(1,n);
    S(Y)=c(Y)-cB*A(:,Y);
    [~,q]=min(b);
    r=XB(q);
    T=S./A(q,:);
    T(T<=0)=10000;
    [~,s]=min(T);
    

    XB(XB==r)=s;
    Y=setdiff(1:n,XB);
    A(:,Y)=A(:,XB)\A(:,Y);
    b=A(:,XB)\b;
    A(:,XB)=eye(m,m);
end
end

function [index]=has_ones(a)
    [m,n]=size(a);
    b=min(m,n);
    one=eye(b);
    index=[];
    result=zeros(m,1);
    for i =1:n
        for j=1:b
            if a(:,i)==one(:,j)
                index=[index,i];
                break;
            end
        end
    end
    for k=index
        result=result+a(:,k);
    end
    if result~=ones(m,1)
       index=[];
    end
end
