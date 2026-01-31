function res = F(x)
    res = 1-(x+1).*exp(-x);
end

function res = newtoniter(x0,u)
    x = inf;
    res = x0;
    while abs(res-x)>1e-7
        x = res;
        res = x - (1-(x+1).*exp(-x)-u)/(x.*exp(-x));
    end
end

n = 1e6;

tic
u = rand(1,n);
x = zeros(1,n);

for i = 1:n
    x(i) = newtoniter(1,u(i));
end
toc

%Sanity check
m = mean(x)
v = (std(x))^2

%For part (e), plot histogram vs theoretical value

hold on
histogram(x,150,normalization='pdf')
xvals = linspace(0,10);
yvals = xvals.*exp(-xvals);
plot(xvals,yvals)
xlabel('X')
ylabel('Probability density')
title('Histogram of $n=10^6$ samples of $X$ compared with the theoretical distribution', interpreter='latex')
hl = legend('Simulation','f(x)=xe^{-x}');
set(hl,'interpreter','latex')
hold off