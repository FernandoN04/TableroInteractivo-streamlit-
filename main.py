import streamlit as st
import funciones.funcion as fs
#este codigo se encarga de inicializar una lista en streamlit
if 'lista' not in st.session_state:
    st.session_state.lista = []

if 'listapi' not in st.session_state:
    st.session_state.listapi = []

if 'listam' not in st.session_state:
    st.session_state.listam = []

menu_opciones = ["Inicio", "Suma", "Area de triangulo", "Calculadora de descuento","Suma de una lista", "Productos","Numeros pares e impares","Multiplicacion","Informacion de una persona","Calculadora","Acerca de"]
selected_option = st.sidebar.selectbox("Opciones", menu_opciones)

match selected_option:
    case "Inicio":
        st.title("Bienvenida")
        nombre = st.text_input("Escriba su nombre")
        if st.button("Aceptar"):
            fs.saludar(nombre)

    case "Suma":
        st.title("Suma sencilla")
        n1 = st.number_input("Ingrese un numero")
        n2 = st.number_input("Ingrese otro numero")
        if st.button("Aceptar"):
            fs.sumar(n1,n2)

    case "Area de triangulo":
        st.title("Area de triangulo")
        b = st.number_input("Ingrese la base del triangulo")
        a = st.number_input("Ingrese la altura")
        if st.button("Aceptar"):
         fs.calcular_area_triangulo(b,a)

    case "Calculadora de descuento":
        st.title("Calculadora de descuento")
        precioB = st.number_input("Ingrese el precio del producto")
        descuento = st.number_input("Ingrese el descuento")
        if st.button("Aceptar"):
            fs.calcular_precio_final(precioB,descuento)

    case "Suma de una lista":
        st.title("Sumatoria")
        n = st.number_input("Ingrese un numero a la lista")
        if st.button("Agregar"):
            st.session_state.lista.append(n)
            st.success("Numero agregado a la lista")
        if st.button("Sumar"):
            fs.sumar_lista(st.session_state.lista)
        if st.button("Limpiar lista"):
            st.session_state.lista = []
            st.success("La lista ha sido limpiada.")

    case "Productos":
        st.title("Productos")
        nombre = st.text_input("Ingrese el nombre del producto")
        cantidad = st.slider("Cantidad",0,500)
        precio_uni = st.number_input("Ingrese el precio por unidad")
        if st.button("Calcular"):
            fs.producto(nombre,cantidad,precio_uni)

    case "Numeros pares e impares":
        st.title("Numeros pares e impares")
        npi = st.number_input("Ingrese un numero a la lista")
        if st.button("Agregar"):
            st.session_state.listapi.append(npi)
            st.success("Numero agregado a la lista")
        if st.button("Mostrar"):
            fs.numeros_pares_e_impares(st.session_state.listapi)
        if st.button("Limpiar lista"):
            st.session_state.listapi = []
            st.success("La lista ha sido limpiada.")

    case "Multiplicacion":
        st.title("Multiplicaciones")
        ns = st.number_input("Ingrese un numero")
        if st.button("Agregar"):
            st.session_state.listam.append(ns)
        if st.button("Limpiar"):
          st.session_state.listam = []
          st.success("La lista ha sido limpiada.")
        if st.button("Multiplicar"):
            fs.multiplicar_todos(st.session_state.listam)

    case "Informacion de una persona":
        st.title("Informacion personal")
        datos_personales = {}
        cantidad_datos = st.number_input("Ingrese la cantidad de datos",1,50,1)
        for i in range(1,cantidad_datos+1):
            claves = st.text_input(f"Ingrese la clave numero {i}")
            valor = st.text_input(f"Ingrese el valor numero {i}")
            if claves and valor:
                datos_personales[claves] = valor

        if st.button("Mostrar"):
            fs.informacio_personal(**datos_personales)

    case "Calculadora":
            st.title("Calculadora Sencilla")
            n1 = st.number_input("Ingrese un numero")
            n2 = st.number_input("Ingrese otro nunmero")

            operacion = st.radio(
        "Seleccione la opcion para realizar la operacion",
        ["Suma", "Resta", "Multiplicacion","Division"])
            if st.button("Realizar operacion"):
                fs.calculadora_flexible(n1,n2,operacion)

    case "Acerca de":
        st.title("Creado por: Sanchez Montes De Oca Fernando Nicolas")
        st.write("Ingenieria en Computacion Inteligente")
        st.write("Universidad de Colima")
        st.write("Programacion funcional")