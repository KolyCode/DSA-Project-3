#import everything from the other files (doing this to make the code cleaner & more readable)
from map_creation import *

def main():
    for i in range(0,100):
        print(i+631)
        create_map()

#calls the main function
if __name__ == '__main__':
    main()