

print("---------Welcome To Quize Game---------")
print("---------------Have Fun---------------")
points = 0

playing = input("Do you want to play?(y/n): ").lower()
if playing != "y":
    print("Ok! bye")
    quit()
else:
    print("Okay! let's play:")

answer = input("1.What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")

answer = input("2.What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    points += 1
else:
    print("Incorrect!")
               
answer = input("3.What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!") 
    points += 1
else:
    print("Incorrect!")

answer = input("4.What does PSU stand for? ").lower()
if answer == "Power Supply unit":
    print("Correct!") 
    points += 1
else:
    print("Incorrect!")

print(f"you got {points} questions correct!")
print(f"you got {(points/4) * 100}% questions correct!")