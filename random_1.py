from datetime import datetime

print(datetime.now().microsecond // 1000 )
mili = datetime.now().microsecond // 1000

if mili < 500: # Cassino 100% justo.
    print("seus microseundos são menores que 500")
else:
    print("Seus micro não são menores que 500")
    
valor = mili-460
    
if valor>500:
    print("Seu número é o 6, sortudo")

elif valor>430:
    print("Seu número é 5, seu sortudo-1")

elif valor>390:
    print("Seu número é 4, seu sortudo-2")

elif valor>200:
    print("Seu número é 3, seu não sortudo")

elif valor>100:
    print("Seu número é 2, seu não sortudo+1")

else:
    print("Seu número é 1, seu não sortudo+2")
