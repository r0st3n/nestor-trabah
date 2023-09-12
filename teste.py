vimport sympy as sp

f_expr = input("Digite a expressão para f(x): ")
g_expr = input("Digite a expressão para g(x): ")

f_expr = f_expr.replace("^", "**")
g_expr = g_expr.replace("^", "**")


x = sp.symbols('x')

f_formula = sp.sympify(f_expr)
g_formula = sp.sympify(g_expr)

f = lambda x_val: f_formula.subs(x, x_val)
g = lambda x_val: g_formula.subs(x, x_val)

def compose(g, f):
    return lambda x_val: g(f(x_val))

x_val = float(input("Digite o valor de x: "))

gof = compose(g, f)
gog = compose(g, g)
fof = compose(f, f)
fog = compose(f, g)

result_gof = gof(x_val)
result_gog = gog(x_val)
result_fof = fof(x_val)
result_fog = fog(x_val)

print("(g ° f)(x) =", result_gof)
print("(g ° g)(x) =", result_gog)
print("(f ° f)(x) =", result_fof)
print("(f ° g)(x) =", result_fog