# ExamenProg1

Examen de Programacion 1 para la UBP

"Evaluación integradora - Programación para Inteligencia Artificial - Segunda parte"

**Nombre:** Gonzalo Ramiro Alvarez Campos  
**Legajo:** 192891  
**Fecha de entrega:** 11/04/2026

---

## 1. Programación Orientada a Objetos

### a) Clases y Objetos

"Una clase es una plantilla, el modelo a seguir, es la fábrica de autos y el objeto es el auto que se crea a partir de esa plantilla". Creo que es la definición más simple y más usada para entender clases y objetos en programación.
Algo un poco mas formal seria, un objeto es una instancia creada de una clase.

```python
# Clase constructora
class Car: 
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def message(self):
        print("Auto {self.brand}, {model} con precio ${price} acaba de ser ensamblado")

# Instanciacion del objeto
car1 = Car('Toyota', 'Corolla', 10000)
car1.message()
```

### b) Encapsulamiento

Encapsulamiento es una práctica común y una medida de seguridad en muchos lenguajes de programación, no todos los lenguajes de programación tienen variables protegidas o privadas así que los métodos de encapsulamiento pueden variar levemente. Su objetivo es proteger estados sensibles de datos para evitar manipulaciones indebidas, por ej si no se encapsulara el dato de saldo de tarjeta podria ser posible modificarlo (un ejemplo extremo y muy simplificado).

Muchos lenguajes, incluido Python, tienen modificadores que le dan la propiedad de "privado" a una variable lo cual imposibilita su uso por fuera del block scope donde fue creada, en este caso en su clase constructora, se crean getters y setters para poder acceder a la variable de una forma segura.

```python
# Clase constructora
class Car: 
    # Constructor
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self._price = price  # este atributo ahora esta privado

    # Metodo
    def message(self):
        print("Auto {self.brand}, {model} con precio ${price} acaba de ser ensamblado")

    # Setter
    def set_price(self, value):
        # aqui podemos tener validaciones y otras herramientas utiles
        self._price = value

    # Getter
    def get_price(self):
        return self._price

# Instanciación del objeto
car1 = Car('Toyota', 'Corolla', 10000)
car1.set_price(100000)  # uso el setter para darle un nuevo valor
print(car1.get_price())
```

### c) Herencia

La herencia permite la reutilización y extensión de una clase padre a clases hijas que tal vez necesiten las propiedades del padre además de las suyas propias. Herencia nos permite crear una clase padre con X, Y, Z atributos y metodos, y despues de ser necesario podemos crear una clase hija con A y B atributos y metodos que pueden heredar lo necesario (X, Y, Z) del padre. Esto evita duplicar codigo y minimizar la complejidad (KISS, DRY).

```python
class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def hi(self):
        print("Hola, me llamo {name}")

class Employee(Person):
    def __init__(self, name, sex, ledger):
        super().__init__(name, sex)
        self.ledger = ledger

employee1 = Employee('Juan', 'male', 1)  # Aqui tengo las capacidades de ambas clases
```

---

## 2. Grafos

### a) Definición

Un grafo es una estructura que relaciona entidades, tiene vértices y aristas. Puede ser dirigido (cada arista tiene una dirección) y no dirigido (las aristas son bidireccionales).

### b) Grafo de la red social

| Nodo    | Arista            |
|---------|-------------------|
| Ana     | Carlos, Beatriz   |
| Carlos  | Diego             |
| Beatriz | Diego, Elena      |
| Diego   | Ana               |
| Elena   | -                 |

Es un grafo dirigido, ya que "X sigue a Y" es una relación asimétrica. Beatriz sigue a Diego pero Diego no sigue a Beatriz.

### c) Implementación en clases

Necesitariamos dos clases: `Usuario` y `RedSocial`.

- **Usuario:** atributos `name` y `follows`. Métodos `follow` y `get_followers`, esto nos posibilita seguir a alguien y saber a quien esa persona sigue.
- **RedSocial:** métodos `add_user`, `register_follow`, `recommend`, `show_graph`.

---

## 3. Regresión y Machine Learning

### a) Regresión vs Clasificación

Es un conjunto de técnicas para predecir el valor numero continuo a partir de variables de entrada. Y la clasificación predice a partir de una categoría o etiqueta discreta.

Ejemplo: predecir la cantidad de autos vendidos para el próximo mes basándose en el historial de ventas, el mes del año y el precio. Aqui la salida, autos vendidos, es un número continuo (regresión).

### b) Normalización de datos

Normalizar es transformar las variables numericas para que tengan una escala comparable. Es util porque los algoritmos como regresion lineal y redes neuronales se ven afectadas por la magnitud de las variables, esto evita que grandes valores dominen a los valores mas chicos.

### c) Train / Test Split

Dividir los datos en conjuntos de entrenamiento y conjuntos de prueba permite evaluar si el modelo generaliza a nuevos datos o si solo memoriza los datos del entrenamiento y da metricas buenas pero erroneas.
