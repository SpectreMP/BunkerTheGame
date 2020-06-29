import random
#library
professions = open("professions.txt","r",encoding="utf-8").read().split(",")
healthStates = open("healthStates.txt","r",encoding="utf-8").read().split(",")
hobbies = open("hobbies.txt","r",encoding="utf-8").read().split(",")
phobias = open("phobias.txt","r",encoding="utf-8").read().split(",")
additionalInfos = open("additionalInfos.txt","r",encoding="utf-8").read().split(",")
bagages = open("bagages.txt","r",encoding="utf-8").read().split(",")
traits = open("traits.txt","r",encoding="utf-8").read().split(",")
specialConditions = open("specialConditions.txt","r",encoding="utf-8").read().split(",")

def reshuffleCards():
    random.shuffle(professions)
    random.shuffle(healthStates)
    random.shuffle(hobbies)
    random.shuffle(phobias)
    random.shuffle(additionalInfos)
    random.shuffle(bagages)
    random.shuffle(traits)
    random.shuffle(specialConditions)

def createCharacter(filename):
    if random.randint(0,1):
        sex="Мужской"
    else:
        sex="Женский"
    age = str(random.randint(14,70))
    profession = professions.pop()
    
    if random.randint(0,100)>40:
        heaviness = "Лёгкой тяжести"
    elif random.randint(0,100)>40:
        heaviness = "Средней тяжести"
    else:
        heaviness = "Высшей тяжести"
    
    if random.randint(0,100)>40:
        healthState = healthStates.pop()+" "+heaviness
    else:
        healthState = "Полностью здоров"
    hobbie = hobbies.pop()
    phobia = phobias.pop()
    additionalInfo = additionalInfos.pop()
    trait = traits.pop()
    bagage = bagages.pop()
    specialCondition = [specialConditions.pop(),specialConditions.pop()]
    characterFile = open("game/"+filename+".txt","w",encoding="utf-8")
    characterFile.write("Пол: "+sex+", Возраст: "+age+"\n")
    characterFile.write("Профессия: "+profession+"\n")
    characterFile.write("Состояние здоровья: "+healthState+"\n")
    characterFile.write("Хобби: "+hobbie+"\n")
    characterFile.write("Фобия: "+phobia+"\n")
    characterFile.write("Дополнительная информация: "+additionalInfo+"\n")
    characterFile.write("Человеческая черта: "+trait+"\n")
    characterFile.write("Багаж: "+bagage+"\n")
    characterFile.write("Карты специальных условий:\n"+specialCondition[0]+"\n"+specialCondition[1])
    characterFile.close()


def characteristicsLength():
    print("\n---------------------------------------")
    print("Профессии: "+str(len(professions)))
    print("Состояния здоровья: "+str(len(healthStates)))
    print("Хобби: "+str(len(hobbies)))
    print("Фобии: "+str(len(phobias)))
    print("Дополнительные факты: "+str(len(additionalInfos)))
    print("Начальные предметы: "+str(len(bagages)))
    print("Черты характера: "+str(len(traits)))
    print("Специальные условия: "+str(len(specialConditions)))
    print("---------------------------------------\n")

reshuffleCards()

while True:
    print("Введите цифру, чтобы выбрать желаемую функцию:")
    print("1 - Вывести количество всех имеющихся характеристик")
    print("2 - Создать персонажей (Полученные характеристики будут удаленны, перезапустите программу чтобы добавить их вновь)")
    print("3 - Создать катастрофу")
    print("4 - Перемешать имеющиеся характеристики")
    print("5 - Закрыть программу")
    answer = input("Введите цифру: ")
    if answer == "1":
        characteristicsLength()
    elif answer == "2":
        for i in range(int(input("Сколько персонажей вы хотите создать?: "))):
            createCharacter("player"+str(i+1))
    elif answer == "4":
        reshuffleCards()
    elif answer == "5":
        break