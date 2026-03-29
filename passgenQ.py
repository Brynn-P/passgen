import secrets
import string
import sys

def passwords():

    while True:
        pas_length = input("How long would you like your password to be?\nMust be 16 or higher\nType 1 to exit:\n")

        if pas_length == "1":  # check for exit first
            sys.exit()

        try:
            pas_len = int(pas_length)
            if pas_len < 16:
                print("This is not advised, passwords should be 16 or greater!")
                continue  # back to input
        except ValueError:
            print("Come now, we said numbers, what are you trying?")
            continue  # back to input

        # Character sets
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        digit = string.digits
        punct = string.punctuation

        # Ensure at least one character from each category
        pass_char = [
            secrets.choice(upper),
            secrets.choice(lower),
            secrets.choice(digit),
            secrets.choice(punct)
        ]

        all_char = upper + lower + digit + punct

        # Fill remaining length
        for _ in range(pas_len - 4):
            pass_char.append(secrets.choice(all_char))

        secrets.SystemRandom().shuffle(pass_char)
        return ''.join(pass_char)


if __name__ == "__main__":
    print(passwords())