# import sys
import argparse
import random
import string

def password_generator(length=8, upper=False, lower=False, digit=False, punc=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits
    if punc:
        pool += string.punctuation
    if pool == '':
        pool += string.ascii_letters
        pool += string.digits
    password = ''.join(random.sample(pool, k=length))
    '''
    if password.isalpha() or password.isdigit() :
        print("Invalid password, Let's create another one!")
        password_generator(length)
        return password
    '''
    return ''.join(random.choices(pool, k=length))

if __name__ == '__main__':
    #print(password_generator(int(sys.argv[1])))
    parser = argparse.ArgumentParser(description="Password_Creator")
    parser.add_argument('length', type=int, help="length of password")
    parser.add_argument('-u', '--upper', help="upper case password", action="store_true")
    parser.add_argument('-l', '--lower', help="lower case password", action="store_true")
    parser.add_argument('-d', '--digit',help="digit password", action="store_true")
    parser.add_argument('-p', '--punc',help="punctuation password", action="store_true")

    args = parser.parse_args()
    print(password_generator(args.length, args.upper, args.lower, args.digit, args.punc))