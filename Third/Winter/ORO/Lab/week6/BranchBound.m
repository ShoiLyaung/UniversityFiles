function [xstar, fxstar] = BranchBound(A, b, c)
lb = [0; 0;0;0];
ub=[inf;inf;inf;inf];

optX = [0; 0];
optVal = 0;
[xstar, fxstar] = BranchBound1(A, b, c, lb, ub, optX, optVal, 0)
end

function [xstar, fxstar] = BranchBound1(A, b, c, vlb, vub, optXin, optF, iter)
    global optX optVal optFlag;
    iter = iter + 1;
    optX = optXin; optVal = optF;
    
    [x, fit, status] = linprog(-c, A, b, [], [], vlb, vub);
    if status ~= 1
        xstar = x;
        fxstar = fit;
        return;
    end
    
    if max(abs(round(x) - x)) >= 1e-3
        if fit > optVal
            xstar = x;
            fxstar = fit;
            return;
        end
        
    else
        if fit > optVal
            xstar = x;
            fxstar = fit;
            return;
        else
            optVal = fit;
            optX = x;
            optFlag = status;
            xstar = x;
            fxstar = fit;
            return;
        end
    end
    midX = abs(round(x) - x);
    notIntV = find(midX > 1e-3);
    pXidx = notIntV(1);
    tempVlb = vlb;
    tempVub = vub;
    if vub(pXidx) >= fix(x(pXidx)) + 1
        tempVlb(pXidx) = fix(x(pXidx)) + 1;
        [~, ~] = BranchBound1(A, b, c, tempVlb, vub, optX, optVal, iter + 1);
    end
    
    if vlb(pXidx) <= fix(x(pXidx))
        tempVub(pXidx) = fix(x(pXidx));
        [~, ~] = BranchBound1(A, b, c, vlb, tempVub, optX, optVal, iter + 1);
    end
    xstar = optX;
    fxstar = optVal;
    fxstar = -fxstar;
end
