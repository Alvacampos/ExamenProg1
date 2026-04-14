# ExamenProg1

Examen de Programacion 1 para la UBP

"Evaluación integradora - Programación para Inteligencia Artificial - Primera parte"

**Nombre:** Gonzalo Ramiro Alvarez Campos  
**Legajo:** 192891  
**Fecha de entrega:** 11/04/2026

---

## 1. Estructuras de Control

### a) Condicionales e iteraciones

La estructura condicional if/elif/else es una estructura lineal que se evalúa una sola vez en tiempo de ejecución, donde se usa el concepto de bifurcación, se toma el camino A o el camino B (dependiendo del resultado booleano), se pueden encadenar muchos elif de ser necesario aunque no está bien visto hacer bloques enteros de elif.

Las estructuras while/for son de bucle o sea que se van a repetir X cantidades de veces, hasta infinito (error común para los mas juniors), una vez que la condición se cumple el bucle termina. Todos en su nucleo hacen una evaluación booleana, eso significa que realmente chequean si es True o False.

Ejemplo sencillo de condicional:

```python
age = 17
if age >= 18:
    print('user can buy alcohol')
else:
    print('user cannot by alcohol, he/she is underage')
```

for/while:

```python
budget = 10
while budget > 0:
    print('user is able to buy things')
    budget -= 1
print('user is under budget, cant keep buying')
```

### b) Diferencia entre while y for

La diferencia entre while y for es que el for si o si va correr al menos una vez (siempre y cuando su arreglo no tenga una longitud de 0), y el while puede que nunca corra. Dependiendo la situación puede convenir uno u el otro, por ej el for lo debemos usar cuando tenemos en claro la "cantidad de vueltas" que vamos a dar y el mientras no sabemos cuantas vueltas puede llegar a dar.

Ejemplo FOR:

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

Aquí sabemos que el array tiene una longitud específica, y el print se va mostrar 5 veces.

Ejemplo WHILE:

```python
i = 1
while i < 5:
    print(i)
    i += 1
```

Aqui i se va imprimir 5 veces pero si cambiamos el condicional para que sea i<1 el print jamás se ejecutaría. O si por X motivo en vez de sumar 1 en cada vuelta sumamos un número random el bucle puede terminar después de una vuelta, o después de Y vueltas.

---

## 2. Funciones

Las funciones son bloques de codigo independiente que pueden ser llamados X cantidad de veces a lo largo del codigo. Son una herramienta vital en programación ya que permite al programador crear herramientas (utils) que puede utilizar a lo largo de su codigo sin repetir dicho codigo, lo centraliza en una funcion (idealmente una función semánticamente sensata, que realice una operación especifica, donde tenga un punto de entrada y uno de salida, donde su comportamiento sea previsible, etc). Nos permiten implementar varios principios como KISS, DRY, SOLID, etc.

Los parámetros son variables que recibe la función para trabajar con distintos valores, permiten que dicha función sea versátil y no estática. Por ejemplo, yo creo una funcion mensaje que al ingresar parámetros como name y date, me permiten dar distintos mensajes acorde a mis necesidades y cada mensaje puede tener X retorno.

Ejemplo:

```python
def ExamStatus(name, date, status):
    print('Alumno {name}, {status} la materia, el dia {date}')
```

Ejemplo usando return:

```python
def Addition(a, b):
    return a + b
```

Estos son ejemplos extremadamente sencillos, realistamente las funciones pueden llegar a ser mucho más complejas, y puede llegar a tal punto donde dicha función sea mejor partirla en funciones más pequeñas para que sea más entendible para los programadores y sea mucho más escalable.

---

## 3. Estructuras de Datos

Dichas estructuras de datos son otra herramienta del programador, que nos permite organizar datos acorde a nuestras necesidades. En la vida real es extremadamente común tener datos complejos, por ejemplo usuarios de una fintech, donde tenes datos de edad, nombre, dirección, uuid, saldo bancario, prestamos, tarjetas de crédito, imagenes de tarjetas, compañias asociadas a dichas tarjetas, etc. Listas, tuplas, diccionarios y conjuntos nos permiten organizar todos estos datos acorde a nuestras necesidades, y dependiendo como los organicemos van a ser las herramientas que tengamos a disposición para "trabajar" dichos datos.

**Almacenar información de un estudiante con nombre, legajo y promedio.** Para esto podriamos usar objetos (diccionario/datasets) ya que no tenemos un solo tipo de dato (string, number, bool) y además seguramente tengamos varios estudiantes.

```python
{
    "name": 'Gonzalo',
    "lastname": 'Alvarez',
    "ledger": 192891,
    "grade": 10
},
{
    "name": 'John',
    "lastname": 'Smith',
    "ledger": 111111,
    "grade": 6
}
```

**Guardar una colección de IDs únicos sin duplicados ni orden específico.** Aqui podriamos usar conjuntos (sets), ya que son unicos pero su orden no importa.

```python
studentsId = {11111, 11112, 11113}
```

**Mantener una secuencia ordenada de calificaciones que se pueda modificar.** Aqui podemos usar listas (list) ya que necesitamos que los datos tengan un orden pero a la vez que puedan repetirse (el alumno puede obtener la misma nota en dos evaluaciones distintas).

```python
grades = [6, 4, 10, 10]
```

---

## 4. LIFO y FIFO

Los conceptos de LIFO y FIFO provienen de las estructuras de datos, donde podemos tener dos comportamientos claros LIFO (last in, first out) donde el último en entrar es el primero en salir y FIFO (first in, first out) donde el primero en entrar es el primero en salir. Esto permite un comportamiento previsible a la hora de manejar datasets (listas ordenadas, donde sí nos importa el orden). Se consideran opuestos en comportamiento y cada uno sirve para distintos casos.

Ejemplo: Tenemos que llenar una heladera, si llenamos dicha heladera con elementos acorde a su fecha de vencimiento, el último elemento en ser guardado va ser el que mayor plazo de vencimiento tenga.

- Si seguimos **LIFO**, el elemento que vamos a sacar primero va ser el que mayor margen de vencimiento tenía, y vamos a dejar en la heladera elementos que van a vencer antes (poco eficiente).
- Si seguimos **FIFO**, el elemento que vamos a sacar primero va ser el primero elemento que guardamos o sea el que tiene menor tiempo antes del vencimiento. Asi la comida nos va a durar más.

Un razonamiento similar puede usarse con los datos en programación, donde nos importa el orden de los datos tanto en la entrada como en la salida. Estos conceptos no solo nos sirven para leer datos, si no tambien para manipularlos y ordenarlos (métodos de ordenamiento como bubble sort y quick sort utilizan estos principios).

```python
array = []
array.append(1)  # agrega
array.pop(0)     # saca
```
