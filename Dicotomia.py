#Primera parte: Definimos la fundicón dicotomía que se encarga de  tabla[indice_min(tabla)]<= t <= tabla[indice_max(tabla)]
from re import M, T
from signal import siginterrupt
from tkinter import _EntryValidateCommand, Variable
from xml.sax.handler import EntityResolver

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

realizacion
    Resultado <- dicotomia_recursiva(tabla,t)

postcondicion 
    Resultado = AUSENTE => ((∀k ∈ Z) (indice_valido(tabla,k)=> tabla[k] ≠t))
    Resultado ≠ AUSENTE => ((indice_valido(tabla,Resultado)=> tabla[Resultado] =t))

fin dicotomia

#Parte 2: Definimos la función dicotomia_recursiva que realizará una búsqueda efectiva si en la función dicotomia Resultado ≠ AUSENTE
Algoritmo dicotomia_recursiva:
    #Indice de "t" en tabla o AUSENTE
entrada
    tabla:TABLA[T -> COMPARABLE] #Objetivo de búsqueda
    t: T  #lo que buscamos 
Resultado: ENTERO #Número de celda que contiene "t" o AUSENTE

variable 
    i: ENTERO 
    j:·ENTERO 
    m:ENTERO 
 
inicializacion
    i <- indice_min(tabla)
    j <- indice_max(tabla)

realizacion
    si 
        i>j 
    entonces 
        Resultado <- AUSENTE 
    si no si 
        m <- (i+j)/2
        si 
            tabla[m]= t 
        entonces
            resultado <- m 
        si no si 
            tabla [m] < t 
        entonces 
            # t no pertenece tabla[i...m-1] => tabla[m+1]<=t<=tabla[j]
            Resultado <- dictomia_recursiva
        si no 
            # no pertenece a tabla[m+1...j]=> tabla[i]<= t <= tabla[m-1]
            Resultado <- dicotomia_recursiva 
                                (sub_tabla(tabla,i,m-1),t)
        fin si
    fin si 
fin dicotomia_recursiva 







