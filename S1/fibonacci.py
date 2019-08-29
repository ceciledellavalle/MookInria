# -*- coding : utf-8 -*-

#
from argparse import ArgumentParser
#
#

def fibonacci(n):
    """retourne le nombre de fibonacci pour l'entier n"""
    # pour les petites valeurs de n il n'y a rien à calculer if n <= 1:
    if n <=1 :
        return 1
    # sinon on initialise f1 pour n-1 et f2 pour n-2 f2, f1 = 1, 1
    # et on itère n-1 fois pour additionner
    i =2
    f1, f2 = 1, 1
    while i < n+1 :
        i +=1
        f2, f1 = f1, f1 + f2 
     # le résultat est dans f1
    return f1

parser = ArgumentParser()
parser.add_argument(dest="entier", type=int, help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier

print(f"fibonacci({entier}) = {fibonacci(entier)}")