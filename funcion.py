import streamlit as st

def saludar(nombre):
    return st.write(f"Hola, {nombre}.")

def sumar(n1, n2):
    return st.write(f"La suma es: {n1 + n2}")

def calcular_area_triangulo(b,a):
    return st.write(f"El area es: {(b*a)/2}")

def calcular_precio_final(precioB,descuento):
    precioI = precioB * 0.16
    precioF = precioI + (precioB - (precioB * (descuento/100)))
    return st.write(f"El precio final es: {precioF}")

def sumar_lista(lista):
    s = 0
    for i in lista:
        s = s + i
    return st.write(f"La suma total es: {s}")

def producto(nombre_producto,cantidad,precio_uni):
    total = cantidad * precio_uni
    return st.write(f"Total a pagar de {nombre_producto} es: {total}")

def numeros_pares_e_impares(listaPI):
    listaP = []
    listaI = []
    for i in listaPI:
        if i % 2 == 0:
            listaP.append(i)
        else:
            listaI.append(i)
    return st.write(f"Lista de numeros impares: {listaI} \n Lista de numeros pares: {listaP}")

def multiplicar_todos(t):
    resultado = 1
    for numero in t:
        resultado *= numero
    return st.write(f"El total de la multiplicacion es: {resultado}")

def informacio_personal(**kwargs):
    for clave,valor in kwargs.items():
        st.write(f"{clave}:  {valor}")

def calculadora_flexible(n1,n2,op):
    ls = {"Suma":n1+n2,"Resta":n2-n1,"Multiplicacion":n1*n2,"Division":n1/n2}
    return st.write(f"El resultado es: {ls.get(op)}")