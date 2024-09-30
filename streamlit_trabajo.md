## Explicación del código: tablero interactivo usando Streamlit en Python

##### En este código, practicamos el desarrollo de una aplicación web sencilla donde el usuario pueda ingresar, en cada sección, datos para resolver algún problema de manera interactiva. En ella, creamos una carpeta donde manejaremos la página y otra para las funciones, y después las importamos para su manejo más práctico.

 
```python
import streamlit as st
import funciones.funcion as fs
```

##### Esta parte del código importamos Streamlit para poder trabajar el desarrollo web y también una librería creada por mí, donde se encuentra lo necesario para resolver los problemas dados.
```python
#este codigo se encarga de inicializar una lista en streamlit
if 'lista' not in st.session_state:
    st.session_state.lista = []

if 'listapi' not in st.session_state:
    st.session_state.listapi = []

if 'listam' not in st.session_state:
    st.session_state.listam = []
```

##### Las listas fueron creadas para evitar problemas con las funciones. Estas listas son útiles cuando queremos almacenar elementos en una lista a lo largo de una sesión de nuestra aplicación de Streamlit.

```python
menu_opciones = ["Inicio", "Suma", "Area de triangulo", "Calculadora de descuento","Suma de una lista", "Productos","Numeros pares e impares","Multiplicacion","Informacion de una persona","Calculadora","Acerca de"]
selected_option = st.sidebar.selectbox("Opciones", menu_opciones)
```

##### Creamos un menú de opciones para cada sección que se trabajará.
```python
match selected_option:
    case "Inicio":
        st.title("Bienvenida")
        nombre = st.text_input("Escriba su nombre")
        if st.button("Aceptar"):
            fs.saludar(nombre)
```

##### Empezamos creando la primera sección llamada “Inicio”, donde se le pide al usuario su nombre y, con el botón, se llama a la función para que la función no se llame antes de tiempo y ella regresa un saludo sencillo.
```python
case "Suma":
       st.title("Suma sencilla")
       n1 = st.number_input("Ingrese un numero")
       n2 = st.number_input("Ingrese otro numero")
       if st.button("Aceptar"):
           fs.sumar(n1,n2)
```

##### La sección “Suma” crea dos inputs de números donde el usuario ingrese dos números y la función los sume, mostrando el resultado, no sin antes presionar el botón que todas las secciones tendrán, ya que, si no, la función se llamará sin condición y tendrá un funcionamiento incorrecto o antes de tiempo, dando resultados vacíos o errores.
```python
case "Area de triangulo":
       st.title("Area de triangulo")
       b = st.number_input("Ingrese la base del triangulo")
       a = st.number_input("Ingrese la altura")
       if st.button("Aceptar"):
        fs.calcular_area_triangulo(b,a)
```

##### Sección “Área de triángulo”: sería lo mismo a lo anterior, dos inputs donde el usuario ingresa y la función se encarga de los cálculos, en este caso, la fórmula del área de un triángulo.
```python
case "Calculadora de descuento":
    st.title("Calculadora de descuento")
    precioB = st.number_input("Ingrese el precio del producto")
    descuento = st.number_input("Ingrese el descuento")
    if st.button("Aceptar"):
        fs.calcular_precio_final(precioB,descuento)
```

##### Sección “Calculadora de descuentos”: el usuario, en los dos inputs, ingresa lo que se pide y lleva 2 argumentos que utilizará la función para calcular los descuentos con impuestos.
```python
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
```

##### Sección de “Suma de una lista”: en esta parte, tuve problemas con las listas, así que tuve que crear una a lo largo de la sesión de Streamlit y así trabajar sin problemas, así que, en ella, crea una lista vacía si es que no existe y, ya que el usuario ingrese un número, presiona el botón para agregar ese número a la lista y calcular la sumatoria con la lista; agregué otro botón para limpiarla por completo, ya que esta lista creada se mantiene en toda la sesión.
```python
case "Productos":
    st.title("Productos")
    nombre = st.text_input("Ingrese el nombre del producto")
    cantidad = st.slider("Cantidad",0,500)
    precio_uni = st.number_input("Ingrese el precio por unidad")
    if st.button("Calcular"):
        fs.producto(nombre,cantidad,precio_uni)
```

##### “Productos”: en esta sección, preguntamos al usuario, en un input, ingresar un nombre del producto, creamos una barra deslizadora para hacerlo más interactivo y probar cosas nuevas, donde el usuario elije la cantidad del producto y otro input para el precio por unidad. El usuario presiona el botón y así llama a la función para hacer su trabajo.

```python
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
```

##### “Números pares e impares”: en este, igual, creamos la lista donde el usuario ingresará número por número, para al final imprimir el resultado de la función, dando asi dos listas: una de impares que dieron un residuo por la división de 2 y otra lista para pares.

```python
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
```


##### “Multiplicación”: en esta, creamos una lista donde el usuario ingresa los números que quiere multiplicar y así darle el resultado llamado por la función.

```python
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
```

##### La sección “Información de una persona”: el fin de esta es crear varios inputs que pida el usuario para ingresar la información que quiera de una persona y en ella almacenarla en un diccionario, en ella creamos un For para crear los inputs, pero los inputs creamos una cadena formateada con la iteración del ciclo For y así no tener problemas con la llave del input, ya que deben ser únicas.
```python
case "Calculadora":
        st.title("Calculadora Sencilla")
        n1 = st.number_input("Ingrese un numero")
        n2 = st.number_input("Ingrese otro nunmero")

        operacion = st.radio(
    "Seleccione la opcion para realizar la operacion",
    ["Suma", "Resta", "Multiplicacion","Division"])
        if st.button("Realizar operacion"):
            fs.calculadora_flexible(n1,n2,operacion)
```

##### “Calculadora”: esta sección es una simple calculadora donde el usuario ingresa dos datos y en ella tendrá un botón de radio para mayor interacción y elegir la opción que quiera, en este caso, la operación que será reconocida en la función donde hay un diccionario con clave del nombre de la opción del botón de radio elegida.

##### Sanchez Montes de Oca Fernando Nicolas 3B