#Ejercicio Palíndromos 
#Primera Parte: Filtración
from imp import create_dynamic
from signal import siginterrupt
from pkg_resources import NullProvider

from Dicotomia import AUSENTE


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
Algoritmo sin_acento:
    #"ca" sin acentuar

precondicion
    ca ≠ NULO 
    en_mayuscula(ca) = ca 

constante
    MAYUSCULA_ACENTUADA: CADENA
    MAYUSCULA: CADENA 

realizacion
    si 
        ca=CADENA_VACIA 
    entonces
        Resultado <- CADENA_VACIA 
    si no si 
        situacion(primero(ca), MAYUSCULA_ACENTUADA) ≠ AUSENTE
    entonces 
        Resultado <- cadena(item(MAYUSCULA, situacion(primero(ca)))
        ⊕
        sin_acento(fin(ca)))
    si no 
        Resultado <- primero(ca)⊕sin_acento(fin(ca))
    fin si 

postcondicion
    ca= CADENA_VACIA => Resultado = CADENA_VACIA
    ca ≠ CADENA_VACIA => Resultado = ("ca" sin acentuar)

fin sin_acento

#Parte 4: Determinar si es un Palíndromo
Algoritmo palindromo:
    #Determinar si "frase" es un palindromo
precondicion
    frase ≠ NULO 

variable 
    ca:CADENA 

realizacion:
    ca <-alfanumerico(ca)
        #filtrar "frase" para que solo se conserven los caracteres alfanuméricos
    ca <- en_mayuscula(ca)
        #transformar todos los caracteres alfabéticos en mayúscula
    ca <- sin_acento 
        #eliminar los acentos de los caracteres alfabéticos
    si 
        ca = inverso(ca) 
    entonces 
        escribir "Es un palindromo"
    si no si 
        ca ≠ inverso(ca)
    entonces 
        escribir "No es un palindromo"
    fin si 
postcondicion 

fin palindromo
