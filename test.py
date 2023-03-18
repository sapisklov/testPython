print('Привет! Это тестовая программа.')
name = input("Как тебя зовут?\n")
print("Привет,",name)
years = int(input("Сколько тебе лет ?"))
if years >= 18:
    print(name, "тебе целых", years, "лет")
elif years <= 10 and years >=5:
    print(name, "тебе всего", years, "Лет ?")
else:
    print(name, 'Как ты пишешь ???')