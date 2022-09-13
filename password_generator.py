import random

longueur = int(input("Quelle est la longueur du mot de passe?"))
selection = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\()*+,-./:;<=>?@[\]^_`{|}~'

mdp = "".join(random.sample(selection, longueur))

print(mdp)