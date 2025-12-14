# Special Requirements => Case-insensitive, no leading whitespaces
# Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

#if the greeting starts with an “h” (but not “hello”), output $20
#use str.startswith(prefix[, start[, end]])¶


def main():

    Greeting = input("Greeting: ").strip() # No blank side in either side
    output = value(Greeting)

    print("$", output, sep = "")


def value(greeting):

    greeting = greeting.casefold() # makes the str lower case

    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith("h"):
        return 20
    else: #If there is no h in first word
        return 100


if __name__ == "__main__":
    main()