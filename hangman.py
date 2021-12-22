PICS = [
    """
    +---+
        |
        |
        |
       ===
    """,
    """
    +---+
    0   |
        |
        |
       ===
    """,
    """
    +---+
    0   |
   /    |
        |
       ===
    """,
    """
    +---+
    0   |
   /|   |
        |
       ===
    """,
     """
    +---+
    0   |
   /|\  |
        |
       ===
    """,
     """
    +---+
    0   |
   /|\  |
   /    |
       ===
    """,
     """
    +---+
    0   |
   /|\  |
   / \  |
       ===
    """,
]

words = "ана шеше апа әке көке ата әже жезде жеңге аға іні қарындас сіңілі нағашы бауыр ағайын жекжат құда келін".split()

"""
1.Программа бір құпиясөзді тізім ішінен таңдап алып жасырсын
2.Ойынның қазіргі жағдайын сипаттайтын суретті шығарсын. Дұрыс терілген әріптерді және дұрыс емес терілген әріптерді де шығарсын.
3.Қолданушы енгізіп жатқан ақпаратты тексерсін.
4.Ойынның аяқталғанын немесе аяқталмағанын тексеру қажет
5.Егер ойын аяқталған болса, онда қолданушыдан жалғастыруды сұрау

"""

import random

def choose_security_word(words_list):
    index = random.randint(0, len(words_list)-1)
    return words_list[index]
def draw_board(wrong_letters, correct_letters, security_word):
    print(PICS[len(wrong_letters)])
    print("Қате терілгендер -->", wrong_letters)
    blank = '-'*len(security_word)
    for index in range(len(security_word)):
        if security_word[index] in correct_letters:
            blank = blank[:index] + security_word[index] + blank[index+1:]
    print("Дұрыс терілгендер -->", blank)

def get_answer(already_answered):
    
    while True:
        answer = input().lower()
        if len(answer) !=1:
            print("Тек бір әріп теру қажет")
            print("Қайта енгізіңіз")
            continue
        elif answer not in 'аәбвгғджзийкқлмноөпрстуұүфхцчһыішще':
            print("Тек қазақша әріп теріңіз")
            print("Қайта енгізіңіз")
            continue
        elif answer in already_answered:
            print("Бұл әріпті бұрын таңдап қойғансыз")
            print("Қайта енгізіңіз")
            continue
        else:
             return answer

def game_continue():
    answer = input("Ойынды тағы ойнаймыз ба? (иә/жоқ)").lower()
    if answer.startswith('и'):
        return True
    else:
        return False

def main():
    qupia_soz = choose_security_word(words)
    durys_tabylgandar = ""
    qate_tabylgandar = ""

    game_ended = False
    
    while True:
         draw_board(qate_tabylgandar, durys_tabylgandar, qupia_soz)
         already_found = True
         for index in range(len(qupia_soz)):
             if qupia_soz[index] not in durys_tabylgandar:
                 already_found = False
                 break 

         if already_found:
             print("Құттықтаймыз!! Сіз жеңімпазсыз!")
             game_ended = True
         elif len(qate_tabylgandar) == len(PICS)-1:
            print("Өкінішті! Сіз ұтылдыңыз!")
            game_ended =True
         else: 
            letter = get_answer(durys_tabylgandar + qate_tabylgandar)
            if letter in qupia_soz:
                durys_tabylgandar += letter
            elif letter not in qupia_soz:
                qate_tabylgandar += letter

         if game_ended:
             draw_board(qate_tabylgandar, durys_tabylgandar, qupia_soz)
             if game_continue():
                 qupia_soz = choose_security_word(words)
                 durys_tabylgandar = ""
                 qate_tabylgandar = "" 
                 game_ended = False
             else:
                break

if __name__ == '__main__':
    main()