a = input()
b = input()
if a != "красный" and a != "желтый" and a != "синий" or b != "красный" and b != "желтый" and b != "синий":
    print("Ошибка")
elif a == "красный" and b == "желтый" or b == "красный" and a == "желтый":
    print ("оранжевый")
elif a == "красный" and b == "синий" or b == "красный" and a == "синий":
    print("фиолетовый")
elif a == b:
    print (a)
else:
    print("зелёный")