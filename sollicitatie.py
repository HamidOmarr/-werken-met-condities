print ('------------------------------------------------------------')
print ('Vacature: Circusdirecteur voor Circus HotelDeBotel')
print ('------------------------------------------------------------')

name=input('Wat is je Naam + achternaam?')
print ('Hallo,' + name)

Geslacht=input('Ben je een Man of Vrouw?')
if Geslacht == 'man' or  Geslacht == 'vrouw':
    print ('+++++++++++++++++++++++++++++++++')
    print ('Naam:' + name)
    print ('Geslacht:' + Geslacht)
    print ('+++++++++++++++++++++++++++++++++')


if Geslacht == 'man' or  Geslacht == 'vrouw':
    Dressuur = int(input('Hoeveel jaar praktijkervaring heb je met dieren-dressuur?'))
    Jongleren = int(input('Hoeveel jaar ervaring heb je met jongleren?'))
    Acrobatiek = int(input('Hoeveel jaar praktijkervaring heb je met acrobatiek?'))
    Mbo = input('Ben jij in bezit van een MBO-4 diploma? [J/N]')
    vrachtwagen= input('Ben jij in bezit van een geldig Vrachtwagen rijbewijs? [J/N]')
    HogeHoed = input('Ben jij in bezit van een hoge hoed? [J/N]?')
else:
    print ('Niet geldig')


if Geslacht == 'man':
    Snor= int(input('Hoe breed is u snor?'))
    lengte=input('Wat is uw lengte?')
    Gewicht=input('Wat is uwlichaamsgewicht?')
    Certificaat = input('heeft u de Certificaat "Overleven met gevaarlijk personeel"?') 
    if Certificaat == 'ja' and Mbo == 'ja' and Snor >= 10 and (Dressuur > 4  or Jongleren > 5 or Acrobatiek > 3):
        print ('Geweldig, wij hebben besloten om je aan te nemen.')
    else:
        print ('Helaas, wij hebben besloten om je niet aan te nemen.')

elif Geslacht == 'vrouw':
    krulhaar = input('Heeft u rood krulhaar [J/N]')
    krulhaarlengte = int(input('Wat is uw haarlengte in cm?'))
    lengte=input('Wat is uw lengte?')
    Gewicht=input('Wat is uwlichaamsgewicht?')
    Certificaat = input('heeft u de Certificaat "Overleven met gevaarlijk personeel"?') 
    if Certificaat == 'ja' and Mbo == 'ja' and krulhaar == 'ja' and krulhaarlengte >= 20 and (Dressuur > 4  or Jongleren > 5 or Acrobatiek > 3):
        print ('Geweldig, wij hebben besloten om je aan te nemen.')
    else:
        print ('Helaas, wij hebben besloten om je niet aan te nemen.')



