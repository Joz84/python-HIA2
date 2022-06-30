false_sentence = "B0nj0ur Par15"

# Solution 1

# result = false_sentence.replace("0", "o")
# result2 = result.replace("1", "i")
# result3 = result2.replace("5", "s")
# print(result3)


# Solution 2
# Dictionnary
dict = {"0": "o", "1": "i", "5": "s", "@": "a" }
print(dict["0"])

result = false_sentence
for number, letter in dict.items():
  # la 1ere fois: number = "0" et letter = "o"
  # la 2eme fois: number = "1" et letter = "i"
  # la 3eme fois: number = "5" et letter = "s"
  print(number + " => " + letter )
  result = result.replace(number, letter)

print(result)

