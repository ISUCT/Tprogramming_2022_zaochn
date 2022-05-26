a = []
print(a)
a = [1,2,3,"some", "another", [5,6,"inner"], "last"]
print(a)
print(a[0])
print(a[6])
print(a[5])
print(len(a))
print(a[len(a)-1])
print(a[-1])
print(a[:3])
print(a[3:-1])
print(a[3:])

some = a[5]
print(some[-1])

print(a[5][-1])

some = [1,2,3]
copy = []
for item in some:
    copy.append(item)
some.append("added")
print(some)
print(copy)

sample = { "Russia": {
            "capital": "Moscow"
            },
        "UK": {
            "capital": "London",
            "population": 20000
        }
}
print(sample["Russia"])
print(sample["UK"]["population"])