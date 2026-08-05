from abc import ABC, abstractmethod

# Characters
class Character(ABC):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    @abstractmethod
    def attack(self, opponent):
        pass

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def __str__(self):
        status = "Alive" if self.is_alive() else 'Defeated'
        return f"{self.name} | HP: {self.health} | Power: {self.power} | {status}"

    def __lt__(self, other):
        return self.power < other.power


class Warrior(Character):
    def attack(self, opponent):
        damage = self.power
        print(f"{self.name} has done {damage} damage to {opponent.name} by his sword")
        opponent.take_damage(damage)

class Mage(Character):
    def attack(self, opponent):
        damage = self.power + 10
        print(f"{self.name} has done {damage} damage to {opponent.name} by his fireball")
        opponent.take_damage(damage)

class Archer(Character):
    def attack(self, opponent):
        damage = self.power - 5
        print(f"{self.name} has done {damage} damage to {opponent.name} by his arrow")
        opponent.take_damage(damage)


# Weapons
class Weapon:
    def __init__(self, name, bonus_damage):
        self.name = name
        self.bonus_damage = bonus_damage

    def __str__(self):
        return f"{self.name} (+{self.bonus_damage} damage)"

class Warrior(Character):
    def __init__(self, name, health, power, weapon):
        super().__init__(name, health, power)
        self.weapon = weapon    # Warrior HAS-A Weapon

    def attack(self, opponent):
        damage = self.power + self.weapon.bonus_damage
        print(f"{self.name} has done {damage} damage to {opponent.name} by {self.weapon.name}")
        opponent.take_damage(damage)


sword = Weapon('Fire Sword', 15)
warrior = Warrior('Arjun', 100, 20, sword)
mage = Mage('Zara', 80, 25)

print(warrior)
print(mage)

warrior.attack(mage)
print(mage)

mage.attack(warrior)
print(warrior)

print(f"\nWhich character is more powerful? {'Mage' if warrior < mage else 'Warrior'}")