#Ejercicio Palíndromos 
#Primera Parte: Filtración
from imp import create_dynamic
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

postcondicion
    (∀k ∈ Z)
    (indice_valido(resultado,k)=>
    #el caracter del Resultado de ídice k pertenece a "ca"
    item(Resultado, k) pertenece a ca y(#Es un carater o una cifra
        es_alfabetico(item(Resultado,k))
      o si no 
        es_una_cifra(item(Resultado,k)))
        )
fin alfanumerico 





#Parte 2: Sustitución de mayúsculas
Algoritmo en_mayuscula(ca:CADENA):CADENA 
        #La cadena es igual a "ca" en mayúsculas.

precondición
    ca ≠ NULO

realización
    si 
        ca = CADENA_VACIA
    entoces 
        Resultado <- CADENA_VACIA 

    si no 
        #concatenar el primer caracter transformado si procede con la transformación del resto de "ca"
        Resultado <- cadena(en_mayuscula(primero(ca))) ⊕ en_mayuscula(fin(ca))
    fin si 

postcondicion
    ca = CADENA_VACIA => Resultado = CADENA_VACIA 
    ca ≠ CADENA_VACIA => Resultado= cadena(en_mayuscula(primero(ca))) ⊕ en_mayuscula(fin(ca))

fin en_mayuscula

#Parte 3: Sustituir los caracteres acentuados
Algoritmo sin_acentos:
    #"ca" sin acentuar

precondicion
    ca ≠ NULO 
    en_mayuscula(ca) = ca 

constante
    MAYUSCULA_ACENTUADA: CADENA
    MAYUSCULA: CADENA 

