# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.


from grafo import Grafo

g = Grafo(False)

#cargar grafo

g.insertar_vertice('cocina')
g.insertar_vertice('comedor')
g.insertar_vertice('cochera')
g.insertar_vertice('quincho')
g.insertar_vertice('baño1')
g.insertar_vertice('baño2')
g.insertar_vertice('habitacion1')
g.insertar_vertice('habitacion2')
g.insertar_vertice('salaestar')
g.insertar_vertice('terraza')
g.insertar_vertice('patio')

g.insertar_arista('cocina', 'comedor', 1)
g.insertar_arista('cocina', 'cochera', 10)
g.insertar_arista('cocina', 'quincho', 12)
g.insertar_arista('cocina', 'baño1', 4)
g.insertar_arista('cocina', 'baño2', 5)
g.insertar_arista('comedor', 'baño1', 4)
g.insertar_arista('comedor', 'terraza', 7)
g.insertar_arista('cochera', 'baño1', 8)
g.insertar_arista('cochera', 'baño2', 9)
g.insertar_arista('cochera', 'habitacion1', 7)
g.insertar_arista('cochera', 'habitacion2', 8)
g.insertar_arista('quincho', 'habitacion1', 11)
g.insertar_arista('quincho', 'habitacion2', 12)
g.insertar_arista('habitacion1', 'salaestar', 5)
g.insertar_arista('habitacion2', 'salaestar', 6)
g.insertar_arista('terraza', 'salaestar', 13)
g.insertar_arista('terraza', 'patio', 5)
g.insertar_arista('baño2', 'patio', 8)
g.insertar_arista('patio', 'habitacion2', 7)

# C
arbol_min = g.kruskal()

arbol_min = arbol_min[0].split('-')
peso_total = 0

for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    # print(f'{nodo[0]} - {nodo[1]} - {nodo[2]}')

print()
print( f'se necesitan {peso_total}m de cable')
print()


# D
if g.existe_paso('habitacion1', 'salaestar'):
    resultado = g.dijkstra('habitacion1')
    cam = g.camino(resultado, 'habitacion1', 'salaestar')
    print()
    print('camino mas corto: ', cam['camino'])
    print('se necesitan', cam['costo'], 'm de cable de red se necesitan para conectar el router con el Smart Tv')
else:
    print('no existe camino entre habitacion1 y salaestar')
print()

































