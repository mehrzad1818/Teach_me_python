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
