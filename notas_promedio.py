"""
Enunciado:
- Pedir al usuario la cantidad de calificaciones a evaluar.
- Inicializar un acumulador para la suma de calificaciones y un contador para el número de calificaciones.
- Iniciar un bucle para ingresar las calificaciones según la cantidad especificada.
- En cada iteración, solicitar la calificación y agregarla a la suma de calificaciones.
- Después del bucle, calcular el promedio dividiendo la suma de calificaciones por la cantidad de calificaciones.
- Determinar si el estudiante aprobó o reprobó comparando el promedio con 60.
- Mostrar el promedio y el resultado (aprobado o reprobado).
"""
# Abrimos un ciclo while para iterar hasta que el usuario ingrese un número entero.
while True:
  veces_a_iterar = input('Ingrese el número de calificaciones a evaluar: ')
  # En caso de que sea un entero, lo convertimos a entero y rompemos el ciclo.
  if veces_a_iterar.isdigit():
    veces_a_iterar = int(veces_a_iterar)
    break
  else:
    # En caso contrario, informamos al usuario que ingrese un número entero.
    print('El número ingresado no es un entero, por favor inténta ingresando un número.')

# Inicializamos una lista de notas vacía.
notas = []

# Luego, con `range` iteramos la cantidad de veces que el usuario ingresó.
for i in range(veces_a_iterar):
  while True:  # Al igual que antes, abrimos un ciclo while para iterar hasta que el usuario ingrese un número entero.
    # Solicitamos la calificación.
    nota = input(f'Ingrese la calificación {i + 1}: ')

    # En caso de que sea un entero, lo convertimos a entero y rompemos el ciclo.
    if nota.isdigit():
      nota = int(nota)
      # Luego, verificamos que esté entre 0 y 100.
      if 0 >= nota <= 100:
        # Si es así, lo agregamos a la lista de notas y rompemos el ciclo.
        notas.append(nota)
        break
      else:
        # En caso contrario, informamos al usuario que ingrese un número entre 0 y 100.
        print('Ingrese un número entre 0 y 100.')
    else:
      # En caso contrario, informamos al usuario que ingrese un número entero.
      print('El número ingresado no es un entero, por favor inténta ingresando un número.')

# Para calcular el promedio, sumamos todas las notas y las dividimos entre la cantidad de notas.
promedio = sum(notas) / len(notas)

# Si el promedio es mayor o igual a 60, el estudiante aprobó, en caso contrario, reprobó.
# Cuando hacemos una interpolación de cadenas, podemos especificar el número de decimales que queremos mostrar.
# con `:.2f` le decimos que muestre 2 decimales, si quisiésemos 5 decimales, sería `:.5f`.
if promedio >= 60:
  print(f'El promedio es {promedio:.2f}. Aprobado.')
else:
  print(f'El promedio es {promedio:.2f}. Reprobado.')
