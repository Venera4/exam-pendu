import pytest
from generate_dicts import lire_filtrer_mots


def test_lire_filtrer_mots_file_not_found():
    #Vérifier que la fonction retourne une erreur lorsque le fichier n'existe pas.
    with pytest.raises(FileNotFoundError):
        lire_filtrer_mots('stuff')  # 'stuff' does not exist

def test_lire_filtrer_mots_file_empty():
    #Vérifier que la fonction retourne une erreur lorsque le fichier est vide.
    with pytest.raises(ValueError):
        lire_filtrer_mots('tests/data_test/filetest_empty.txt') 

def test_lire_filtrer_mots_instance():
    #S'assurer que la fonction retourne bien une liste

    chemin="tests/data_test/filetest3.txt"
    filtre=lire_filtrer_mots(chemin)
    assert isinsance(filtre,list)



