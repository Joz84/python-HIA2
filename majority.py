def majority(age):
  # Si l'age est supérieur ou égale à 18
    # alors écrire "Cheers!"
  # Sinon
    # Afficher "tu n'est pas sur le bon site, amani"

  if age >= 18:
    return"Cheer!"
  else:
    return "Tu n'est pas sur le bon site, Amani!"



############# Les Tests du pauvres #######

print(majority(17) == "Tu n'est pas sur le bon site, Amani!")
print(majority(38) == "Cheers!")
print(majority(76) == "Cheers!")
