x=str(input("Enter letter"))
vowels=("a","A","e","E","i","I","o","O","u","U")
for i in vowels[9]:
    if(vowels[x]==vowels[i]):
        print("Character is a vowel")
    else:
        i=i+1
