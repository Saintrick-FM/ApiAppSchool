# class Africain:
#     COULEUR_YEUX = 'noir'
#     NEZ = 'épaté'
#
#     def __init__(self, nom_objet, taille_propre, sexe_objet):
#         self.nom= nom_objet
#         self.taille= taille_propre
#         self.sexe= sexe_objet
#
#     def __str__(self):
#         return self.nom
#
#     def marcher(self):
#         print('Je marche')
#
#     def manger(self):
#         print('Je mange')
#
#
# africain1= Africain('loris', 'géant', 'masculin')
#
#
# africain3 = Africain
# africain3.nom= 'leonel'
# africain3.taille= '1m50'
#
# print('africain3 {}.'.format(africain3))
#
#


class FiguresGeometriaues:
    # POIL = 'blanc'
    # QUEUE = 'longue'

    def __init__(self, nom, longueur, largeur):
        self.nomOjet= nom
        self.longueurOjet= longueur
        self.largeurOjet = largeur

    def CalculSuperficie(self):
        superficie = self.longueurOjet*self.largeurOjet
        print('superficie de ', self.nomOjet, ' => ', superficie)


figure1 = FiguresGeometriaues('carré', 2, 2)
figure1.CalculSuperficie()
figure2=FiguresGeometriaues('rectangle', 8, 4)
figure2.CalculSuperficie()