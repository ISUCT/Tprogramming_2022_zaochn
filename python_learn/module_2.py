a = 5
b = 6
print(a >= b)

print(True or False)

if a > 10:
    print("a > 10")
elif a == 5:
    print("a == 5")
    print("Additional")
elif a > 5:
    print("a > 5")
else:
    print("a is not defined")

if a == 5:
    print("a == 5")
    print("Additional")
if a > 10:
    print("a > 10")
if a > 5:
    print("a > 5")
else:
    print("a is not defined")

language = "english"
daytime = "asdf"

if language == "english":
    print("English")
    if daytime == "morning":
        print("Good morning")
        if a == 5:
            print("a == 5")
    else:
        print("Good evening")

i = 0
while i < 3:
    print(f"i={i}")
    i += 1
    print("action in while")
print("action after while")

for i in "string":
    print(i)

for i in range(1, 5):
    print(i)

for i in  range(1,10):
    for j in range(1,10):
        mul = i * j
        print(f"{i} x {j} = {mul}")
    print("--------------------")