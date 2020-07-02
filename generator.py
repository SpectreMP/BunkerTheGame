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
characteristicsList = [professions,healthStates,hobbies,phobias,additionalInfos,bagages,traits,specialConditions]

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
    age = int(random.normalvariate(40,15))
    if age<14:
        age+=10
    age=str(age)
    if random.randint(0,100)<15:
        if sex=="Мужской":
            age+=", гомосексуалист"
        else:
            age+=", лесбиянка"
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
    characterFile.write("Багаж: "+bagage+"\n\n\n")
    characterFile.write("Карты специальных условий:\n1."+specialCondition[0]+"\n2."+specialCondition[1]+"\n")
    characterFile.write("---------------------------------------------\n")
    characterFile.write("              ПРАВИЛА ИГРЫ:\n")
    characterFile.write("1. На первом ходу открывается 3 характеристики (Профессия + 2 любые на выбор). Далее - по одной каждый новый круг.\n")
    characterFile.write("2. 1 характеристика - 1 строчка\n")
    characterFile.write("3. Разрешено никого не выгонять на голосовании. Тогда на следующем круге придётся выгнать двоих.\n")
    characterFile.write("4. Время на описание персонажа и его оправдание - 60 секунд.\n")
    characterFile.write("5. Женщина остаётся плодовитой до 49 лет. Мужчина ограничений по возрасту не имеет.\n")
    characterFile.write("6. Характеристики и карты специальных условий не повторяются.\n")
    characterFile.write("7. Если карта специальных условий была озвучена, она будет применена автоматически\n")
    characterFile.write("8. Игрок может использовать карты специальных условий в любой момент времени от начала игры и до объявления ведущим о его выбывании.\n")
    characterFile.write("9. Карты специальных условий могут быть использованны лишь единожды за игру.\n")
    characterFile.write("10. Если вы не можете назвать своего персонажа геем/лесбиянкой по этическим причинам, назовите его \"Чайлдфри\"")
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
    print("3 - Сгенерировать новую характеристику")
    print("4 - Создать катастрофу")
    print("5 - Перемешать имеющиеся характеристики")
    print("6 - Закрыть программу")
    answer = input("Введите цифру: ")
    if answer == "1":
        characteristicsLength()
    elif answer == "2":
        for i in range(int(input("Сколько персонажей вы хотите создать?: "))):
            createCharacter("player"+str(i+1))
    elif answer == "3":
        print ("Какую характеристику сгенерировать?\n1. Возраст и половая ориентация\n2. Профессия\n3. Состояние здоровья\n4. Хобби\n5. Фобия\n6. Дополнительная информация\n7. Багаж\n8. Человеческая черта\n9. Карта специальных условий")
        rewritefile = open("game/rewrited.txt","w",encoding="utf-8")
        answer = int(input("Введите число: "))
        
        if answer == 1:
            age = int(random.normalvariate(40,15))
            if age<14:
                age+=10
            age = str(age)
            if random.randint(0,100)<15:
                age+=", гомосексуален(а)"
            rewritefile.write(age)
        elif answer == 3:
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
            rewritefile.write(healthState)
        else:
            rewritefile.write(characteristicsList[answer-2].pop())
        rewritefile.close()
    elif answer == "5":
        reshuffleCards()
    elif answer == "6":
        break