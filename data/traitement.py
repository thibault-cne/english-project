alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def pretreament():
    res = []
    with open("words.txt", "r") as fichier:
        lines = fichier.readlines()
        n = len(lines)
        c = 0
        for line in lines:
            tmp = line.strip()

            tmp = tmp.upper()

            good_format = False

            for letter in tmp:
                if letter in alphabet:
                    good_format = True
                else:
                    good_format = False
                    break
            
            if good_format and tmp not in res and len(tmp) < 12:
                res.append(tmp)

            c += 1
            print(str((100*c)//n), end="\r")


    return res

def tri():
    res = pretreament()
    res.sort()
    with open("word_jeu.txt", "w") as fichier:
        for word in res:
            fichier.write(word+"\n")

tri()