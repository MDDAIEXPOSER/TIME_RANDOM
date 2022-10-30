from random import randint
def main():
    while True:
        print('Your track_num:')
        track_num = str(input())
        if track_num.lower() == 'off':
            break
        else:
            print('Runners:', randint(1,100))
            print('You in', randint(1,2),'run')
if __name__ == "__main__":
  main()
