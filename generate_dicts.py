#import pour la suppression des accents
from unidecode import unidecode
 
    """
    Depuis le fichier liste_mots.txt, on récupère tous les mots de 6,7,8,9,10 lettres.
    et on génère 5 fichiers textes contenant les mots en fonction de leur taille (un mot par ligne, séparé par un \n):
    dico_6_lettres.txt
    dico_7_lettres.txt
    dico_8_lettres.txt
    dico_9_lettres.txt
    dico_10_lettres.txt
    On enlève les accents, les espaces, les tirets et les mots en double.
    """

def lire_filtrer_mots(chemin_lexique, longueur):
    """
    Lit les mots depuis le fichier source (par exemple data/liste_mots.txt) et applique un filtre pour retourner une liste de mots d'une longueur donnée en supprimant les accents, les espaces, et les tirets et éliminant les doublons
    
    Args: 
      chemin_lexique(str): Chemin d'accès au fichier de lexique contenant les mots
      longueur(int): Longueur des mots
    
    Returns:
      une liste Python contenant uniquement les mots valides en majuscule ayant la taille spécifiée.
    """
    liste_mots=set()
    with open(chemin_lexique,"r") as f:

      for ligne in f:
        mot=ligne.split()[0]
        mot=unidecode(mot)
        mot=mot.replace("-", "").replace(" ", "").upper()
        if len(mot)==longueur:
          liste_mots.add(mot)
    return list(liste_mots)
    


def ecrire_liste_mots(liste_mots:list, longueur:int) -> None:
    """Génère un fichier texte contenant tous les mots pour une longueur donné
    
    """

    chemin_dico_ecriture:str = f"data/dico_{longueur}_lettres.txt"

    with open(chemin_dico_ecriture, 'w', encoding='utf-8') as file:
        file.writelines(f"{mot}\n" for mot in liste_mots)




def main(chemin:str) -> None:
    for long in range(6,11):
        # génère la liste de mot pour la longueur donné
        lst_mots = lire_filtrer_mots(chemin_lexique=chemin, longueur=long)

        # Génère un fichier texte correspondant
        ecrire_liste_mots(lst_mots, longueur=long)

if __name__ == '__main__':
    chemin = "data/liste_mots.txt"
    main(chemin= chemin)
    
