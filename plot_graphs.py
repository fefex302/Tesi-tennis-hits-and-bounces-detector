import csv
import matplotlib.pyplot as plt
import sys

#questo script permette di plottare 9 grafici alla volta passandogli il csv da cui generare i grafici e la label che vogliamo (0,1,2,3), con il parametro
#offset si può slittare la generazione dei grafici di un numero desiderato di righe

if(len(sys.argv) != 4):
        print('run as: "python3 sumxy.py <input.csv> <label> <offset>"')
        exit(1)

input = sys.argv[1]
label = int(sys.argv[2])
offset = int(sys.argv[3])


with open(input, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    nplots = 0
    lineno = 0
    fig, ax = plt.subplots(3,3)
    for row in reader:
        lineno += 1
        if(lineno < offset):
             continue
        if(nplots >= 9):
            break
        
        x1, y1, x2, y2, x3, y3, mx, my, b= map(float, row)

        #controllo che il label sia quello passato come parametro
        if(int(b) != label):
            continue

        p1 = (0, 0)
        p2 = (x1, y1)
        p3 = (x1 + x2, y1 + y2)
        p4 = (x1 + x2 + x3, y1 + y2 + y3)
        print(p1,p2,p3,p4)

        fig.add_subplot(3,3,nplots+1)
        plt.plot([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]])
        plt.scatter([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]])
        plt.scatter(0,0, c='red')
        plt.annotate(lineno,(0,0),color='purple')
        #plt.plot(p1,p2,p3,p4)
        #ax.set_xlim([-5, 300])
        #ax.set_ylim([-5, 300])
        #ax.annotate(str(lineno),p1)
        #ax.set_title(nplots)
        nplots += 1
    plt.show()
        
        