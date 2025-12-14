def main():

    while True:
        try:
            user_input = input("Fraction: ")
            percentage = convert(user_input)
            str_output = gauge(percentage)

            print(str_output)

        except (ValueError, ZeroDivisionError):
            continue

        else:
            break


def gauge(percentage):

    if percentage <= 1:
        gauge_val = "E"

    elif percentage >= 99:
        gauge_val = "F"

    else:
        gauge_val = f"{percentage}%"

    return gauge_val


def convert(fraction):

    input_list = fraction.split("/")
    x, y = float(input_list[0]), float(input_list[1])  # X / Y Format

    output = (x / y) * 100  # Calculates percentage, Raises ZeroDivisionError if y = 0

    if not (x.is_integer() and y.is_integer()) or x > y or (x < 0 or y < 0):  # ex 1.0 is integer, 4.5 isn't a integer
        raise ValueError("Invalid input !") # Rasing value error

    return round(output)  # Rounds the output percentage, it's a whole number


if __name__ == "__main__":
    main()
