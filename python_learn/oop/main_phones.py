import phone
import cellfhone

phone1 = phone.Phone("Samsung")
phone2 = phone.Phone("Android", 3)

phone1.age = 10
print(phone1.age)
phone2.age = -10

phone2.set_age(350)
age = phone2.get_age()
print(age)

print(phone2.name)

phone1.call("12-34-54")
phone2.call("22-33-44")
phone1.accept_call()

cell1 = cellfhone.CellPhone("Nokia", 5)

print(cell1.age)
cell1.call("33-33-33")

cell1.decline_call()