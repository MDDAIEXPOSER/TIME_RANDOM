from random import randint
import time 
def main():
    while True:
        print('Delete from arena?')
        solution = str(input())
        if solution.lower() == 'yes':
            time.sleep(120)
        elif solution.lower() == 'no':
            continue
        else:
            break
if __name__ == "__main__":
  main()
