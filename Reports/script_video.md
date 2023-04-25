# Script pour la vidéo de présentation du projet

## Introduction

Notre projet consiste à créer une solution algorithmique
et logicielle pour renvoyer le meilleur coup à jouer
dans une partie de puissance 4 en fonction de l'état
du jeu avant le coup. Nous avons pour cela utilisé
un algorithme minimax avec élagage alpha-beta. Le
tout reposant sur une fonction d'évaluation du
jeu qui permet d'attribuer un score au joueur
qui joue le coup.

## Fonction d'évaluation

La fonction d'évaluation est la fonction qui permet
de donner une valeur à un état du jeu du point de
vue d'un joueur. On peut facilement considérer qu'elle
renvoie le "score" du joueur pour un état donné. Cette
fonction est donc très importante pour l'algorithme
minimax qui va chercher à maximiser le score du joueur
qui joue le coup et minimiser celui de son adversaire.

Notre fonction d'évaluation donne un score plus grand
aux états du jeu où le joueur a des jetons proches
non séparés par des jetons adverses. Elle inspecte
chaque rangée de 4 cases (horizontales, verticales
et diagonales) et augmente le score du joueur si
seulement ses jetons sont présents dans la rangée (donc les autres cases doivent être vides). On
augmente de 5 points pour 3 jetons présents et de 2
points pour 2 jetons. On augmente aussi le score de
3 points pout chaque jeton présent dans la rangée
centrale, considérée comme plus stratégique.

Dans cet exemple, le joueur rouge gagne 3 points car il a un jeton sur la colonne centrale, 2 points grâce à la diagonale grise, 2 points grâce à la diagonale verte et 5 points grâce à la diagonale noire. Ce qui fait un total de 12 points
Le joueur jaune quant à lui gagne 6 points car il a 2 jetons sur la colonne centrale, et 2 points grâce à la diagonale grise, 2 points grâce à la diagonale verte, 5 points grâce à la diagonale noire et 2 points grâce à la colonne rose. Ce qui fait un total de 17 points

Cette fonction d'évaluation assez simple à mettre en
œuvre reflète pour un état de jeu donné le nombre d'
opportunités de victoire du joueur. Elle est donc
adaptée pour un algorithme minimax qui va chercher
à favoriser les états de jeu menant à la victoire.

## Algorithme minimax

 Notre algorithme minimax passe en revue toutes les possibilités pour un nombre limité de coups (dépendant de la profondeur, élément passé en paramètre) et à leur assigner une valeur correspondant au score. Il va chercher à maximiser le score du joueur qui joue le coup et minimiser celui de son adversaire. On utilise l'élagage alpha-bêta pour optimiser la recherche du meilleur coup en limitant le nombre de nœuds visités dans l'arbre de jeu.

## Structure du code

Au niveau des fichiers notables :
- game_manager vérifie si un coup est gagnant
- entities regroupe les méthodes liées au joueur et au plateau
- heuristics contient le calcul du score
- strategies contient l'algorithme minimax, et également une stratégie aléatoire utilisée au début pour tester notre modélisation

## Organisation

Pour l'organsation au sein de l'équipe, étant donné que la modélisation du plateau et le calcul du coup à jouer sont interdépendants, nous avons travaillé tous les 3 dessus en même temps avec du pair-programming. Cela nous a permis de pouvoir avoir un feedback en direct et donc de prendre les meilleurs décisions au niveau de la logique du code ainsi que l'implémentation. Une fois le calcul du coup et la modélisation terminées, nous nous sommes occupés de l'API avec le framework fastAPI, qui nous a permi d'avoir une API assez simple au vu des consignes asses basiques pour l'utilisation de cette dernière. Cette méthode de travail a aussi permi que chaque membre du groupe puisse travailler sur toutes les parties, et donc apporter son expérience ou gagner en compétence.