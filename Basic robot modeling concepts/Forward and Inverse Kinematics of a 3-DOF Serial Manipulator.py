import sympy as sp

l_1, l_2, l_3 = sp.symbols('l_1 l_2 l_3')
theta_1, theta_2, theta_3 = sp.symbols('theta_1 theta_2 theta_3')

x = l_1 * sp.cos(theta_1) + l_2 * sp.cos(theta_1 + theta_2) + l_3 * sp.cos(theta_1 + theta_2 + theta_3)
y = l_1 * sp.sin(theta_1) + l_2 * sp.sin(theta_1 + theta_2) + l_3 * sp.sin(theta_1 + theta_2 + theta_3)
phi = theta_1 + theta_2 + theta_3

jac = sp.Matrix([[x.diff(theta_1), x.diff(theta_2), x.diff(theta_3)],
                 [y.diff(theta_1), y.diff(theta_2), y.diff(theta_3)],
                 [phi.diff(theta_1), phi.diff(theta_2), phi.diff(theta_3)]])


#sympy pretty print
sp.pprint(jac)