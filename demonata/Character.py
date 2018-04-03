class Character:
    def __init__(self, name, hp, weapon):
        """@ReturnType Character"""
        self.___name = name        # @AttributeType String
        self.___hp = hp            # @AttributeType int
        self.___inventory = list() # @AttributeType list (of Items)
        self.___weapon = weapon    # @AttributeType Weapon

    def getName(self):
        """@ReturnType String"""
        return self.___name
        

    def setName(self, name):
        self.___name = name

    def getHP(self):
        """@ReturnType int"""
        return self.___hp

    def setHP(self, hp):
        self.___hp = hp

    def heal(self, hp):
        self.setHP(self.___hp + hp)

    def takeDamage(self, hp):
        self.setHP(self.___hp - hp)

    def getWeapon(self):
        """@ReturnType Weapon"""
        return self.___weapon

    def isDead(self):
        """@ReturnType boolean"""
        return self.___hp <= 0
