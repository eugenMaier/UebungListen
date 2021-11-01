#Name:Eugen Maier
#Klasse:ETS2021
#Datum:01.11.2011



namen = ["Werner", "Udo", "Herbert", "Silke", "Claudia", "Kai", "Kerstin", "Elke", "Toni", "Christina", "Anna", "Ute", "Klaus", "Britta", "Katja", "Simone", "Claus", "Tim", "Theodor"]
namen = namen + ["Andrea", "Andi", "Wolfgang"]  #fügt Namen zur Liste hinzu

namen.sort(reverse = True)              #sortiert die Liste
for i in namen:
    if i == "Christina":
        print("Christine")
    else:

        print(i)
print("Ende der Schleife", len(namen))  #zählt wie viele namen in der Liste sind
for i in namen[::-1]:
    if i == "Christina":                #ersetzt Christina in der Liste
        print("Christine")
    else:

        print(i)
print("Ender der zweiten Schleife", len(namen))
    



