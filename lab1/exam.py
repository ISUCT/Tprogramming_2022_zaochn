ninjas = int(input("введите количество врагов:"))
if (ninjas <= 10):
  print("Я одолею этих ниндзя!")
elif (ninjas >= 30):
  print("Их слишком много")
elif (ninjas < 30 or ninjas >= 10):
  print("Будет непросто, но я с ними разделаюсь")