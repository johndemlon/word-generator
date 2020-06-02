#m.txt is the biggest file in there so i used it !
import random
inpat  = input("Enter The Number of Words : ")
for words in range(0, int(inpat)):
    n = 0
    limit = random.choice(range(0, 3652650))
    for l in open("m.txt","r").readlines() :
        n = n + 1
        if(n == limit):
            print(l)
            break
