#Sovelluksen tervetuloa
print("************************************")
print("***Tervetuloa leivontamuuntimeen!***")
print("************************************")

#Tyhjä rivi1
print("")

#Sovelluksen suorittamisen aloitus
aloitetaanko = input('Aloita muuntaminen painamalla "k" ')

#Tyhjä rivi
print("")

while True:

    #Sovellus alkaa
    if aloitetaanko == "k":
        print("Aloitetaan! ")
        #Tyhjä rivi
        print("")
        break

    #Sovellusta ei toteuteta
    elif aloitetaanko != "k":
        print("Toiminto peruutettu! ")
        quit()

#Muuntosuhteen määrittely
#Tuotteiden määrien muutokset voi suorittaa kertomalla määrän (lopullinen/alkuperainen) suhteella
alkuperainen = float(input("Montako annosta/peltiä/kappaletta alkuperäinen ohje tuottaa? Vastaa numerolla. "))
lopullinen = float(input("Montako annosta/peltiä/kappaletta haluat tehdä? Vastaa numerolla. ")) 

#Tyhjä rivi
print("")

#Luodaan listat tuotteille ja niiden määrille
tuotelista = []
maaralista = []
yksikkolista = []

#Annetaan listoille tietoja
while True:

    #Nimetään tuotteet yksitellen
    tuote = input("Mikä on tuotteen nimi? Päätä tuotteiden nimeäminen painamalla enteriä. ")

    if tuote == "":
        break

    tuotelista.append(str(tuote))

    #Annetaan tuotteille määrä
    maara = input("Paljonko tuotetta on? ")

    if maara == "":
        break

    maaralista.append(float(maara))

    #Selvitetään tuotteen yksikkö
    yksikko = input("Mikä on tuotteen yksikkö? ")

    if yksikko == "":
        break

    yksikkolista.append(str(yksikko))

#Luodaan muuttujat jotka laskee tulostettua määrää
i = 0
k = 0

#Tyhjä rivi
print("")

#Tulostetaan tuotteet ja määrät alussa
print("Alkuperäisten tuotteiden nimet ja määrät: ")
while i < len(tuotelista):
    #Tulostetaan tuotelista
    print(tuotelista[i])
    #Muunnetaan liukuluku merkkijonoksi 
    alkuperainenfloat = maaralista[i]
    alkuperainenstr = str(alkuperainenfloat)
    #Tulostetaan määrä ja yksikkö samalle riville
    print(alkuperainenstr + " " + yksikkolista[i])
    i += 1

#Tyhjä rivi
print("")

print("Lopullisten tuotteiden nimet ja määrät: ")
while k < len(tuotelista):
    #Tulostetaan tuotelista
    print(tuotelista[k])
    #Muunnetaan liukuluku merkkijonoksi
    lopullinenfloat = maaralista[k] * (lopullinen/alkuperainen)
    lopullinenstr = str(lopullinenfloat)
    #Tulostetaan määrä ja yksikkö samalle riville
    print(lopullinenstr + " " + yksikkolista[k])
    k += 1

#Viimeinen tulostus
print("")
print("********************************************************")
print("***Sovellus suoritettiin onnistuneesti loppuun saakka***")
print("********************************************************")
