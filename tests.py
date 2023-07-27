import pandas as pd
from pandas import Index

# recupérer la fonction qui crée le dataframe
from app import create_dataframe

# NB: 
# pour faire des tests unitaires, il vaut mieux 
# utiliser des bibliothèques dédiées comme
# unittest et pytest

# vérifier un certain nombre d'assertions

# verify the create_dataframe method works as expected
df = create_dataframe()

# test du pauvre pour verifier que l'objet créé est effectivement un objet de type dataframe
assert str(type(df)) == "<class 'pandas.core.frame.DataFrame'>"

# test du pauvre pour verifier que j'ai bel et bien les colonnes désirées
assert list(df.columns) == ["Pays", "Président"]

# on peut tester plein d'autres choses
assert df.shape == (4, 2)

# ???
