# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:37:50 2021

@author: boris
"""



#diccionario = {'verde': [1,2,3] , 'quiero': [1], 'rama': [3], "viento":[2,4]}


diccionario = {'verde':[3,[[1,2,[1,5]],[2,1,[1]],[3,1,[1]]]],
                'frota':[1,[[4,1,[3]]]],
                'higuera':[1,[[4,1,[2]]]],
                'quiero':[1,[[1,1,[4]]]],
                'rama':[1,[[3,1,[2]]]],
                'viento':[2,[[2,1,[2]],[4,1,[5]]]]}



def recuperarlista(t1, diccionario):
    a = diccionario[t1]
    b = a[1]
    lista_aux = []
    lista_doc = []
    for i in range(len(b)):
        lista_aux = b[i]
        lista_doc.append(lista_aux[0])
        lista_aux = []
    return lista_doc


def interseccion(t1, t2, diccionario):
    respuesta = []
    l1 = recuperarlista(t1, diccionario)
    l2 = recuperarlista(t2, diccionario)
    p1 = 0
    p2 = 0
    if p1 is not None and p2 is not None:
        
        while p1<len(l1) and p2 <len(l2):
            if (l1[p1] == l2[p2]):
                respuesta.append(l1[p1])
                p1 = p1 +1
                p2 = p2 +1
            else:
                if (l1[p1] < l2[p2]):
                    p1 = p1 + 1
                else:
                    p2 = p2 + 1
    
    return respuesta





def union(t1, t2, diccionario):
    respuesta = []
    l1 = recuperarlista(t1, diccionario)
    l2 = recuperarlista(t2, diccionario)
    p1 = 0
    p2 = 0
    while p1 <= len(l1) and  p2 <= len(l2):
        if p1>=len(l1):
          while p2<len(l2):
            respuesta.append(l2[p2])
            p2+=1
          break
        if p2>=len(l2):

          while p1<len(l1):
            respuesta.append(l1[p1])
            p1+=1
          break
        if l1[p1] < l2[p2]:
          respuesta.append(l1[p1])
          p1+=1
        elif l1[p1] == l2[p2]:
          p1+=1
          p2+=1
        else:
          respuesta.append(l2[p2])
          p2+=1

    return respuesta


def notf(t1, t2, diccionario):
    respuesta = []
    l1 = recuperarlista(t1, diccionario)
    l2 = recuperarlista(t2, diccionario)
    p1 = 0
    p2 = 0
    while p1 <= len(l1) and  p2 <= len(l2):
        if p1>=len(l1):
          while p2<len(l2):
            p2+=1
          break
        if p2>=len(l2):

          while p1<len(l1):
            respuesta.append(l1[p1])
            p1+=1
          break
        if l1[p1] < l2[p2]:
          respuesta.append(l1[p1])
          p1+=1
        elif l1[p1] == l2[p2]:
          p1+=1
          p2+=1
        else:
          p2+=1

    return respuesta




print("Provando la interseccion", interseccion("verde", "viento", diccionario))
print("Provando la union", union("verde", "viento", diccionario))
print("Provando la resta", notf("verde", "viento", diccionario))
