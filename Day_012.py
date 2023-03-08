# This is the 12th day of Learning Python
# We will learn about Global and Local Namespaces and also Scopes

# What is Scope?

# Scope is like planting an apple tree in your house.
# If it is planted inside your garden with fences around it,
# it is you and your family which can only access it.

# But it it's on the sidewalk, it is accessed by everyone.

# This example below will illustrate the points:

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope:


def drink_potion():
    potion_strenght = 2
    print(potion_strenght)


drink_potion()
print(potion_strenght)

# When you create a new variable inside a FUNCTION, it is only available inside that function


# Global Scope

player_health = 10  # This is a global variable


def game():
    def drink_potion():
        potion_strenght = 2  # This is a local variable
        print(potion_strenght)
        print(player_health)


drink_potion()
print(player_health)

# In Python, there's no such thing as Block Scope:
if 3 > 2:
    a_variable = 10

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[5]

    print(new_enemy)


print(enemies)


# How to modify a Global Variable?
# Modifiying Global Scope

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
