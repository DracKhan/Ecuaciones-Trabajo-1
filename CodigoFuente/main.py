# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 15:32:06 2025

@author: andre
"""

from funciones_edo import *

def menu():
    while True:
        print("\nMenú:")
        print("1. Graficar mapa de pendientes")
        print("2. Mostrar solución general y particular con SymPy")
        print("3. Graficar solución particular")
        print("4. Graficar mapa de pendientes con 4 soluciones de la familia")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            mapa_pendientes()
        elif opcion == "2":
            soluciones_simplicas()
        elif opcion == "3":
            graficar_solucion_particular()
        elif opcion == "4":
            mapa_con_familia_soluciones()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
