age = int(input("How old are you?"))

if age < 20:
    print("You can't drink.")
elif age >= 20 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")
