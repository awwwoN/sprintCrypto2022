#Déchiffrement Monoalphabétique
#Message Chiffré
c="""Atzx sj ujsxnje ytzy ij rjrj ufx vzj stzx fqqntsx atzx ktzwsnw
lwfyznyjrjsy ytzyjx qjx htwwjhyntsx ? Ifsx qj hfiwj ij qf uwjufwfynts iz
XUWNSY stzx fqqtsx atzx uwtutxjw ijx ijknx mjgitrfifnwjx. Ifsx hmfvzj
ijkn nq d fzwf zsj htwwjhynts i'jcjwhnhjx f wjhzujwjw. Qf nq x'fajwj vzj
ytzy hj vzn xzny jxy knsfqjrjsy zs knhmnjw uik jshtij js gfxj64. F atzx
ij ijhtijw ytzy hjqf jy fnsxn wjhtsxynyzjw qj ithzrjsy yfsy jxujwj.
Fyyjsynts xn atzx atzqje ywfsvznqqjrjsy ijhtijw qj gfxj64 vzn xzny stzx
jxujwtsx vzj atzx faje fuuqnvzj qj ijhfqflj vzn atzx f ujwrnx ij qnwj hj
rjxxflj !"""

#On enlève espaces/points/tous les caractères qu'on veut pas
s=''.join([x for x in c if x.isalpha()])
#print(s)

#On compte l'occurence des caractères du texte
freq={}
for x in s:
    freq[x]=freq.get(x,0)+1
#print(freq)

#Petit indice de coincidence
def ic(freq):
    n=0
    divid=0
    result=0
    for x in freq:
        nx=freq[x]  # nombre d'occurences du caractère x
        divid=divid+(nx*nx-1)
        n=n+nx
    #return n
    result=divid/(n*n-1)
    return result   
print('Indice de coincidence : ', ic(freq))

#Tri des caractères par ordre décroissant
l=[(freq[c],c) for c in freq]
l.sort(reverse=True)
print(l)

#Traduction avec les lettres les plus utilisées de la langue française selon Wiki : ESAIN
print(c.translate(str.maketrans('jxztfnywsqi','ESARTINULOD')))