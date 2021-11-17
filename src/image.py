from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        img_bin = Image()
        img_bin.set_pixels(np.zeros((self.H, self.W), dtype=np.uint8))

        for y in range(len(self.pixels)):
            for x in range(len(self.pixels[y])):
                if self.pixels[y][x] >= S: # Est ce que le seuil est inclut ou exclu ?
                    img_bin.pixels[y][x] = 255

        return img_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        
        x_min = min(np.where(self.pixels==255)[1])
        x_max = max(np.where(self.pixels==255)[1])

        y_min = min(np.where(self.pixels==255)[0])
        y_max = max(np.where(self.pixels==255)[0])

        """
        for y in range(len(self.pixels)):
            if 255 in self.pixels[y]:
                y_min = y
                break
        
        for y in range(len(self.pixels)-1, y_min, -1):
            if 255 in self.pixels[y]:
                y_max = y
                break
        
        x_min = self.pixels[y_min].index(255)
        x_max = len(self.pixels[y_min]) - 1 - self.pixels[y_min][::-1].index(255)

        for y in range(y_min, y_max+1):
            index_first_255 = self.pixels[y].index(255)
            index_last_255 = len(self.pixels[y]) - 1 - self.pixels[y][::-1].index(255)

            if index_first_255<x_min:
                x_min=index_first_255

            if index_last_255>x_max:
                x_max=index_last_255
        """
        new_img = Image()
        new_img.set_pixels(np.zeros((y_max-y_min+1, x_max-x_min+1)))
        new_img.pixels=np.array(self.pixels[y_min:(y_max+1)][x_min:(x_max+1)])
        return new_img

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        pass


    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        pass

