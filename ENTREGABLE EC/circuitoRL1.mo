model circuitoRL1

Real L = 0.004;
Real A = 14;
Real R = 500;
Real w = 125000;
Real vout(start = 0);


equation

der(vout)*L + R*vout = L*A*w*Modelica.Math.cos(time*w);



end circuitoRL1;
