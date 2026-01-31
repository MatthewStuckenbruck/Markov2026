n = 1e6;

tic
x1 = -log(rand(1,n));
x2 = -log(rand(1,n));

x = x1+x2;
toc

%Sanity check
m = mean(x)
v = var(x)