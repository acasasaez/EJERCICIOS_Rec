#Primera parte: Definimos la fundicón dicotomía
from re import T
from tkinter import _EntryValidateCommand

from pkg_resources import NullProvider


Algoritmo dicotomia:
    #Indice de "t" en tabla o AUSENTE
entrada 
    tabla[T-> COMPARABLE] #Objetivo de búsuqeda
    t: T  #lo que buscamos 
Resultado: ENTERO #Número de celda que contiene "t" o AUSENTE.

precondicion
    #se han inicializado "t" Y "tabla"
    t ≠ NULO 
    tabla ≠ NULO 
    #"tabla" ordenada en orden creciente 
    #"t" está en el orden de los componentes de "tabla" 
    tabla[indice_min(tabla)]<= t <= tabla[indice_max(tabla)]

