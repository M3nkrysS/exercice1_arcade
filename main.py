"""
Modèle de départ pour la programmation Arcade.
Il suffit de modifier les méthodes nécessaires à votre jeu.
"""
import arcade
from random import randint, choice


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Modèle de départ"


class MyGame(arcade.Window):
    """
    La classe principale de l'application

    NOTE: Vous pouvez effacer les méthodes que vous n'avez pas besoin.
    Si vous en avez besoin, remplacer le mot clé "pass" par votre propre code.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # Si vous avez des listes de sprites, il faut les créer ici et les
        # initialiser à None.

    def setup(self):
        """
        Configurer les variables de votre jeu ici. Il faut appeler la méthode une nouvelle
        fois si vous recommencer une nouvelle partie.
        """
        # C'est ici que vous allez créer vos listes de sprites et vos sprites.
        # C'est aussi ici que vous charger les sons de votre jeu.
        self.black = 0, 0, 0
        self.blue = 0, 0, 255
        self.brown = 177, 117, 89
        self.dark_blue = 0, 0, 128
        self.cyan = 0, 255, 255
        self.gold = 255, 220, 70
        self.green = 0, 255, 0
        self.red = 255, 0, 0
        self.grey = 180, 180, 180
        self.orange = 255, 120, 0
        self.pink = 255, 0, 128
        self.purple = 170, 0, 255
        self.silver = 240, 240, 235
        self.violet = 238, 130, 238
        self.white = 255, 255, 255
        self.yellow = 255, 255, 0
        self.salmon = 255, 76, 76
        self.copper = 245, 175, 145
        self.brass = 220, 175, 90
        self.mandarin = 255, 156, 0
        self.color_list = [self.black, self.dark_blue, self.blue, self.brown, self.cyan, self.gold, self.green, self.red, self.grey, self.orange, self.pink, self.purple, self.silver, self.violet, self.white, self.yellow, self.salmon, self.salmon, self.copper, self.brass, self.mandarin]
        self.number_of_repeats = 0
        self.clear()

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """
        # Cette commande permet d'effacer l'écran avant de dessiner. Elle va dessiner l'arrière
        # plan selon la couleur spécifié avec la méthode "set_background_color".

        while self.number_of_repeats <= 20:
            self.random_color = choice(self.color_list)
            self.circle = arcade.draw_circle_filled(randint(50, 750), randint(50, 550), randint(15, 50),(self.random_color))
            self.color_list.remove(self.random_color)
            self.number_of_repeats += 1
        # Invoquer la méthode "draw()" de vos sprites ici.


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()