# EJERCICIOS_Rec
La tarea de esta semana consta de 3 ejercicios en los que debíamos emplear funciones recursivas. Para presentarlos he creado el repositorio de github cuyo enlace adjunto: 

Ejercicio 1: Debíamos elaborar los algoritmos que nos permitiesen realizar una búsqueda por dicotomía

![ejercicio dicotomia](https://user-images.githubusercontent.com/91721826/155897052-c953e5c4-8cbe-4e20-a491-2b7d9224d6c6.jpg)
![Jupi](https://user-images.githubusercontent.com/91721826/155897055-0d8d7a55-6acc-46f4-9f1f-047371c398a0.jpg)


Ejercicio 2: COnsiste en elaborar los algoritmos que nos permitiesen identificar palíndromos. Para ello, tuvimos que realizar funciones que nos permitiesen:

      1. eliminar los carcteres no alfanuéricos.
      
      2. sustituir los caracteres alfabéticos por sus respectivas mayúsculas.
      
      3. eliminar los acentos en los caracteres alfabéticos.
      
      4. comprobar que la cadena resultante  fuese igual a la inversa de la misma.
      
  ![palindromo](https://user-images.githubusercontent.com/91721826/155897038-9499a0f4-0a1e-4493-9944-0de009ceaca7.jpg)
  

      
Ejercicio 3: Teniendo en cuenta una serie de n fichas de colores distintos, se nos pide elabrorar un algoritmo que ordene la mismas en 3 series, de tal manera que que queden agrupadas aquellas que tengan el mismo color. 

Los respectivos pseudocódigos de mi trabajo son:
1. Ejercicio Dicotomía:

```Algoritmo dicotomia:
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

2. Ejercicio Palíndromos
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

3. Ejercicio Dijkstra
Algoritmo permutar(serie_fichas: CADENA; i,j,k,n:ENTERO)
    #Mover la ficha a la situación "j+1" en la serie de su color
precondicion
    indice_valido(serie_fichas, 1)
    indie_valido(serie_fichas, n)

    sub_cadena(serie_fichas, 1,n) ≠ NULO 
    0<=i<=n
    0<=j<=n
    0<=k<=n
    (∀ m ∈ N)
    (1<=m<=i => item(serie_fichas, m)= "R")
    (i+1<=m<=j => item(serie_fichas, m)= "V")
    (k+1<=m<=n => item(serie_fichas, m)= "B")

realizacion
    si k ≠ j entonces 
        #Falta desplazar fichas de índices comprendidos entre j+1 y k
        #Observar la ficha indice j+1
        segun el valor de 
            item(serie_fichas, j+1)
        hacer 
            si "R" entonces
                #La ficha es Roja: intercambiarla con la ficha Verde que ocupa el lugar i+1
                intercambiar(
                    item(serie_fichas, i+1),
                    item(serie_fichas, j+1)
                        )
                #(A1´): ROJAS DESDE 1 HASTA i+1
                #(A2´): VERDES DESDE i+2 HASTA j+1
                #(A3): AZULES DESDE k+1 HASTA n
                permutar(serie_fichas, i+1, j+1, k, n)
            fin si 

            si "V" entonces
                #La ficha es Verde; está en su lugar y S2 
                #se extiende desde i+1 hasta j+1
                #(A1):ROJAS DESDE 1 HASTA i
                #(A2´): VERDES DESDE i+1 HASTA j+1
                #(A3): AZULES DESDE k+1 HASTA n
                permutar(serie_fichas,i,j+1,k,n)
            fin si 

            si "B" entonces
                #La ficha Azul: intercambiarla con la ficha de índice k
                intercambiar(
                            item(serie_fichas, j+1)
                            item(serie_fichas,k)
                            )
                #(A1):ROJAS DESDE 1 HASTA i
                #(A2): VERDES DESDE i+1 HASTA j
                #(A3´): AZULES DESDE k HASTA n
                permutar(serie_fichas,i,j,k-1,n)
            fin si
        fin hacer 
    fin si

postcondicion
    antiguo(i)=i; antiguo(j) = j; antiguo(k)=k 
    serie_fichas ="RR...RVV...VBB..B"

fin permutar 

Algoritmo bandera 
constante
    CANTIDAD_FICHAS_MAX: ENTERO <-????
        #número mñaximo de fichas a ordenarç

variable 
    fichas: CADENA[COLOR][1, CANTIDAD_FICHAS_MAX]

inicialización
    fichas <- ??????

realizacion
    permutar(fichas,0,0,longitud(fichas), longitud(fichas))

fin bandera
