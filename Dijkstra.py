#Parte 1 Función permutar:
from msvcrt import kbhit
from pkg_resources import NullProvider


permutar(serie_fichas: CADENA; i,j,k,n:ENTERO)
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
