import collections

#checks if there are no Start states or too many
#checks if there are no Finish states
#checks if states and words from transitions are either missing or not in the states and words sections

error = []
words = []
states = collections.defaultdict(list)
trans = []
start = -1
finish = []
okay_t = 0
okay_s = 0

def citeste():
    where = 0
    global start
    with open('input.txt', 'r') as reader:
        for line in reader:
            #print(line, end='')
            input = line.split()

            if input[0] == "End":
                 where = 0;

            if where == 1:
                words.append(input[0])

            if where == 2:
                input[0] = input[0].replace(',', '')
                if input[0] in states.keys():
                    error.append(1);
                else:
                    if len(input) == 2:
                        states[input[0]] = input[1]
                        if input[1] == 'S':
                            start = input[0]
                        elif input[1] == 'F':
                            finish.append(input[0])
                    elif len(input) == 3:
                        input[1] = input[1].replace(',', '')
                        states[input[0]].append(input[1])
                        states[input[0]].append(input[2])
                    else:
                        states[input[0]] = ""

            if where == 3:
                input[0] = input[0].replace(',', '')
                input[1] = input[1].replace(',', '')
                trans.append(input)

            if input[0] == "Sigma:":
                where = 1;
            if input[0] == "States:":
                where = 2;
            if input[0] == "Transitions:":
                where = 3;
            #print(input)

def afiseaza():
    print(words)
    print(states)
    print(trans)
    print(start)
    print(finish)

def verifica_states():
    s_cnt = 0
    f_cnt = 0
    cnt = 0
    ok=1
    global okay_s
    for i in states:
        cnt = cnt+1
        for value in states[i]:
            if value == "S":
                s_cnt= s_cnt + 1
                if s_cnt > 1:
                    ok=0
                    print("Too many 'Start' states. Check line " + str(cnt) + " of the States input.")
                    okay_s = 0
            if value == "F":
                f_cnt= f_cnt + 1

    if s_cnt ==0:
        print("There is no 'Start' state")
        ok=0
        okay_s = 0
    if f_cnt == 0:
        print("There is no 'Finish' state")
        ok=0
        okay_s = 0
    if ok==1:
        okay_s = 1
        print("The 'States' section is valid.")

def verifica_tranzitie():
    ok=1
    okay=1
    cnt = 0
    global okay_t
    for linie in trans:
        cnt= cnt +1
        if len(linie) !=3:
            Print("Line "+str(cnt)+ " of the Transitions input doesn't have enough terms.")
            ok=0
            okay_t = 0
        elif (linie[0] not in states ) or (linie[2] not in states) or (linie[1] not in words):
            print("A state or word from line " + str(cnt) + " of the Transitions input is invalid.")
            okay_t = 0
            okay=0

    if ok==1 and okay ==1:
        print("The 'Transitions' section is valid.")
        okay_t = 1

import sys
def verifica():
        #cuvant = input()
        cuvant = str(sys.argv[1])
        stare = str(start)
        litera = 0
        okay = 1
        eroare = 0
        while (stare not in finish or litera<len(cuvant)) and okay == 1 :
            continua = 0
            if cuvant[litera] not in words:
                eroare = 1
            for linie in trans:
                if linie[1] == cuvant[litera] and str(linie[0]) == str(stare) and continua == 0:
                    #print("found " + cuvant[litera-1])
                    #print("states " + stare +" " + linie[2])
                    stare = linie[2]
                    litera= litera + 1
                    continua = 1

                if continua == 1:
                    break

            if continua == 0:
                okay = 0
                if eroare == 1:
                    print("Word is not valid, contains letters not found in 'Sigma'.")
                else:
                    print("Word is not valid, transition doesn't exist.")

        if okay == 1:
            print("Word is valid.")

if __name__ == '__main__':
    #funtion to read and memorise the data input
    citeste()
    #funtion to display the data input
    #afiseaza()
    print()
    verifica_states()
    verifica_tranzitie()
    if okay_t == 1 and okay_s == 1:
        verifica()
    else:
        print("Sections not valid, cannot check input.")