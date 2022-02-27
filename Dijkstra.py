#Parte 1 Función permutar:
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
