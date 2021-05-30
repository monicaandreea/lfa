start = 0  # starea initiala
finish = 0  # starea finala (accepted)
moves = []
tape = []


def read_turing(infile):
    global start, finish
    with open(infile) as file:
        start = file.readline().strip()
        finish = file.readline().strip()

        for line in file.readlines():
            line = line.strip()
            move = line.strip().split(',')
            if len(move) == 5:
                moves.append(move)

    return


def is_accepted(word):
    tape = list(word)
    i = 0
    st = 0
    dr = len(tape) - 1
    next = start
    poz = ">"
    while st <= dr:
        if i < st:
            if next == "qLeft1":
                next = "qSearch1R"
                #print(next)
                i = i + 1
                if int(tape[i]) == 1:
                    next = "q1"
                    st = st + 1
                    dr = dr - 1
                    i = i + 1
                    poz = ">"
                elif int(tape[i]) == 0:
                    next = "qReject"
            if next == "qLeft0":
                next = "qSearch0R"
                #print(next)
                i = i + 1
                if int(tape[i]) == 0:
                    next = "q0"
                    st = st + 1
                    dr = dr - 1
                    i = i + 1
                    poz = ">"
                elif int(tape[i]) == 1:
                    next = "qReject"

        elif i > dr:

            if next == "qRight1":
                next = "qSearch1L"
                #print(next)
                i = i - 1
                if int(tape[i]) == 1:
                    next = "q1"
                    dr = dr - 1
                    st = st + 1
                    i = i - 1
                    poz = "<"
                elif int(tape[i]) == 0:
                    next = "qReject"
            if next == "qRight0":
                next = "qSearch0L"
                #print(next)
                i = i - 1
                if int(tape[i]) == 0:
                    next = "q0"
                    dr = dr - 1
                    st = st + 1
                    i = i - 1
                    poz = "<"
                elif int(tape[i]) == 1:
                    next = "qReject"


        elif int(tape[i]) == 1 and (next == "q0" or next == "q1"):
            if poz == ">":
                next = "qRight1"
            elif poz == "<":
                next = "qLeft1"

        elif int(tape[i]) == 0 and (start == "q0" or start == "q1"):
            if poz == ">":
                next = "qRight0"
            elif poz == "<":
                next = "qLeft0"
                
        #print(next)

        while poz == ">" and (next == "qRight0" or next == "qRight1") and i<=dr:
            i = i + 1

        while poz == "<" and (next == "qLeft0" or next == "qLeft1") and i>=st:
            i = i - 1

        if st>=dr and (next == "q1" or next == "q0"):
            next = finish

        if next == finish:
            print(word, "Accepted.")
            return

        if next == "qReject":
            print(word, "Rejected.")
            return


if __name__ == '__main__':
    read_turing('input.txt')
    print(start)
    print(finish)
    print(moves)
    for word in ['101101', '100', "101010111010101"]:
        is_accepted(word)
