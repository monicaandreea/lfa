import collections

#checks if there are no Start states or too many
#checks if there are no Finish states
#checks if states and words from transitions are either missing or not in the states and words sections

error = []
words = []
states = collections.defaultdict(list)
trans = []


def citeste():
    where = 0
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

def verifica_states():
    s_cnt = 0
    f_cnt = 0
    cnt = 0
    ok=1
    for i in states:
        cnt = cnt+1
        for value in states[i]:
            if value == "S":
                s_cnt= s_cnt + 1
                if s_cnt > 1:
                    ok=0
                    print("Too many 'Start' states. Check line " + str(cnt) + " of the States input.")
            if value == "F":
                f_cnt= f_cnt + 1

    if s_cnt ==0:
        print("There is no 'Start' state")
        ok=0
    if f_cnt == 0:
        print("There is no 'Finish' state")
        ok=0
    if ok==1:
        print("The 'States' section is valid.")

def verifica_tranzitie():
    ok=1
    okay=1
    cnt = 0
    for linie in trans:
        cnt= cnt +1
        if len(linie) !=3:
            Print("Line "+str(cnt)+ " of the Transitions input doesn't have enough terms.")
            ok=0
        elif (linie[0] not in states ) or (linie[2] not in states) or (linie[1] not in words):
            print("A state or word from line " + str(cnt) + " of the Transitions input is invalid.")
            okay=0

    if ok==1 and okay ==1:
        print("The 'Transitions' section is valid.")

if __name__ == '__main__':
    #funtion to read and memorise the data input
    citeste()
    #funtion to display the data input
    #afiseaza()
    print()
    verifica_states()
    verifica_tranzitie()
