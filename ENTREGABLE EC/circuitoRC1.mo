model circuitoRC1

Real R = 500;
Real C = 0.0005;
Real w = 4;
Real A = 14;
Real vout(start = 0);


equation

der(vout)*R*C + vout = A*Modelica.Math.sin(time*w);


end circuitoRC1;
