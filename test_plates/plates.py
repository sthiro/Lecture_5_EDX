# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# Assume that any letters in the user’s input will be uppercase. 

def main():

    plate = input("Plate: ")
    if is_valid(plate): #is_valid going to return bool value
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s == "": return False

    elif length_check(s) and first_2_letter_check(s) and number_middle_check(s) and no_punctuation_space_check(s): #I created function for all type of check
        return True
    else:
        return False


def length_check(plate): 

    if 2 <= len(plate) <= 6: # Check whether plate is in correct range of length
        return True
    else:
        return False

def first_2_letter_check(plate): # THCXXX

    first_2_letter = plate[0:2] # Slice first two value of plate string

    if first_2_letter[0].isalpha() and first_2_letter[1].isalpha(): #Checks whether first and second char are letter
        return True # if there is no number
    
    else: return False #If there is number
    
def no_punctuation_space_check(plate):

    return plate.isalnum()

def number_middle_check(plate):
    # Itereate each element in that string and check whether it contains number or not.
    # When iterating if there is number check remaining character are number or not

    sliced_plate = plate[2:-1] # Slice it using [2:-1], it doesnt include first, second and last element. Because we dont need to check that whether it's number or not

    for char in sliced_plate: # Iterates for each element in the sliced string

        if char.isdigit(): # Detects number
            # Note: return => Return value, break the loop and exit the function
                    
            index_for_first_detected_number = plate.index(char) # Returns the index of the first occurrence of the detected number. 
            remaining_str = plate[index_for_first_detected_number:]

            if char == "0":  return False # Number starts with 0
            
            if remaining_str.isdecimal(): #Return True or False by check if number isn't in the middle
                return True # Number is not in the middle
            else: 
                return False #Number is in the middle

    return True # Return True if there is no number in the middle 


if __name__ == "__main__":
    main()
