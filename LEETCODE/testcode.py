def guess_color(a,b):
    lista, listb, res = list(a), list(b), []
    for i,each in enumerate(listb):
        if listb[i] == lista[i]:
            listb[i] = None
            lista[i] = None
            res.append('Hit')
        if i == len(lista) - 1 or i == len(listb) - 1:
            break
    for i,each in enumerate(listb):
        if listb[i] == None:
            continue
        if listb[i] in lista:
            t = lista.index(listb[i])
            lista[t] = None
            listb[i] = None
            res.append('Peudo Hit')
    print(res)
a = 'RGBY'
b = 'RRGBB'
guess_color(a,b)







