import pandas

class Cellule:
    def __init__(self, texte):
        self.texte = texte # texte de la cellule
        self.valeur = None   # le résultat numérique
        self.en_cours = False  # pour détecter les cycles
        self.erreur = None     # si il ya une erreur dans le calcul ou un cycle
import pandas as pd

fichier = pandas.read_csv("test", header=None)

nb_lignes, nb_colonnes = fichier.shape # compter les lignes et colonnes

def indice_to_colonne(ind): # convertir un indice en lettre de colonne
    resultat = ""
    while True:
        ind, reste = divmod(ind, 26)
        lettre = chr(ord('A') + reste)
        resultat = lettre + resultat
        if ind == 0:
            break
        ind -= 1
    return resultat

def creer_dico(fichier):
    nb_lignes, nb_colonnes = fichier.shape
    grille = {}

    for i in range(nb_lignes) : # index lignes
        for j in range(nb_colonnes) : # index colonnes
            lettre_colonne = indice_to_colonne(j)
            numero_ligne = i + 1
            nom_cellule = f"{lettre_colonne}{numero_ligne}" 
            texte = fichier.iat[i, j]  # texte de la cellule
            if pandas.isna(texte): # si la cellule est vide, on met une chaîne vide
                texte = "" 

            grille[nom_cellule] = Cellule(str(texte)) # ajouter la cellule au dictionnaire

    return grille
