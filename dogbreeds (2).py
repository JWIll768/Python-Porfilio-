dogbreads  = ["Affenpinscher " , "AfghanHound " , "AiredaleTerrier " , "AkbashDog " , "Akita " , "AlapahaBlueBloodBulldog " , "AlaskanHusky " , "AlaskanMalamute " , "AmericanEskimoDog " , "AmericanFoxhound " , "AmericanPitBullTerrier " , "AmericanWaterSpaniel " , "AnatolianShepherdDog " , "AustralianKelpie " , "AustralianShepherd " , "Azawakh " , "Basenji " , "BassetBleudeGascogne " , "Beagle " , "Beauceron " , "BedlingtonTerrier " , "BelgianMalinois " , "BelgianTervuren " , "BerneseMountainDog " , "BlackandTanCoonhound " , "Bloodhound " , "BluetickCoonhound " , "Boerboel " , "BorderTerrier " , "BostonTerrier " , "BouvierdesFlandres " , "Boxer " , "BoykinSpaniel " , "BraccoItaliano " , "Briard " , "Brittany " , "Bullmastiff " , "CairnTerrier " , "CaneCorso " , "CardiganWelshCorgi " , "CatahoulaLeopardDog " , "CaucasianShepherd(Ovcharka) " , "CavalierKingCharlesSpaniel " , "ChineseCrested " , "Chinook " , "ChowChow " , "ClumberSpaniel " , "CockerSpaniel(American) " , "CotondeTulear " , "Dalmatian " , "DogoArgentino " , "EnglishShepherd " , "EnglishSpringerSpaniel " , "Eurasier " , "FieldSpaniel " , "FinnishLapphund " , "GermanPinscher " , "GermanShepherdDog " , "GermanShorthairedPointer " , "GiantSchnauzer " , "GlenofImaalTerrier " , "GoldenRetriever " , "GordonSetter " , "GreatDane " , "GreatPyrenees " , "Greyhound " , "Harrier " , "Havanese " , "IrishSetter " , "IrishWolfhound " , "ItalianGreyhound " , "JapaneseChin " , "Keeshond " , "Komondor " , "Kuvasz " , "LabradorRetriever " , "LagottoRomagnolo " , "Leonberger " , "LhasaApso " , "Maltese " , "MiniatureSchnauzer " , "Newfoundland " , "NorfolkTerrier " , "Papillon " , "PembrokeWelshCorgi " , "PharaohHound " , "Plott " , "Pug " , "RedboneCoonhound " , "RhodesianRidgeback " , "Rottweiler " , "Samoyed " , "Schipperke " , "ScottishDeerhound " , "ShihTzu " , "SilkyTerrier " , "SoftCoatedWheatenTerrier " , "SpanishWaterDog " , "Vizsla " , "Weimaraner"]
dogweights = [6,50,40,90,65,55,38,65,20,65,30,25,80,31,35,33,22,35,20,80,17,40,40,65,65,80,45,110,12,10,70,50,25,55,70,30,100,13,88,25,50,80,13,10,50,40,55,20,9,50,80,44,35,40,35,33,25,50,45,65,32,55,45,110,85,50,40,7,35,105,7,4,35,80,70,55,24,120,12,4,11,100,11,3,25,40,40,14,45,75,75,50,10,70,9,8,30,30,50,55]
import random
#Loop through weight list finding tiny dogs
#Filtering
#Functions

filtered_list = []
def dog_size():
    size = input("What size dog are you looking for? (tiny,small, medium, large)")
    if size == "tiny":
        for i in range(len(dogweights)):
            if dogweights[i] <=10 :
                filtered_list.append(dogbreads[i])
        print(filtered_list)

    if size == "small":
        for i in range(len(dogweights)):
            if dogweights[i] >= 11 and dogweights[i] <= 25:
                filtered_list.append(dogbreads[i])
        print(filtered_list)

    if size == "medium":
        for i in range(len(dogweights)):
            if dogweights[i] >= 26 and dogweights[i] <= 60:
                filtered_list.append(dogbreads[i])
        print(filtered_list)

    if size == "large":
        for i in range(len(dogweights)):
            if dogweights[i] >= 60
                filtered_list.append 0(dogbreads[i])
        print(filtered_list) 0

def dog_choice():
        x = random.choice(filtered_list)
        print("We recommend " + x + " dog breed ")

#Main
dog_size()
dog_choice()
