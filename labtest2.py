# Lab test 2 Mateusz Matijuk C21473436 12-05-2023

class Hero(object):
    """Basic template for hero. Contains name, power level and health
    points attributes. Implements the punch methods and string method."""

    def __init__(self, name="", power_level=1, health_points=100):
        self.__name = name
        self.health_points = health_points
        self.power_level = power_level

    def punch(self) -> float:
        """Return the punch power, which is 2 times the heroes level"""
        return self.power_level * 2

    def __str__(self):
        hero_info = f"Name: {self.__name}\n"
        hero_info += f"Power level: {self.power_level}\n"
        hero_info += f"Health points: {self.health_points}\n"

        return hero_info


class Mage(Hero):
    """Class template for a mage. """

    def __init__(self, name="", power_level=1, health_points=100, ability_power=1):
        Hero.__init__(name="", power_level=1, health_points=100)
        self.ability_power = power_level * 1.5

    def fireball(self):
        """Return the fireball damage, which is 3 times the mages power level."""
        return self.ability_power * 2

    def heal(self):
        """Return updated health points which are increased by 20 when healed."""
        return self.health_points + 20

    def combat(self, other):
        """Method for combat"""
        if type(other) != Monster:
            """Check if other is a monster"""
            print("Hero only fights monsters.")
            return

        while self.health_points > 0 or other.health_pts > 0:
            """While loop to ensure fight till death"""
            other.health_pts = other.health_pts - Mage.fireball(self)
            print("Hero dealt ", Mage.fireball(self), " damage with fireball")
            self.health_points = self.health_points - Monster.attack(other)
            print("Monster dealt ", Monster.attack(other), " damage with attack")

            if self.health_points == 0:
                print("Hero has been slain.")
                return
            else:
                print("Monster has been slain.")


class Monster(object):
    """Class template for a monster"""

    def __init__(self, monster_name="", strength=float, health_pts=float, roar=""):
        self.monster_name = monster_name
        self.strength = strength
        self.health_pts = health_pts
        self.roar = roar

    def __str__(self):
        return f"{self.monster_name} " ":" "({self.roar})"

    @staticmethod
    def make_roar(self):
        """print the roar"""
        print(self.roar)
        return

    def attack(self):
        """return value of attack"""
        return self.strength

    def __add__(self, other):
        """merging monsters using string concatenate, overloading operators and creating new values for attributes"""
        if type(other) != Monster:
            print("You can only merge monsters.")
            return

        new_monster_name = self.monster_name + other.monster_name
        new_strength = self.strength * 2
        new_health_pts = self.health_pts + other.health_pts
        new_roar = self.roar + other.roar + '!!!'


"""Create hero and monsters"""
hero1 = Mage("Yennefer", 50, 300, 5000)
monster1 = Monster("Vampire", 10, 100, "I love blood")
monster2 = Monster("Ghost", 20, 100, "Boo")

"""Merge monster 2 and 1 to create monster 3"""
monster3 = monster1 + monster2

"""Call combat function"""
Mage.combat(hero1, monster1)
Mage.combat(hero1, monster2)
Mage.combat(hero1, monster3)

"""Check winner"""
if hero1.health_points > 0:
    print("Hero won.")
else:
    print("Hero lost.")
