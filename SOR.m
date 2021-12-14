clc 
clear

A = [4.63 -1.21 3.22; -3.07 5.48 2.11; 1.26 3.11 4.57];
b = [2.22; -3.17; 5.11];
err = 1;
x = [0,0,0];
n = 3;
tol = 10^-3;
w = 1.2;

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
        x(i) = (1-w)*x(i)+w*((b(i)-s)/A(i,i));

        err = x - xold;
    end
end

x
