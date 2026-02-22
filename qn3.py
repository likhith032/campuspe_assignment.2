a= input("Enter a sentence: ")
print("Original :", a)
print("Characters (without spaces) :", len(a.replace(" ", "")))
print("UPPERCASE :", a.upper())
print("lowercase :", a.lower())
print("Characters (with spaces) :", len(a))
words = a.split()
print("Words :", len(words))
print("Title Case :", a.title())
if len(words) > 0:
    print("First word :", words[0])
else:
    print("First word : None")
if len(words) > 0:
    print("Last word :", words[-1])
else:
    print("Last word: None")
print("Reversed :", a[::-1])