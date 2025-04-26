#Laura Cadillo
#Lylian Challier

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

#import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file, verbose=False):

        if verbose:
            print("***Verification des cartes***")

        with open(cards_file, "r") as f:
            cards = [list(map(int, line.split())) for line in f.readlines()]

        order = len(cards[0]) - 1

        # TEST JEU VALIDE ??
        # Check the number of symbols per card is the same for each card
        #ESTO HACE AL JUEGO VALIDO
        if any(len(card) != len(cards[0]) for card in cards):
            if verbose:
                print("ERREUR : il n'y a pas le même nombre de symboles sur chaque cartes")
            return 2

        # check that each pair of cards shares one and only one symbol in common
        #ESTO HACE AL JUEGO VALIDO
        for i in range(len(cards) - 1):
            for j in range(i + 1, len(cards)):
                common_symbols = set(cards[i]) & set(cards[j])
                if len(common_symbols) != 1:
                    if verbose:
                        print("ERREUR : chaque paires de cartes n'a pas exactement un symbole en commun")
                    return 2

        # TEST JEU OPTIMAL ??
        # Check the total number of cards and symbols
        #CONDICIONES
        exp_nb_cards = order ** 2 + order + 1
        exp_nb_symbols = order ** 2 + order + 1
        symbols = set([symbol for card in cards for symbol in card])
        exp_symbols_per_card = order + 1

        # ESTO HACE AL JUEGO OPTIMO
        if len(cards) != exp_nb_cards:
            if verbose:
                print(f"ERREUR : le jeu n'est pas optimal, il y a {len(cards)} cartes, il en faudrait {exp_nb_cards}")
            return 1

        if len(cards[0]) != exp_symbols_per_card:
            if verbose:
                print(f"ERREUR : le jeu n'est pas optimal, il y a {len(cards[0])} symboles par carte, il en faudrait {exp_symbols_per_card}")
            return 1

        if len(symbols) != exp_nb_symbols:
            if verbose:
                print(f"ERREUR : le jeu n'est pas optimal, il y a {len(symbols)} symboles, il en faudrait {exp_nb_symbols}")
            return 1

        # aucun test n'est déclenché alors le jeu est valide et optimal
        if verbose:
            print("Le jeu est valide et optimal")
        return 0


# on vérifie les jeux de cartes contenus dans les fichiers cartes_test{i}.txt pour i=1,...,6
# seuls les jeux générés avec comme ordre un nombre premier doivent être valides et optimaux
# pour avoir le détail des erreurs de chaque jeu tester, il faut mettre verbose=True
# on choisit l'ordre et le fichier dans lequel verifier les cartes
instancia = Verificator()
result = instancia.verify("L3/Devoir 1 ALGO/Code/Q4 Dobble/cartes_test6.txt", verbose=True)
