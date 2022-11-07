# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
# nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:

# a. de cada una de las maravillas se conoce su nombre, país de ubicación(puede ser más de uno en las naturales) y tipo(natural o arquitectónica)
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales
# e. determinar si algún país tiene más de una maravilla del mismo tipo
# f. deberá utilizar un grafo no dirigido.


from grafo import Grafo

g = Grafo(False)

# MARAVILLAS ARQUITECTONICAS
g.insertar_vertice('chichen itza', datos={'pais': 'mexico', 'tipo': 'arquitectonico'})
g.insertar_vertice('gran muralla', datos={'pais': 'china', 'tipo': 'arquitectonico'})
g.insertar_vertice('ciudad de petra', datos={'pais': 'jordania', 'tipo': 'arquitectonico'})
g.insertar_vertice('coliseo de roma', datos={'pais': 'italia', 'tipo': 'arquitectonico'})
g.insertar_vertice('machu picchu', datos={'pais': 'peru', 'tipo': 'arquitectonico'})
g.insertar_vertice('cristo redentor', datos={'pais': 'brasil', 'tipo': 'arquitectonico'})
g.insertar_vertice('taj mahal', datos={'pais': 'india', 'tipo': 'arquitectonico'})

# MARAVILLAS NATURALES
g.insertar_vertice('cataratas del iguazu', datos={'pais': 'argentina', 'tipo': 'natural'})
g.insertar_vertice('montaña de mesa', datos={'pais': 'sudafrica', 'tipo': 'natural'})
g.insertar_vertice('amazonas', datos={'pais': 'brasil', 'tipo': 'natural'})
g.insertar_vertice('bahia de ha long', datos={'pais': 'vietnam', 'tipo': 'natural'})
g.insertar_vertice('isla jeju', datos={'pais': 'corea del sur', 'tipo': 'natural'})
g.insertar_vertice('rio subterraneo de puerto princesa', datos={'pais': 'filipinas', 'tipo': 'natural'})
g.insertar_vertice('parque nacional de komodo', datos={'pais': 'indonesia', 'tipo': 'natural'})

g.insertar_arista('chichen itza', 'gran muralla', 2000)
g.insertar_arista('chichen itza', 'ciudad de petra', 3000)
g.insertar_arista('chichen itza', 'coliseo de roma', 4000)
g.insertar_arista('chichen itza', 'machu picchu', 1000)
g.insertar_arista('chichen itza', 'cristo redentor', 1200)
g.insertar_arista('chichen itza', 'taj mahal', 2000)
g.insertar_arista('gran muralla', 'ciudad de petra', 1900)
g.insertar_arista('gran muralla', 'coliseo de roma', 700)
g.insertar_arista('gran muralla', 'machu picchu', 4300)
g.insertar_arista('gran muralla', 'cristo redentor', 1500)
g.insertar_arista('gran muralla', 'taj mahal', 1700)
g.insertar_arista('ciudad de petra', 'coliseo de roma', 2000)
g.insertar_arista('ciudad de petra', 'machu picchu', 2100)
g.insertar_arista('ciudad de petra', 'cristo redentor', 950)
g.insertar_arista('ciudad de petra', 'taj mahal', 900)
g.insertar_arista('coliseo de roma', 'machu picchu', 1400)
g.insertar_arista('coliseo de roma', 'cristo redentor', 2400)
g.insertar_arista('coliseo de roma', 'taj mahal', 2100)
g.insertar_arista('machu picchu', 'cristo redentor', 2200)
g.insertar_arista('machu picchu', 'taj mahal', 1100)
g.insertar_arista('cristo redentor', 'taj mahal', 800)

g.insertar_arista('cataratas del iguazu', 'montaña de mesa', 1900)
g.insertar_arista('cataratas del iguazu', 'amazonas', 4000)
g.insertar_arista('cataratas del iguazu', 'bahia de ha long', 4100)
g.insertar_arista('cataratas del iguazu', 'isla jeju', 1350)
g.insertar_arista('cataratas del iguazu', 'parque nacional de komodo', 1550)
g.insertar_arista('cataratas del iguazu', 'rio subterraneo de puerto princesa', 2700)
g.insertar_arista('montaña de mesa', 'amazonas', 2750)
g.insertar_arista('montaña de mesa', 'bahia de ha long', 3150)
g.insertar_arista('montaña de mesa', 'isla jeju', 3000)
g.insertar_arista('montaña de mesa', 'parque nacional de komodo', 5000)
g.insertar_arista('montaña de mesa', 'rio subterraneo de puerto princesa', 3900)
g.insertar_arista('amazonas', 'bahia de ha long', 2000)
g.insertar_arista('amazonas', 'isla jeju', 4700)
g.insertar_arista('amazonas', 'parque nacional de komodo', 4600)
g.insertar_arista('amazonas', 'rio subterraneo de puerto princesa', 900)
g.insertar_arista('bahia de ha long', 'isla jeju', 1000)
g.insertar_arista('bahia de ha long', 'parque nacional de komodo', 2500)
g.insertar_arista('bahia de ha long', 'rio subterraneo de puerto princesa', 1500)
g.insertar_arista('isla jeju', 'parque nacional de komodo', 1200)
g.insertar_arista('isla jeju', 'rio subterraneo de puerto princesa', 3000)
g.insertar_arista('rio subterraneo de puerto princesa', 'parque nacional de komodo', 1600)

# C
# g.barrido_profundidad('amazonas')
# print()

# arbol_natural_min = g.kruskal_tipo()
# arbol_natural_min = arbol_natural_min[0].split('-')

# peso_total = 0

# for nodo in arbol_natural_min:
#     nodo = nodo.split(';')
#     peso_total += int(nodo[2])
#     # print(f'{nodo[0]} - {nodo[1]} - {nodo[2]}')

# print()
# print(f'se necesitan {peso_total}m de cable')
# print()

# D
paises = g.contar_maravillas()

for p in paises:
    if paises[p]['nat'] == True and paises[p]['arq'] == True:
        print(f'Pais que tienen maravillas tipo natural y arquitectónicas: {p}')
print()

# E
paises_tipo_natural, paises_tipo_arquitectura = g.pais_mismo_tipo()

for p in paises_tipo_natural:
    if paises_tipo_natural[p]['mismo_tipo'] == True:
        print(f'Pais que tiene más de una maravilla del mismo tipo (natural): {p}')

for p in paises_tipo_arquitectura:
    if paises_tipo_arquitectura[p]['mismo_tipo'] == True:
        print(f'Pais que tiene más de una maravilla del mismo tipo (arquitectura): {p}')
print()



