def add_saluation(sentence):
  salutation = "Bonjour "
  new_sentence = salutation + sentence
  return new_sentence


sentence1 = "Leve toi!"
sentence2 = "Donne moi le pain"
sentence3 = "Passe niveau 3 sur codewars"

# salutation = "Bonjour "
# new_sentence1 = salutation + sentence1
# new_sentence2 = salutation + sentence2
# new_sentence3 = salutation + sentence3

new_sentence1 = add_saluation("Leve toi!")
new_sentence2 = add_saluation(sentence2)
new_sentence3 = add_saluation(sentence3)


print(new_sentence1)
print(new_sentence2)
print(new_sentence3)
