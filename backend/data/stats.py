import os

def main():
    res = [0] * 27
    with open("./pli07.txt", 'r') as fichier:
        myline = fichier.readline()
        while myline:
            res[len(myline)-1] += 1
            myline = fichier.readline()
    
    return res

print(main())
