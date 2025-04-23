#no podes leer el archivo mas de una vez
votos_partido={}
with open("RESULTADOS.TXT","rt",encoding="utf-8")as archivo:
    for linea in archivo:
        partido,lista=linea.split(";")
        if partido in votos_partido:
            votos_partido[partido]+=1
        else:
            votos_partido[partido]=1
partido_ganador=max(votos_partido,key=votos_partido.get)
#Diccionario de votos por lista del ganador
votos_lista={}
with open("RESULTADOS.TXT","rt",encoding="utf-8") as archivo:
    for linea in archivo:
        partido,lista=linea.split(";")
        if partido==partido_ganador:
            if lista in votos_lista:
                votos_lista[lista]+=1
            else:
                votos_lista[lista]=1
votos_partido= dict(sorted(votos_partido.items(),key=lambda x: x[1], reverse=True))
total_votos=sum(votos_partido.values())
for partido in votos_partido:
    ast=""int(votos_partido[partido]//2)
    porc=(votos_partido[partido]/total_votos)100
    print(f"{partido.ljust(20)}{ast.center(2)}{porc:.1f}%")
print("\n")
votos_partido= dict(sorted(votos_lista.items(),key=lambda x: x[1], reverse=True))
total_votos=sum(votos_lista.values())
print("Partido Ganador:",partido_ganador)
for lista in votos_lista:
    lista2=lista.strip()
    ast=""int(votos_lista[lista]//2)
    porc=(votos_lista[lista]/total_votos)100
    print(f"Lista{lista2.ljust(10)} {ast.center(2)} {porc:.1f}%")