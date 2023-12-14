close all;
figure(1);

plot(out.y.Time,out.y.Data(:,1),'r',out.y.Time,out.y.Data(:,2),'k:','linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('Ideal position signal','position tracking');