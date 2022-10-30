import time
from random import randint

def flip_your_destiny():
    while True:
        print('Do u want to throw these cubes?')
        answer = str(input())
        if answer.lower() == "yes" or answer.lower() == "yeah":
            time.sleep(6)
            print('Destiny do:', randint(1,6), 'and', randint(1,6))
        elif answer.lower() == 'no':
            print('OK')
            break
        else:
            break

def main():
    flip_your_destiny()

if __name__ == "__main__":
  main()
