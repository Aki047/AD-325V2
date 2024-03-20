"""
write a program that examines an array of different animals and determines
how many of them have exactly four legs, simulating a real-world coding
interview scenario."""

"""
What if array empty
is it case sensitive
if no fourlegged animals what is return
do we need to account for specific category of animals
if so scaleablity for other leg counts

Sample Arrays

Input: animals = ['lion', 'monkey', 'deer', 'snake', 'elephant']
List of Animals and Their Leg Counts:
Animals with Four Legs: 'lion', 'deer', 'elephant', 'horse', 'dog', 'cat'
Animals with Two Legs: 'monkey', 'parrot', 'ostrich'
Animals with No Legs: 'snake', 'worm'
Animals with Multiple Legs (more than four): 'spider', 'ant', 'centipede'
"""
def howManyLegs(animals, four_Legs):
    if not animals:
        raise ValueError("The input array is empty. Please provide a non-empty array.")

    animalCount = 0
    has_four_legged_animal = False  # Flag to check if at least one four-legged animal is found

    for animal in animals:
        if animal in four_Legs:
            animalCount += 1
            has_four_legged_animal = True

    if not has_four_legged_animal:
        print("There are no four-legged animals in the array.")

    return animalCount



animals = ['lion', 'monkey', 'snake', 'deer', 'elephant']
four_Legs = ['lion', 'deer', 'elephant', 'horse', 'dog', 'cat']
two_Legs = ['monkey', 'parrot', 'ostrich']
zero_Legs =['snake', 'worm']
multiple_Legs = ['spider', 'ant', 'centipede']


