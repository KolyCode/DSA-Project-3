#import everything from the other files (doing this to make the code cleaner & more readable)
from map_creation import *
from path_finding import *

def main():
    while True:
        create_maps()

#calls the main function
if __name__ == '__main__':
    main()