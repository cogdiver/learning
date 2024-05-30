% Variables
x = [1 2 3 4];
y = [1 2 3 4];
x + y
x * 10

isvarname time
isvarname time-1

% Uso de nombre reservados
sin(180) %  -0.8012
sin=4;
which sin
sin
% sin(0)
clear sin
which sin

% Operaciones +-*/^
1 + 2
1 - 2
1 * 2
1 / 2
2 ^ 3
pi

x=9;
a=1;
b=3;
c=5;

poly = a*x^2 + b*x + c;
denom = 4*pi*x^2 + cos(x - 2)*poly;
f = (log(poly) - sin(poly)) / denom;
f

% Matrices
y = [1;2;3;4];
z = [1 2 3 4];
y * z

c = 1:3:10;
c

0.000000000000000000000000000005
5000000000000000000000000000000
0.5
save exercises/results/cap2 c
save exercises/results/cap2.dat y -ascii