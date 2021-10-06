j = ('ja') 
n = ('nee')

vraag1 = ('Is de kaas geel? [ja of nee]?')
vraag2 = ('Zitten er gaten in kaas? [ja of nee]?')
vraag3 = ('Heeft de kaas blauwe schimmels? [ja of nee]?')
vraag4 = ('Heeft de kaas een korst? [ja of nee]?')
vraag5 = ('Is de kaas belachelijk duur? [ja of nee]?')
vraag6 = ('Is de kaas hard als steen? [ja of nee]?')
vraag7 = ('Heft de kaas een korst [ja of nee]?')

a = ('Camembert')
b = ('Mozzarella')
c = ('Emmenthaler')
d = ('Leerdammer')
e = ('Parmigiano Reggiano')
f = ('Goudse kaas')
g = ('Blue de Rochbaron')
h = ('Fourme dambert')

antwoord1=input(vraag1)
if antwoord1 == 'ja':
    antwoord2=input(vraag2)
    if antwoord2 =='ja':
        antwoord5=input(vraag5)
        if antwoord5=='ja':
            print (c)
        else:
            print (d)

    if antwoord2 == 'nee':
     antwoord6=input(vraag6)
    if antwoord6 =='ja':
        print(e)
    else:
        print (f)
        
if antwoord1 == 'nee':
    antwoord3=input(vraag3)
    if antwoord3 == 'ja':
     antwoord4=input(vraag4)
     if antwoord4 =='ja':
         print (g)
    else:
         print (h)

if antwoord3 == 'nee':
    antwoord7=input(vraag7)
    if antwoord7=='ja':
        print (a)
    else:
        print (b)