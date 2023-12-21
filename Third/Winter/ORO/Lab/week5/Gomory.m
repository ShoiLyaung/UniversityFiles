function [xstar,fxstar,iter] = Gomory(A,b,c)
    [m, n] = size(A);
    xstar = zeros(n,1);
    fxstar = Inf;
    iter = 0;
    while true
        iter = iter + 1;

        % Solve LP relaxation
        [x,fval] = linprog(c,[],[],A,b,zeros(n,1));
        
        % Check if all variables are integer
        if all(abs(round(x) - x) < 1e-3)
            xstar = x;
            fxstar = fval;
            break;
        end
        
        % Find a violated constraint
        for i = 1:m
            if abs(round(x(i)) - x(i)) > 1e-3
                % Add the constraint to A and b
                newrow = zeros(1,n);
                newrow(i) = 1;
                A = [A; newrow];
                b = [b; floor(x(i))];
                break;
            end
        end
    end
end