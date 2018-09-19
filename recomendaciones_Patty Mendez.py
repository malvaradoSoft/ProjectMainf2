import numpy as np
import pandas as pd

def datos():
  categorias = np.random.choice(30, 100, replace=True)
  id_peliculas = np.random.choice(1000, 100, replace=False)
  columns = {'categorias': categorias, 'id_peliculas': id_peliculas}
  dt = pd.DataFrame(data=columns)
  return dt

def d_Euclidiana(x1, y1, x2, y2):
  return np.sqrt(((x2-x1)**2) + ((y2-y1)**2))

def d_Manhattan(x1, y1, x2, y2):
  return np.sqrt(np.abs(x1-y1) + np.abs(x2-y2))

def d_Coseno(x1, y1, x2, y2):
  filas = x1.size
  distancias = np.zeros(filas)
  for i in range(filas):
    u = [x1[i], y1[i]]
    v = [x2, y2]
    distancias[i] = np.dot(u, v) / np.math.sqrt(np.dot(u, u) * np.dot(v, v))
  return distancias

def recomendar_euclidiana(dt, x1, y1):
  d = d_Euclidiana(dt['categorias'], dt['id_peliculas'], x1, y1)
  dt_2 = pd.concat([dt.reset_index(drop=True), round(d, 2)], axis=1)
  top5 = dt_2.sort_values(0, ascending=True).head()
  return top5

def recomendar_manhattan(dt, x1, y1):
  d = d_Manhattan(dt['categorias'], dt['id_peliculas'], x1, y1)
  dt_2 = pd.concat([dt.reset_index(drop=True), round(d, 2)], axis=1)
  top5 = dt_2.sort_values(0, ascending=True).head()
  return top5

def recomendar_coseno(dt, x1, y1):
  d = pd.DataFrame({0: d_Coseno(dt['categorias'], dt['id_peliculas'], x1, y1)})
  dt_2 = pd.concat([dt.reset_index(drop=True), round(d, 10)], axis=1)
  top5 = dt_2.sort_values(0, ascending=False).head()
  return top5

x1 = 25
y1 = 500
print('\n')
print('--------- RECOMENDACION DE PELICULAS ---------\n')
print("La película desde la cual se quiere encontrar recomendaciones es: ")
print('Categoría:', x1, ' -  ID: ',  y1)
print('Las películas recomendadas usando la distancia Euclidiana son: ')
print(recomendar_euclidiana(datos(), x1, y1), '\n\n')
print('Las películas recomendadas usando la distancia de Manhattan son: ')
print(recomendar_manhattan(datos(), x1, y1), '\n\n')
print('Las películas recomendadas usando la distancia de Coseno son: ')
print(recomendar_coseno(datos(), x1, y1))
print('\n\n')