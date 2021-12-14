clc
clear

n = 5;
x = [0 8 16 24 23 40];
f = [14.621 11.843 9.870 8.418 7.305 6.413];

p = 27;

for i = 1:n
	l(i) = 1;
	for j = 1:n
		if(j~=i)
			l(i) = l(i)*(p-x(j))/(x(i)-x(j));
		end
	end
end

sum = 0;
for i = 1:n
	sum = sum + l(i)*f(i);
end
sum

