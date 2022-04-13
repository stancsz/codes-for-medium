# Live Coding Vlogs 
# https://youtu.be/QAWqQtKw8Tc
import random
import secrets
import string


class StrongPassword:
    """
    - min 1 upper case letter
    - min 1 lower case letter
    - min 1 digit
    - min 1 special character
        - allow user to customize the special character
    - length has to be greater or equal to 8
    """

    def __init__(self):
        pass

    @staticmethod
    def get_strong_password(length=16,
                            min_lower=1,
                            min_upper=1,
                            min_digit=1,
                            min_special=1,
                            custom_specials=None
                            ):
        if length < 8:
            length = 8
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        digits = string.digits
        if custom_specials:
            special = custom_specials
        else:
            special = string.punctuation

        if (min_lower + min_upper + min_digit + min_special) > length:
            length = min_lower + min_upper + min_digit + min_special
            print(f"length modified to {length}")
        password = ""

        generator = [(min_lower, lower),
                     (min_upper, upper),
                     (min_digit, digits),
                     (min_special, special),
                     (length - min_lower + min_upper + min_digit + min_special, upper + lower + digits + special)
                     ]
        for item in generator:
            for i in range(item[0]):
                password += secrets.choice(item[1])
        password = list(password)
        random.shuffle(password)
        return "".join(password)


if __name__ == '__main__':
    print(StrongPassword.get_strong_password())
    print(StrongPassword.get_strong_password(custom_specials="!@#$%^&*()-=_+"))
