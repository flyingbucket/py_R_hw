dream_attractions = []
while True:
    dream_attraction = input("If you could visit one place in the world, where would you go? ")
    dream_attractions.append(dream_attraction)
    repeat = input("Would you like to continue? (yes/no) ")
    if repeat == "no":
        break
print("The survey results are as follows:")
for dream_attraction in dream_attractions:
    print(dream_attraction)