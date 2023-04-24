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
seulement ses jetons sont présents dans la rangée. On
augmente de 5 points pour 3 jetons présents et de 2
points pour 2 jetons. On augemente aussi le score de
3 points pout chaque jeton présent dans la rangée
centrale, considérée comme plus stratégique.

Cette fonction d'évaluation assez simple à mettre en
œuvre reflète pour un état de jeu donné le nombre d'
opportunités de victoire du joueur. Elle est donc
adaptée pour un algorithme minimax qui va chercher
à favoriser les états de jeu menant à la victoire.

## Algorithme minimax

// TODO

## Pistes d'amélioration