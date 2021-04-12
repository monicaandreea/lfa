words = []
trans = []
start = -1
finish = []

def citeste():
    cnt = 0
    global n, m, k, start
    with open('input.txt', 'r') as reader:
        for line in reader:
            cnt = cnt+1;
            input = line.split()

            if cnt == 1:
                n = int(input[0])
                m = int(input[1])

            if cnt > 1 and cnt <= m+2:
                trans.append(input)

            if cnt == m+3:
                start=int(input[0])

            if cnt == m+4:
                i = 0
                while i<int(input[0]):
                    finish.append(int(input[i+1]))
                    i=i+1

            if cnt == m+5:
                k = int(input[0])

            if cnt > m+5:
                words.append(input[0])

def verifica():
    for word in words:
        traseu = []
        litera = 0
        okay = 1
        stare = start
        traseu.append(stare)
        while (int(stare) not in finish or litera < len(word)) and okay == 1:
            continua = 0
            for linie in trans:
                if linie[2] == word[litera] and (linie[0]) == str(stare) and continua == 0:
                    stare = linie[1]
                    traseu.append(stare)
                    litera = litera + 1
                    continua = 1

                if continua == 1:
                    break

            if continua == 0:
                okay = 0
                print("NU")

        if okay == 1:
            print("DA")
            print("Traseu:", end=" ")
            print(*traseu)


def afiseaza():
    print(n)
    print(m)
    print(trans)
    print(start)
    print(finish)
    print(words)

if __name__ == '__main__':
    citeste()
    #afiseaza()
    verifica()
