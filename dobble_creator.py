#Laura Cadillo
#Lylian Challier

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image, ImageOps
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size


    def create_card(self, symbols): 
        #colors needed for the cards
        background_color = (255, 255, 255)  #white 
        border_color = (224, 224, 224)  #black
        #create the card with the background color
        white_card = Image.new("RGB", (self.pic_size, self.pic_size), background_color)

        #where the images will be pasted in the card
        coordenates = [0, 0]
        #data needed to resize the images
        total_images = len(symbols) +1 
        max_cards_per_row =  math.sqrt(total_images)
        max_size_card = round(self.pic_size // max_cards_per_row)
        size_card = round(max_size_card // 1.25)

        for symbol in symbols:
            
            #find the path of the images that will be pasted in the card
            image_file = os.path.join("images", f"{symbol}.png")
            image = Image.open(image_file)
            # rotate the images to make them look more random
            image = image.rotate(random.randint(0, 180), expand=True)
            #change the size of the images to fit in the card
            image = image.resize((size_card, max_size_card))

            white_card.paste(image, (coordenates[0], coordenates[1]), image)
            #change the coordenates to paste the next image
            coordenates[0] += max_size_card 
            # end of the card reached, change the row
            if coordenates[0] >= self.pic_size - size_card :
                #go back to the start of the row
                coordenates[0] = self.border_size
                #go to the next row
                coordenates[1] += max_size_card 

        #add a border to the card
        white_card_with_border = ImageOps.expand(white_card, border=self.border_size, fill=border_color)
        return white_card_with_border
        
        
       
    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")
    

        with open(cards_file, 'r') as file:
            # initialize on 1 to save the cards with the correct name
            i = 1
            for line in file:
                #read each card's symbols
                card_symboles = list(map(int, line.strip().split()))
                #create the cards
                card = Creator.create_card(self, card_symboles)
                #save the cards in the results folder
                card.save(f"results/card{i}.jpg")
                #save next card
                i+=1
                
 