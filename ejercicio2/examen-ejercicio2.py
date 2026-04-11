import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler


# ── CLASSES ────────────────────────────────────────────────────────────────────

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock
        self.sales = []

    @property
    def stock(self):
        return self.__stock

    def sell(self, quantity, date=None):
        if quantity > self.__stock:
            print(f'  Error: stock insuficiente (disponible: {self.__stock})')
            return False
        self.__stock -= quantity
        self.sales.append({
            'date': date or datetime.now(),
            'quantity': quantity,
            'price': self.price
        })
        return True

    def __str__(self):
        total = sum(v['quantity'] for v in self.sales)
        return f'{self.name} | Precio: ${self.price} | Stock: {self.__stock} | Ventas totales: {total}'


class Inventory:
    def __init__(self):
        self.products = {}   # name -> Product

    def add_product(self, name, price, stock):
        if name in self.products:
            print('  El producto ya existe.')
            return
        self.products[name] = Product(name, price, stock)
        print(f"  Producto '{name}' registrado.")

    def register_sale(self, name, quantity, date=None):
        if name not in self.products:
            print('  Producto no encontrado.')
            return
        if self.products[name].sell(quantity, date):
            print(f"  Venta registrada: {quantity} unidades de '{name}'.")

    def get_dataframe(self):
        """Construye un DataFrame con todo el historial de ventas."""
        records = []
        for p in self.products.values():
            for s in p.sales:
                records.append({
                    'product': p.name,
                    'date': pd.to_datetime(s['date']),
                    'quantity': s['quantity'],
                    'price': s['price'],
                    'income': s['quantity'] * s['price']
                })
        return pd.DataFrame(records)

    def analyze(self):
        df = self.get_dataframe()
        if df.empty:
            print('  Sin datos de ventas para analizar.')
            return
        print('\n--- Resumen por producto ---')
        summary = df.groupby('product').agg(
            unidades_vendidas=('quantity', 'sum'),
            ingresos_totales=('income', 'sum'),
            promedio_por_venta=('quantity', 'mean')
        ).round(2)
        print(summary.to_string())
        print(f"\n  Producto más vendido: {df.groupby('product')['quantity'].sum().idxmax()}")
        print(f"  Ingreso total: ${df['income'].sum():,.2f}")


class Predictor:
    def __init__(self):
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.trained = False
        self.metrics = {}

    def train(self, df):
        if df.empty or len(df) < 4:
            print('  Se necesitan más datos para entrenar.')
            return

        df = df.copy()
        df['month'] = df['date'].dt.month
        df['week'] = df['date'].dt.isocalendar().week.astype(int)

        X = df[['month', 'week', 'price']].values
        y = df['quantity'].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)

        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)

        self.metrics = {
            'MAE': round(mean_absolute_error(y_test, y_pred), 2),
            'R2': round(r2_score(y_test, y_pred), 4),
            'muestras_entrenamiento': len(X_train),
            'muestras_prueba': len(X_test)
        }
        self.trained = True
        print('  Modelo entrenado exitosamente.')
        self.show_metrics()

    def predict(self, month, week, price):
        if not self.trained:
            print('  Primero entrene el modelo (opción 4).')
            return None
        X = self.scaler.transform([[month, week, price]])
        return max(0, round(self.model.predict(X)[0], 1))

    def show_metrics(self):
        if not self.trained:
            print('  No hay modelo entrenado.')
            return
        print('\n  Modelo: Regresión Lineal')
        for k, v in self.metrics.items():
            print(f'  {k}: {v}')


# ── UTILS FUNCTIONS ──────────────────────────────────────────────────────

def print_line_break():
    print('\n' + '=' * 45 + '\n')

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('  Por favor ingrese un número entero válido.')

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('  Por favor ingrese un número válido.')


# ── MAIN MENU ────────────────────────────────────────────────────────────

print('Bienvenido al sistema de gestión de inventario con predicción de ventas\n')
inventory = Inventory()
predictor = Predictor()
runProgram = True

while runProgram:
    print_line_break()
    print('1. Registrar nuevo producto.')
    print('2. Registrar venta de un producto.')
    print('3. Analizar datos históricos.')
    print('4. Entrenar modelo de machine learning.')
    print('5. Predecir ventas futuras.')
    print('6. Ver stock recomendado y ganancias estimadas.')
    print('7. Ver métricas del modelo.')
    print('8. Salir.')

    option = input('\n  Seleccione una opción: ').strip()

    match option:
        case '1':
            print_line_break()
            name  = input('  Nombre del producto: ').strip()
            price = input_float('  Precio: $')
            stock = input_int('  Stock inicial: ')
            inventory.add_product(name, price, stock)

        case '2':
            print_line_break()
            name     = input('  Nombre del producto: ').strip()
            quantity = input_int('  Cantidad vendida: ')
            inventory.register_sale(name, quantity)

        case '3':
            print_line_break()
            inventory.analyze()

        case '4':
            print_line_break()
            df = inventory.get_dataframe()
            predictor.train(df)

        case '5':
            print_line_break()
            if not predictor.trained:
                print('  Entrene el modelo primero (opción 4).')
            else:
                name = input('  Nombre del producto: ').strip()
                if name not in inventory.products:
                    print('  Producto no encontrado.')
                else:
                    month  = input_int('  Mes a predecir (1-12): ')
                    week   = input_int('  Semana del año (1-52): ')
                    price  = inventory.products[name].price
                    result = predictor.predict(month, week, price)
                    print(f'\n  Predicción de ventas: {result} unidades')
                    print(f'  Ingreso estimado: ${result * price:,.2f}')

        case '6':
            print_line_break()
            if not predictor.trained:
                print('  Entrene el modelo primero (opción 4).')
            else:
                month = input_int('  Mes a planificar (1-12): ')
                week  = input_int('  Semana del año (1-52): ')
                print(f"\n  {'Producto':<15} {'Pred. ventas':>13} {'Stock rec.':>11} {'Ganancia est.':>14}")
                print('  ' + '-' * 55)
                for name, p in inventory.products.items():
                    sales_pred = predictor.predict(month, week, p.price)
                    if sales_pred is None:
                        continue
                    recommended_stock = int(sales_pred * 1.2)   # 20% de margen de seguridad
                    estimated_profit  = sales_pred * p.price
                    print(f'  {p.name:<15} {sales_pred:>13} {recommended_stock:>11} ${estimated_profit:>13,.2f}')

        case '7':
            print_line_break()
            predictor.show_metrics()

        case '8':
            print_line_break()
            print('  Saliendo del programa...')
            runProgram = False

        case _:
            print('  Opción no válida, por favor intente nuevamente.')