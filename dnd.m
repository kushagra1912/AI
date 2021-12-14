x = [1 1.5 2 2.5];
f = [2.7183 4.4817 7.3891 12.1825];
g= @(x) exp(x);
p = 2.25;
n = 4;

for 1 = 1:n
	for j = 1:n
		F(i,j) = (F(i-1,j)-F(i-1,j-1))/x(j)-x(j-i+1);
	end
end
for i = 2:n
	prod(1) = 1;
	for j = 1:i-1
		prod(i)=prod(i)*(p-x(j));
	end
end
sum = 0;
for i = 1:n
	sum = sum + prod(i)*F(i,i);
end
sum