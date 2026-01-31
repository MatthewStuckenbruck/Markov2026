n = 1e6;

function res = f(x)
    res = x*exp(-x);
end

function res = g(x)
    res = 1/2*exp(-x/2);
end

%u = %rand(1,n);
%x = -2*ln(rand(1,n));

c = 4*exp(-1);

xlist = zeros(1,n);

tic
counter = 1;
while counter <= n
    u = rand;
    x = -2*log(rand);
    if u <= f(x)/(c*g(x))
        xlist(counter) = x;
        counter = counter + 1;
    end
end
toc

%Sanity check
m = mean(xlist)
v = var(xlist)
