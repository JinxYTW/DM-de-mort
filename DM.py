def sous_tab(p:list):
    l=[]
    for i in range(len(p)):
        l.append(p[i])
        for k in range(len(l)-1):
            if len(l) > 1:
                l.append(p[i]+l[k])
    l.insert(0,0)
    return ((l))

    #%%
'''Les éléments de Sk+1 sont les éléments de Sk avec l'élément Pi+1,ainsi que la somme de Pi+1 avec les termes de Sk.
De ce fait,on a:
Sk+1=[terme de Sk , Pi+1, somme de Pi+1 avec les termes de Sk]

Exemple:

S2=[1,3,4]
S3=[1,3,4,5,6,8,9]
Soit:
S2=[1,3,4]
S3=[1,3,4,5,5+1,5+3,5+4]
Soit:
S2=[1,3,4]
S3=[S2,5,5+1,5+3,5+4]

Avec S0=[0]'''
#%%
def somme_min(p):
    S=max(p)
    C=[]
    for i in range(len(p)):
        if p[i] >= S/2:
            C.append(p[i])
    return (min(C))
#%%
def sol_tab(L:list):
    cache = {0:[]}
    l=[]
    for i in range(len(L)):
        l.append(L[i])
        if L[i] not in cache:
            cache[L[i]] = [L[i]]
        for k in range(len(l)-1):
            if len(l) > 1:
                l.append(L[i]+l[k])
                if l[-1] not in cache:
                    cache[l[-1]] = [l[k],L[i]]
    print(cache)
    for cle, valeur in cache.items():
        for element in valeur:
            if valeur.count(element) > 1:
                if element in cache:
                    elementmod = cache.get(element)
                    if len(elementmod) > 1:
                        cache[cle][cache[cle].index(element)] = elementmod
                        liste = cache[cle]
                        flat = [int(p) for p in [ p for i in liste for p in list(str(i)) if p != ' ' and p != "[" and p != "]" and p != ","]]
                        cache[cle] = flat
                
    return cache
#%%
L=[5,[-19,8],8,[185,97,212,56,89],[3, 1]]
print (type(L))
flat = [int(p) for p in [ p for i in L for p in list(str(i)) if p != ' ' and p != "[" and p != "]" and p != ","]]
print(flat)
#%%
def sol_tabb(L:list):
    #Je sais déjà que c'est pas légal,donc la moindre des choses c'est d'expliquer
    
    #La partie qui suit permet de créer le dictionnaire de façon très bête
    cache = {0:[]}
    l=[]
    for i in range(len(L)):
        l.append(L[i])      
        for k in range(len(l)-1):
            if len(l) > 1:
                l.append(L[i]+l[k])
                if l[-1] not in cache:
                    cache[l[-1]] = [l[k],L[i]]
        if L[i] not in cache:
            cache[L[i]] = [L[i]]
    #Cette partie permet de remplacer une valeur des listes par sa correspondance trouvable dans le dictionnaire
    for cle, valeur in cache.items():
        for element in valeur:
            if valeur.index(element) != 0:
                if element in L:
                    if valeur.count(element) > 1:
                        if element in cache:
                            elementmod = cache.get(element)
                            if len(elementmod) > 1:
                                cache[cle][cache[cle].index(element)] = elementmod
                                liste = cache[cle]
                                flat = [int(p) for p in [ p for i in liste for p in list(str(i)) if p != ' ' and p != "[" and p != "]" and p != ","]]
                                cache[cle] = flat
            else:
                if element in cache:
                    elementmod = cache.get(element)
                    if len(elementmod) > 1:
                        cache[cle][cache[cle].index(element)] = elementmod
                        liste = cache[cle]
                        flat = [int(p) for p in [ p for i in liste for p in list(str(i)) if p != ' ' and p != "[" and p != "]" and p != ","]]
                        cache[cle] = flat
    #Celle-ci de trier le dictionnaire par ordre croissant des clés                    
    sorted_cache = {}
    for key in sorted(cache.keys()):
        sorted_cache[key] = cache[key]                 
                           
    return sorted_cache


