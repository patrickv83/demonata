"""Main game file"""
from src.controller import Controller

def main():
    print "Welcome to Demonata\n"
    gc = Controller()
    gc.start()

if __name__ == "__main__":
    main()
