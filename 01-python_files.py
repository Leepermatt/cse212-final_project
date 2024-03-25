# Queue Example

print('Good Morning! What food did you put in your pantry')
print("Hit enter after each food added, press 'r' to remove and 'q' to quit")
pantry = []
while True:
    data = input()
    if str.lower(data) =="q":
        break
    elif str.lower(data) =="r":
        print("Removing:", pantry.pop(0))
    else:
        pantry.append(data)
    print(pantry)
print("You have the following food in your pantry:")
for food in pantry:
    print(food)



