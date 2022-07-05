import string

def same_case(a, b):
  alphabet = list(string.ascii_lowercase + string.ascii_uppercase)

  if a not in alphabet or b not in alphabet:
    return -1
  elif a+b in [(a+b).upper(), (a+b).lower()]:
    return 1
  else:
    return 0

print(same_case("a", "A") == 0)
print(same_case("a", "b") == 1)
print(same_case("a", "?") == -1)
print(same_case("%", "C") == -1)
print(same_case("x", "B") == 0)
