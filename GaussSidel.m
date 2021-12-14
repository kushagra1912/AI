clc 
clear

A = [10 8 -3 1; 2 10 1 -4; 3 -4 10 1; 2 2 -3 10];
b = [16 , 9 , 10 , 11];
err = 1;
x = [0,0,0,0];
n = 4;
tol = 10^-5;

while (norm(err,inf)>tol)
    xold = x;
    for i = 1:n
            s = 0;
            for j = 1: i-1
                s = s + A(i,j)*x(j);
            end
            for j = i+1 : n
                s = s + A(i,j)*xold(j);
            end
        x(i) = (b(i) - s)/A(i,i);

        err = x - xold;
    end
end

x
