import random


class Player:
    def __init__(self):
        self.health = 100
        self.strength = 3
        self.defence = 3

    def get_damage(self, damage,  strength):
        damage_dealt = (damage + strength - self.defence)
        self.health -= damage_dealt
        print(f"Gracz otrzymał {damage_dealt} obrażeń.")
        print(f"Zostało mu {self.health} życia.")


class Enemy:
    def __init__(self):
        self.health = 500
        self.strength = 20
        self.defence = 4

    def get_damage(self, damage, strength):
        damage_dealt = (damage + strength - self.defence)
        self.health -= damage_dealt
        print(f"Przeciwnik otrzymał {damage_dealt} obrażeń.")
        print(f"Zostało mu {self.health} życia.")


class Dice:
    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    @staticmethod
    def roll_for_damage():
        roll = Dice.roll_dice()
        player_damage = roll
        while roll == 6:
            roll = Dice.roll_dice()
            player_damage += roll
        return player_damage


def fight(player, enemy):
    player_damage = Dice.roll_for_damage()
    enemy.get_damage(player_damage, player.strength)
    if enemy.health <= 0:
        return player
    enemy_damage = Dice.roll_for_damage()
    player.get_damage(enemy_damage, enemy.strength)
    if player.health <= 0:
        return enemy
    return False


def game():
    player = Player()
    enemy = Enemy()
    fight_result = fight(player, enemy)
    while not fight_result:
        fight_result = fight(player, enemy)
    if fight_result == player:
        print("Brawo! Wygrałeś!")
    else:
        print("Przegrałeś głupi hujcu!")


if __name__ == "__main__":
    game()
