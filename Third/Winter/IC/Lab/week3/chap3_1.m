M=3;
if M==1
    % Membership function for Middle Age People
    for k=1:1:201
        x(k)=k;
    if x(k)>=0 && x(k)<=25
        y(k)=0.0;
    elseif x(k)>25 && x(k)<=70
        y(k)=gaussmf(k,[5 40]);
    elseif x(k)>70 && x(k)<=200
        y(k)=0.0;
    else
        y(k)=0.0;
    end
    end
    plot(x,y,'LineWidth',2)
    xlabel('x Years')
    ylabel('Degree of membership') 
    xlim([0 200])
elseif M==2
    % Membership function for Old People
    for k=1:1:201
        x(k)=k;
    if x(k)>=0 & x(k)<=50
        y(k)=0.0;
    elseif x(k)>50 & x(k)<=70
        y(k)=(k-50)/20;
    elseif x(k)>70 & x(k)<=200
        y(k)=1;
    else
        y(k)=1.0;
    end
    end
    plot(x,y,'LineWidth',2)
    xlabel('x Years')
    ylabel('Degree of membership') 
    xlim([0 200])
elseif M==3
    % Membership function for Young People
    for k=1:1:201
        x(k)=k;
    if x(k)>=0 & x(k)<=25
        y(k)=1.0;
    elseif x(k)>25 & x(k)<=70
        y(k)=(70-k)/45;
    elseif x(k)>70 & x(k)<=200
        y(k)=0.0;
    else
        y(k)=0.0;
    end
    end
    plot(x,y,'LineWidth',2)
    xlabel('x Years')
    ylabel('Degree of membership') 
    xlim([0 200])
end