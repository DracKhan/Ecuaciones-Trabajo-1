# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 21:58:51 2025

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def mapa_pendientes():
    x = np.linspace(-15, 15, 25)
    y = np.linspace(-15, 15, 25)
    X, Y = np.meshgrid(x, y)

    derivada = (1 / 7) * (5 / Y - 2 * Y)
    deltax = 1
    deltay = derivada
    magnitud = np.sqrt(deltax**2 + deltay**2)
    deltax /= magnitud
    deltay /= magnitud

    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, deltax, deltay, color='blue')
    plt.title("Mapa de pendientes de $2y + 7\\frac{dy}{dx} = \\frac{5}{y}$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()


def soluciones_simplicas():
    x = sp.Symbol("x")
    y = sp.Function("y")
    edo = sp.Eq(2*y(x) + 7*y(x).diff(x), 5 / y(x))

    print("Ecuación diferencial:")
    sp.pprint(edo)

    sol_general = sp.dsolve(edo, y(x))
    print("\nSolución general:")
    sp.pprint(sol_general)

    condicion_inicial = {y(0): 14}
    sol_particular = sp.dsolve(edo, y(x), ics=condicion_inicial)
    print("\nSolución particular (con y(0)=14):")
    sp.pprint(sol_particular)


def graficar_solucion_particular():
    x = sp.Symbol("x")
    y = sp.Function("y")
    edo = sp.Eq(2*y(x) + 7*y(x).diff(x), 5 / y(x))
    sol_particular = sp.dsolve(edo, y(x), ics={y(0): 14})
    
    f = sp.lambdify(x, sol_particular.rhs, modules='numpy')
    x_vals = np.linspace(-0.5, 15, 400)
    y_vals = f(x_vals)
    
    x0 = 0
    y0 = f(x0)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='Solución particular', color='green')
    plt.plot(x0, y0, 'ro')  
    plt.annotate(f'y(0) = {y0:.2f}', xy=(x0, y0), xytext=(x0 + 0.5, y0),
                 arrowprops=dict(arrowstyle='->', color='red'), color='red')
    
    plt.title("Solución particular de la EDO")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

def mapa_con_familia_soluciones():
    x = sp.Symbol("x")
    y = sp.Function("y")
    edo = sp.Eq(2*y(x) + 7*y(x).diff(x), 5 / y(x))
    
    sol = sp.dsolve(edo, y(x))
    if isinstance(sol, list):
        sol = sol[0]
    sol_general = sol  
    
    C = sp.Symbol("C1")
    soluciones = []
    
    for c_val in [1, 5, 10, 20]:
        expr = -sol_general.rhs.subs(C, c_val)  # negamos para rama positiva
        f = sp.lambdify(x, expr, "numpy")
        soluciones.append((f, f"Solución C={c_val}"))
    
    for c_val in [1, 5, 10, 20]:
        expr = sol_general.rhs.subs(C, c_val)
        f = sp.lambdify(x, expr, "numpy")
        soluciones.append((f, f"Solución C={c_val}"))
    
    # Mapa de pendientes
    x_vals = np.linspace(-10, 6, 25)
    y_vals = np.linspace(-60, 60, 25)
    X, Y = np.meshgrid(x_vals, y_vals)
    derivada = (1/7)*(5/Y - 2*Y)
    deltax = 1
    deltay = derivada
    magnitud = np.sqrt(deltax**2 + deltay**2)
    deltax /= magnitud
    deltay /= magnitud
    
    plt.figure(figsize=(8, 6))
    plt.quiver(X, Y, deltax, deltay, color='gray', alpha=0.5)
    
    # Graficar cada solución
    x_range = np.linspace(-10, 6, 400)
    for f, label in soluciones:
        try:
            y_range = f(x_range)
            plt.plot(x_range, y_range, label=label)
        except Exception as e:
            print(f"Error graficando {label}: {e}")
            continue
    
    plt.title("Mapa de pendientes con familia de soluciones")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
