from time import time

def playing_chess(solutions):
   count_of_start = time()
   while time() - count_of_start < 1800:
       if solutions.lower() != 'off':
          print('Время затраченное на ход:',round(time() - count_of_start, 2))
          print('Оставшееся время:', (30 -  round((time() - count_of_start) / 60, 2)))
       else:
          break

def main():
    playing_chess(input())

if __name__ == "__main__":
    main()
