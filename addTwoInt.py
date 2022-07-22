#!/usr/bin/env python

import sys

def add_num(a,b):
    sum=a+b;
    return sum;

numa = input("Entrez la premiere valeur:")
numb = input("Entrez la deuxieme valeur:")
print("La somme est : ",add_num(numa,numb))
print(sys.argv)



if len(sys.argv) > 3 :
        print('Vous avez renseigne plus de 2 parametres')
        conti = 0



if len(sys.argv) < 3 :
         print('Vous avez renseigne moins de 2 parametres')
         conti = 0


