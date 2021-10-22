import os
print("Donnez le nom du fichier sans extansion :")
NomFichier1 = input() + ".cnf"
Fichier1 = open(NomFichier1, "r")
NomFichier2 = NomFichier1[0:-4] + "temp" + ".cnf"
Fichier2 = open(NomFichier2 , "w")
print("Donnez le nombre de clauses :")
NombreClauses = input() 
stri = Fichier1.readline()[0:-4] + str(int(NombreClauses)+1)
Fichier2.write(stri)
Fichier2.write("\n")
for ligne in Fichier1.readlines():
    Fichier2.write(ligne)

print("Veuillez insérer le but (en chiffre):\n"
"parmis les propositions suivantes:\n"
"Na ⇒ 1	Nb ⇒ 2		Nc ⇒ 3		céa ⇒ 4	céb ⇒ 5	céc ⇒ 6\n"
"coa ⇒ 7	cob ⇒ 8	coc ⇒ 9	Ma ⇒ 10	Mb ⇒ 11	Mc ⇒ 12\n")

But = input()

NouvelleClause = str(int(But)*-1) + "   " +  str(0)
Fichier2.write(NouvelleClause)

Command = str("./ubcsat -alg saps -i ZOO_V2.cnf -solve > test.txt")

os.system(Command)

with open('test.txt') as f:
    if 'PercentSuccess = 100.00' in f.read():
        print("Il existe une solution !!")
    else:
        print("Pas de solutions trouvées")
