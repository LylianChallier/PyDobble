#Laura Cadillo
#Lylian Challier

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random # pour le melange des symboles sur chaque carte 
# for mixing symbols on each card

class Generator():

    def __init__(self, order=7):
        self.order = order
        #self.cards_file = cards_file

    def add_symbol_to_card(self, symbols, cards): 
        cards_nxn = [[[0] * (self.order + 1) for _ in range(self.order)] for _ in range(self.order)]
        cards_horizon = [[[0] * (self.order + 1)] for _ in range(self.order + 1)]

        # étape 1 plan horizontal
        for i in range(self.order):
            for j in range(self.order):
                cards_nxn[i][j][0] = symbols[i]
                cards_horizon[0][0][i] = symbols[i]

        # étape 2 plan diagonale et étape 3 plan antidiagonale
        for k in range(1, self.order):
            for i in range(self.order):
                for j in range(self.order):
                    cards_nxn[j][(i + j * k) % self.order][k] = symbols[i + k * self.order]
                cards_horizon[k][0][i] = symbols[i + k * self.order]

        # étape 4 plan verticale
        for i in range(self.order):
            for j in range(self.order):
                cards_nxn[j][i][self.order] = symbols[i + self.order ** 2]
                cards_horizon[self.order][0][i] = symbols[i + self.order ** 2]

        # étape 5 complète l'horizon
        for i in range(self.order + 1):
            cards_horizon[i][0][self.order] = symbols[self.order ** 2 + self.order]

        # on insère cards_nxn et cards_horizon dans notre paquet de cartes : cards
        for i in range(self.order):
            for j in range(self.order):
                cards[i * self.order + j][:] = cards_nxn[i][j][:]
        for i in range(self.order + 1):
            cards[self.order ** 2 + i][:] = cards_horizon[i][0][:]

        # on mélange les images de chaque cartes
        for card in cards:
            random.shuffle(card)

    def generate(self, cards_file="cartes.txt", verbose=False):
        nb_cards = self.order ** 2 + self.order + 1
        cards = [[0] * (self.order + 1) for _ in range(nb_cards)]
        symbols = list(range(1, nb_cards + 1))

        # on génère nos cartes
        self.add_symbol_to_card(symbols, cards)

        # on écrit le résultat dans un fichier .txt
        with open(cards_file, "w") as f:
            for card in cards:
                f.write(' '.join(map(str, card)) + '\n')

        if verbose:
            print("***Generation des cartes***")
            print(f"nombre de cartes: {nb_cards}")
            print(f"les symboles: {symbols}")
            print("et les cartes:")
            for card in cards:
                print(card)


# on créée un jeu de cartes d'ordre 7
# on choisit l'ordre et le fichier dans lequel écrire les cartes
instance = Generator(7)
instance.generate("L3/Devoir 1 ALGO/Code/Q4 Dobble/cartes.txt")
