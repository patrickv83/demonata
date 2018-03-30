import Item
import Character
import Enemy
import Demon

def main():
  print "Welcome to Demonata"
  joe=Character("Joe", 500);
  meanJoe=Enemy(joe, 0);
  demonJoe=Demon(meanJoe);

  brownie=Enemy(Character("Suzy", 10));

if __name__ == "__main__":
    main()
