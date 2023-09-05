import os


def generateArrays(matrixOrders, matrixRes, people, x, numArray, session):
    count = 1
    for i in range(x):
        matrixOrders[i] = [0] * people
        matrixRes[i] = [0] * people
        numArray[i] = count
        if i <= session - 2:
            count += 1
        elif session * 2 - 3 + people > i >= session - 2 + people:
            count -= 1
        else:
            count = session


def printMatrix(matrixOrd, matrixRes, x, people, session, name, numArray):
    for i in range(x):
        if i == 0:
            print(end="   ")
            for j in range(people):
                print("{:<15}".format(name[j]), end="")
            print("\n\n")
        print("{:<3}".format(numArray[i]), end="")
        for j in range(people):
            print("{} - {:<11}".format(matrixOrd[i][j], matrixRes[i][j]), end="")
            if j % session == 0 and j != 0: print(end=" ")
        print("\n")
        if i == session - 2 or i == session - 2 + people \
                or i == session * 2 - 3 + people or i == session * 2 - 3 + people * 2:
            print("\n")
    input()


def gameSession(session, matrixOrders, matrixRes, numArray, countSession, name, countPlayer, sumVar):
    count = countPlayer
    sumSession = numArray[countSession]
    for i in name:
        while True:
            matrixOrders[countSession][count] = int(input(f"Взятка игрока {name[count]}: "))
            if matrixOrders[countSession][count] <= numArray[countSession]:
                if i == name[-1]:
                    if matrixOrders[countSession][count] != sumSession: break
                else:
                    break
        sumSession -= matrixOrders[countSession][count]
        if count < len(name) - 1:
            count += 1
        else:
            count = 0
    count = countPlayer
    sumSession = numArray[countSession]
    for i in range(len(name)):
        var = int(input(f"Кол-во взяток игрока {name[count]}: "))
        if var == matrixOrders[countSession][count]:
            sumSession -= matrixOrders[countSession][count]
            sumVar[i] += 1
            if matrixOrders[countSession][count] == 0:
                matrixRes[countSession][count] = 5
            else:
                if matrixOrders[countSession][count] != numArray[countSession]:
                    matrixRes[countSession][count] = matrixOrders[countSession][count] * 10
                else:
                    if numArray[countSession] != 1:
                        matrixRes[countSession][count] = matrixOrders[countSession][count] * 10 * 2
                    else:
                        matrixRes[countSession][count] = matrixOrders[countSession][count] * 10
            if sumVar[i] == len(name) + (session - 1) or (len(name) + session - 1) * 2:
                matrixRes[countSession][count]
        else:
            sumSession -= var
            if var > matrixOrders[countSession][count]:
                matrixRes[countSession][count] = var
            else:
                matrixRes[countSession][count] = matrixOrders[countSession][count] * (-10)
        if count < len(name) - 1:
            count += 1
        else:
            count = 0
    if sumSession == 0:
        countSession += 1
        if countPlayer != len(name) - 1:
            countPlayer += 1
        else:
            countPlayer = 0
    else:
        print("Вы допустили ошибку")
        input()
    return [countSession, countPlayer]


def rewriteData(matrixOrders, matrixRes, name, x):
    numPlayer = -1
    namePlayer = input("Напишите имя игрока: ")
    for i in range(len(name)):
        if name[i] == namePlayer: numPlayer = i
    if numPlayer == -1: return
    gameSession = int(input("Напишите номер игровой сессии: "))
    if 0 > gameSession > x: return
    while True:
        os.system("cls")
        var = input("Изменить значение:\n"
                    "1. Взятка\n"
                    "2. Результат\n"
                    "3. Имя игрока\n"
                    "4. Выход\n"
                    ">")
        if var == "1":
            matrixOrders[gameSession-1][numPlayer] = int(input("\nЗначение: "))
        elif var == "2":
            matrixRes[gameSession-1][numPlayer] = int(input("\nЗначение: "))
        elif var == "3":
            name[numPlayer] = input("\nИмя: ")
        elif var == "4":
            break


def resultsGame(numArray, sumResults, matrixRes, name):
    for i in range(len(name)):
        sumResults[i] = 0
        for j in range(len(numArray)):
            sumResults[i] += matrixRes[j][i]
        print(f"Результат игрока {name[i]}: {sumResults[i]}")
    input()


def mainInfo():
    session = None
    people = None
    while not isinstance(session, int):
        try:
            session = int(input("Пулька: "))
            break
        except ValueError: continue
    while not isinstance(people, int):
        try:
            people = int(input("Кол-во людей: "))
            break
        except ValueError: continue
    name = []
    for i in range(people):
        name.append(input(f"Введите имя игрока {i + 1}: "))
    return [session, people, name]


def startPrint():
    print("\n\t=================\n"
          "\t|               |\n"
          "\t|   P_O_K_E_R   |\n"
          "\t|               |\n"
          "\t=================")
    input("\nНажмите на любую кнопку для начала игры...")
    os.system("cls")


def menu(matrixOrders, matrixRes, x, people, session, name, numArray, sumResults):
    countSession = 0
    countPlayer = 0
    while True:
        os.system("cls")
        print(f"Кол-во карт в игровой сессии - {numArray[countSession]}\n\n"
              "1. Вывести матрицу\n"
              f"2. Начать игровую сессию({countSession + 1})\n"
              "3. Перезаписать данные\n"
              "4. Результаты\n"
              "5. Выход")
        var = int(input(">"))
        if var == 1:
            os.system("cls")
            printMatrix(matrixOrders, matrixRes, x, people, session, name, numArray)
        elif var == 2:
            os.system("cls")
            result = gameSession(session, matrixOrders, matrixRes, numArray, countSession, name, countPlayer)
            countSession = result[0]
            countPlayer = result[1]
        elif var == 3:
            os.system("cls")
            rewriteData(matrixOrders, matrixRes, name, x)
        elif var == 4:
            os.system("cls")
            resultsGame(numArray, sumResults, matrixRes, name)
        elif var == 5:
            break


def main():
    startPrint()
    resMainInfo = mainInfo()
    session = resMainInfo[0]
    people = resMainInfo[1]
    name = resMainInfo[2]
    x = (session * 2 - 2) + people * 2
    numArray = [0] * x
    matrixOrders = [0] * x
    matrixRes = [0] * x
    sumResults = [0] * people
    sumVar = 0
    remains = 1
    generateArrays(matrixOrders, matrixRes, people, x, numArray, session)
    menu(matrixOrders, matrixRes, x, people, session, name, numArray, sumResults)


if __name__ == "__main__":
    main()
