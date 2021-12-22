import random

print("Сәлем, есіміңізді енгізіңіз:")
name = input()
number = random.randint(1,20)
print(f"Жақсы,{name}.Біз сізге 1...20 аралығында кездейсоқ сан жасырдық")
print("Осы жасырылған санды 6 әрекеттің ішінде тауып көріңіз")
print("Сіздің ойыңызша бұл қандай сан?")

for i in range(6):
    try:
        guess = int(input())
        if guess > number:
            print("Сіз енгізген сан тым үлкен")
        if guess < number:
            print("Сіз енгізген сан тым кіші")
        if guess == number:
            break
    except ValueError:
        print("Тек бүтін санды енгізу керек")
        print("Санды қайта енгізіңіз")
        print("-"*20)
        continue
if guess == number:
    print(f"Сіз ұттыңыз! Сіз жасырынған санды {i+1} әрекеттен таптыңыз!")
if guess != number:
    print("Өкінішке орай санды 6 әрекеттің ішінде таба алмадыңыз:(")
