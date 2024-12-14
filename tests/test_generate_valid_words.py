import pytest

from solver import generate_valid_words

def test_generate_valid_words_start_d():
    """On sait que la première lettre du mot est un D"""
    assert generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]
    ) == ["DEVANT"]


def test_generate_valid_words_suitable_word():
    """On sait que le mot n'e contient pas de lettre 's' et contient 'M' """
    assert generate_valid_words(
        possible_words=["SAISIR", "VOISIN", "POINTE", "MARIER"],
        letters_in_secret=[("M",0)],
        letters_not_in_secret=["S"]
    ) == ["MARIER"]
    
    
def test_generate_valid_words_fichier_vide():
    """On sait que le fichier possible words est vide"""
    assert generate_valid_words(
        possible_words=[],
        letters_in_secret=[('K',2),('E',1)],
        letters_not_in_secret=[]
    ) == []    
    
    
    
def test_generate_valid_words_instance():
    """#S'assurer que la fonction retourne bien une liste"""
    assert isinstance(generate_valid_words(
        possible_words=["DEVANT", "ENTREE", "PORTER", "GAUCHE"],
        letters_in_secret=[('D', 0)],
        letters_not_in_secret=[]),list)