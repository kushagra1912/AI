clc
clear
a = [4 1 0; 1 20 1; 0 1 4];
x0 = [1 ; 1; 1];
n = 3;
tol = 10^-3;
N = 50
x = x0;
k(1) = 0;


for i = 2:n
    y = a*x;
    k(i) = norm(y, inf)
    x = (1/k(i))*y;
    if (abs(k(i)-k(i-1)))<tol
        k(i)
        break;
    else
        x0 = x;
        i = i+ 1;
    end
end
