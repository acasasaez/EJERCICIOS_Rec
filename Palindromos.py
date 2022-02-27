#Ejercicio Palíndromos 
#Primera Parte: Filtración
from signal import siginterrupt
from pkg_resources import NullProvider


Algoritmo alfanumerico (ca: CADENA): CADENA
    #La copia de "ca" sin los caracteres no alfanuméricos.

precondicion
    ca ≠ NULO 

realizacion
    si
        ca = CADENA_VACIA
    entonces 
        Resultado <- CADENA_VACIA
    si no si 
        es_alfabético(primero(ca)) 
        o si no 
            es_una_cifra(primero(ca))
    entonces 
        Resultado <- cadena(primero(ca)) ⊕ alfanumerico(fin(ca))
    si no 
        Resultado <- alfanumerico (fin(ca))
    fin si