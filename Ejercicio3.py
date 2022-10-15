lista = [1,3,4,7,99,3,1,5,6,7,2,9,2,5,99,-1,-2,9,3,44,5]

def modificar(l):
  
    l = list(set(l))  
    l.sort(reverse=True)  
 
    impares = []  
    for i in l:
        if i%2 == 0:
            impares.append(i)
            
    suma = sum(impares)  
    impares.insert(0, suma)  
    return impares  


nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )