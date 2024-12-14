#import pour calculer l'occurence d'une lettre
from collections import Counter 


def generate_valid_words(possible_words, letters_in_secret, letters_not_in_secret):
  '''
  Permet d'obtenir la liste des mots encore valides en fonction des lettres déjà jouées
 
  Args:
  possible_words [list(str)]: La liste des mots potentiellement valides (par exemple, au départ, tous les mots d'une longueur donnée).
  letters_in_secret [list(tuple)]: Une liste de tuples représentant les lettres déjà trouvées par l'utilisateur ainsi que leur position dans le mot.
  letters_not_in_secret [list(str)]: Une liste des lettres déjà essayées par l'utilisateur mais qui ne sont pas dans le mot.

  Returns:
  List[str]: La liste des mots encore valides
  '''
  mot_valides=[]
  for word in possible_words:
    valid=False
    # Vérifie que le mot ne contient aucune lettre exclue
    if not set(word) & set(letters_not_in_secret):
      for lettre, index in letters_in_secret:
        if word[index]==lettre:
          valid=True
    if valid==True:
      mot_valides.append(word)
  return mot_valides


def generate_best_letters(possible_words:list, letters_not_played:list[str], letters_in_secret, letters_not_in_secret):
    
  '''
  Suggère à l'utilisateur quelle lettre jouer ensuite, en se basant sur la liste des mots valides générée par generate_valid_words 
    
  Args:
  possible_words [list(str)]: La liste des mots encore en jeu après application des règles de generate_valid_words.
  letters_not_played [list(str)]: Une liste de lettres que l'utilisateur n'a pas encore essayées.
  letters_in_secret [list(str)]: La liste des lettres correctement placées dans le mot, avec leurs positions.
  letters_not_in_secret [list(str)]: La liste des lettres qui ne sont pas dans le mot.

  Returns:
  str: une suggestion qui est directement affichée dans le jeu pour guider l'utilisateur vers la meilleure lettre à jouer.
  '''
  letter_occur = Counter(letter for word in possible_words for letter in word)     
  options={}              
  nbr_words=len(possible_words)
  if nbr_words>0:
    for letter in letters_not_played:
      freq_let=letter_occur[letter]/nbr_words
      options[letter]=freq_let

  if options:
        sorted_dict = dict(sorted(options.items(), key=lambda item: item[1], reverse=True))
        max_key = max(options, key=options.get)
        return (f"La meilleure lettre à jouer: {max_key}")
  else:
        print("Aucune lettre valide à jouer")
        return None








