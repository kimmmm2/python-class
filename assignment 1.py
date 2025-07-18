letter = input("Enter a letter: ")
letter = letter.lower()
vowels = ['a', 'e', 'i', 'o', 'u']


if letter in vowels:
    print("it is a vowel.")
else:
    print("It is a constant.")