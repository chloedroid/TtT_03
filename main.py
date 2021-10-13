# export records webpublicatie = 'Europeana' uit adlib naar csv
# zet csv om naar dataframe

import pandas as pd
# pip install pandas in terminal

df = pd.read_csv("stam.csv", delimiter=',')
print(df)

# read kolomnamen
# print(df.columns)

# read meerdere kolommen
# df2 = df[['object_name', 'creator']])
# print(df2)

# read 1 of meer rij(en)
# print(df.iloc[1:4])

# read een specifieke locatie
# print(df.iloc[1:10,1:2])

# om dataframe te bekijken, laat bovenstaande lopen in python console ipv terminal en klik op 'view as dataframe'

#######################################################################################################################

# transformaties van de dataframe

# 1. wijzigen kolomnaam

# df = df.rename(columns={"institution.name": "instellingsnaam", "production.place": "plaats vervaardiging"})
# print(df)

#######################################################################################################################

# 2. delete kolom

# df3 = df.drop(["object_name", 'instellingsnaam'], 1)
# print(df3)

#######################################################################################################################

# 3. toevoegen kolom

# df['Test'] = df['object_name'] + df['institution.name']
# print(df)

#######################################################################################################################

# 4. verplaats kolom

# cols = list(df.columns.values)
# print(cols)
# df = df[cols[0:1] + [cols[-1]] + cols[2:24]]
# print(df)

#######################################################################################################################

# 5. alfabetisch/numeriek sorteren

# df = df.sort_values('material', ascending=False)
# print(df)

# df5 = df.sort_values(['creator', 'material'], ascending=[1,0])
# print(df5)

#df6 = df.sort_values('objectnummer')
#print(df6)

#######################################################################################################################

# 6. filteren

# df3 = df.loc[df['production.place'] == 'Gent']
# print(df3)

#######################################################################################################################

# 7. filteren op meerdere condities

# df4 = df.loc[(df['production.place'] == 'Gent') & (df['creator.role'] == 'ontwerper')]
# print(df4)

#######################################################################################################################

# 8. csv opslaan

# df4.to_csv('Gentseontwerpers.csv')

#######################################################################################################################

# 9. waarden tellen

# 9.1 aantal records
# aantal_records = df["object_name"].count()
# print(aantal_records)

#######################################################################################################################

# 9.2 tellen van het aantal records met een beschrijving
# beschrijving = df["description"].count()
# print(beschrijving)

#######################################################################################################################

# 9.3 aantal records vervaardigd in Gent
# filteren op waarde die je wil tellen
filterplaatsGent = df.loc[df['production.place'] == 'Gent']

# tellen aantal keer waarden voorkomt in kolom
records_vervaardigdinGent = filterplaatsGent['production.place'].count()
print(records_vervaardigdinGent)

#######################################################################################################################

# visualiseren met matplotlib

from matplotlib import pyplot as plt
# pip install matplotlib

# 1. aantal records vervaardigd in Gent
vervaardigingGent = [aantal_records-records_vervaardigdinGent, records_vervaardigdinGent]
plt.pie(vervaardigingGent)
plt.show()

#######################################################################################################################

# 2. voorbeeld van barchart met ontbrekende velden

vervaardiger = df["creator"].count()
vervaardiger_rol = df["creator.role"].count()
vervaardiging_plaats = df["plaats vervaardiging"].count()
vervaardiging_datumbegin = df["vervaardiging.datum.begin"].count()
vervaardiging_datumeind = df["vervaardiging.datum.eind"].count()
associatie_onderwerp = df["associatie.onderwerp"].count()

velden = ["vervaardiger", "rol vervaardiger", "plaats vervaardiging", "datum vervaardiging begin",
          "datum vervaardiging eind", "associatie onderwerp"]
aanwezig = [vervaardiger, vervaardiger_rol, vervaardiging_plaats, vervaardiging_datumbegin, vervaardiging_datumeind,
            associatie_onderwerp]
afwezig = [aantal_records-vervaardiger, aantal_records-vervaardiger_rol, aantal_records-vervaardiging_plaats,
           aantal_records-vervaardiging_datumbegin, aantal_records-vervaardiging_datumeind,
           aantal_records-associatie_onderwerp]

plt.bar(velden, aanwezig)
plt.bar(velden, afwezig, bottom=aanwezig)
plt.show()

#######################################################################################################################

# brainstorm project cogent datavisualisatie
#    - gemeenschappelijke grafieken (inclusief thesaurus & personen/instellingen)
#    - grafieken per instelling