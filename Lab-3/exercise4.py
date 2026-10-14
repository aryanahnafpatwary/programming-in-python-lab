a=input("Enter a character: ")
print(a)
if len(a)<=1 and 'a'<=a<='z' or 'A'<=a<='Z':
    match a:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print(a, "is a Vowel")
        case 'A' | 'E' | 'I' | 'O' | 'U':
            print(a, "is a Vowel")
        case _:
            print(a, "is a Consonant") 
else:
    print("Invalid Input")