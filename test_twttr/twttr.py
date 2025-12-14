# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase.
# Vowel => {A,E,I,O,U}


def main():

    s =  input("Input: ")
    output = shorten(s) #Input the str
    print(output)

def shorten(word):

    shorten_str = ""
    for c in word:
        if c.casefold() not in ["a", "e", "i", "o", "u"]: # Checks whether lower case of each iterated charecter isn't a vowel
            shorten_str += c

    return shorten_str


if __name__ == "__main__":
    main()
