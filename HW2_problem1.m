clear all
close all

x0 = 10;
gamma = 4;

for N = [100 1000 10000]

    w = rand(1,N);

    x = x0.*w.^(1/(-gamma+1));

    hold on
    histogram(x,'DisplayName', 'Simulation', normalization='pdf')

    xvals = linspace(x0,120,400);
    yvals = (gamma-1)/x0.*(xvals/x0).^(-gamma);
    plot(xvals,yvals,)
    title(sprintf('Normalized histogram of simulation vs pdf for N=%d', N))
    xlabel('x')
    ylabel('probability density')
    hl = legend('Simulation', '$f(x)=\frac{\gamma-1}{x_0}\left(\frac{x}{x_0}\right)^{-\gamma}$');
    set('hl','interpreter','latex')
    hold off
    drawnow
    uiwait
    cla
end