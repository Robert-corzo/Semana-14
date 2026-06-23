def fiboFRB(n): 
    global contador 
    contador +=1 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        return fiboFRB(n - 1) + fiboFRB(n - 2) 

def fiboPDR(n): 
    lista = [-1 for _ in range(n+1)]
    return fiboPDRU(n, lista)

def fiboPDRU(n, lista): 
    global contador 
    contador +=1 
    if lista[n] != -1:
        return lista[n]
    elif n == 0: 
        lista[n] = 0
        return lista[n]
    elif n == 1: 
        lista[n] = 1
        return lista[n]
    else: 
        lista[n] = fiboPDRU(n - 1, lista) + fiboPDRU(n - 2, lista) 
        return lista[n]


contador = 0 
print(f"Resultado PD: {fiboPDR(40)} Contador :{contador}") 

contador = 0 
print(f"Resultado FB: {fiboFRB(40)} Contador :{contador}") 