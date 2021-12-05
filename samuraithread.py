import threading
import time

import samuraithread
from solutionthread import *


threadTime = time.time()

sayi=0
sayi2=0
topleft = []
topright = []
bottomleft = []
bottomright = []
middle = []

def vektorel(A, B):

    return [a+b for a in A for b in B]

rakamlar= '123456789'
satir= 'ABCDEFGHI'
sutun= rakamlar
kare  = vektorel(satir, sutun)
birimliste = ([vektorel(satir, c) for c in sutun] +
            [vektorel(r, sutun) for r in satir] +
            [vektorel(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
birim = dict((s, [u for u in birimliste if s in u])
             for s in kare)
iliski = dict((s, set(sum(birim[s],[]))-set([s]))
             for s in kare)



def olasi_degerler(grid):
    degerler = dict((s, rakamlar) for s in kare)
    for s,d in deger_ayir(grid).items():
        if d in rakamlar and not atama(degerler, s, d):
            return False
    return degerler



def deger_ayir(grid):

    harfler = [c for c in grid if c in rakamlar or c in '*']
    assert len(harfler) == 81
    return dict(zip(kare, harfler))



def atama(degerler, s, d):
    diger_degerler = degerler[s].replace(d, '')
    if all(eleme(degerler, s, d2) for d2 in diger_degerler):
        return degerler
    else:
        return False



def eleme(degerler, s, d):


    adimlar = open("C:/Users/Gökçe Yılmaz/Desktop/SamuraiSudokuSolver/threadadimlari.TXT", "a")

    if d not in degerler[s]:
        return degerler
    degerler[s] = degerler[s].replace(d,'')

    if len(degerler[s]) == 0:
        return False
    elif len(degerler[s]) == 1:
        d2 = degerler[s]
        if not all(eleme(degerler, s2, d2) for s2 in iliski[s]):
            return False
    for u in birim[s]:
        dplaces = [s for s in u if d in degerler[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:

            if not atama(degerler, dplaces[0], d):
                return False
    adimlar.write(str(degerler))
    adimlar.write("\n")
    adimlar.write("Thread ile harcanan zaman: " + str(time.time() - threadTime))
    adimlar.write("\n")
    adimlar.write("\n")
    return degerler


def display(degerler):
    """
    Konsolda sudoku kısımlarını yazdırma
    """
    samuraithread.sayi = samuraithread.sayi + 1

    width = 1 + max(len(degerler[s]) for s in kare)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in satir:
        print(''.join(degerler[r+c].center(width) + ('|' if c in '36' else '') for c in sutun))

        if r in 'CF': print(line)

    solution("A", degerler)
    solution("B", degerler)
    solution("C", degerler)
    solution("D", degerler)
    solution("E", degerler)
    solution("F", degerler)
    solution("G", degerler)
    solution("H", degerler)
    solution("I", degerler)
    print(samuraithread.sayi)

    print()
    samuraithread.sayi2= samuraithread.sayi2 +1

def solution(letter,vals):
    if samuraithread.sayi==1:
        i = 1
        while i < 10:
            topleft.append(vals[letter + str(i)])
            i = i + 1
    elif samuraithread.sayi==2:
        i = 1
        while i < 10:
            topright.append(vals[letter + str(i)])
            i = i + 1
    elif samuraithread.sayi==3:
        i = 1
        while i < 10:
            bottomleft.append(vals[letter + str(i)])
            i = i + 1
    elif samuraithread.sayi==4:
        i = 1
        while i < 10:
            bottomright.append(vals[letter + str(i)])
            i = i + 1
    elif samuraithread.sayi==5:
        i = 1
        while i < 10:
            middle.append(vals[letter + str(i)])
            i = i + 1





def degerler_ayristir(grid):
    "Txt dosyasından alınan değerlerin hangi satırın hangi kareye ait olduğunu ayırır"
    a = ([x[:9] for x in grid[:9]])
    a1 = str(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+a[8])
    b = ([x[9:] for x in grid[:6]] + [x[12:] for x in grid[6:9]])
    b1 = str(b[0] + b[1] + b[2] + b[3] + b[4] + b[5] + b[6] + b[7] + b[8])
    c = ([x[:9] for x in grid[12:]])
    c1 = str(c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8])
    d = ([x[12:] for x in grid[12:15]] + [x[9:] for x in grid[15:]])
    #d1 = str(d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8])
    orta = ([x[6:15] for x in grid[6:9]] + [x[:9] for x in grid[9:12]] + [x[6:15] for x in grid[12:15]])

    i=0
    j=0
    ortaa=[]
    for i in range(9):
        for j in range(9):
            ortaa.append(orta[i][j])

    i = 0
    j = 0
    dd = []
    for i in range(9):
        for j in range(9):
            dd.append(d[i][j])

    print(str(ortaa[0]+ortaa[1]))






    Thread1 = threading.Thread(target=solve(a1))
    Thread1.start()
    threadTime1 = time.time()

    a1= solve2(a1)
    b1 = solve2(b1)
    c1 = solve2(c1)

    ortaa[0]= a1[60]
    ortaa[1] = a1[61]
    ortaa[2] = a1[62]
    ortaa[9] = a1[69]
    ortaa[10] = a1[70]
    ortaa[11] = a1[71]
    ortaa[18] = a1[78]
    ortaa[19] = a1[79]
    ortaa[20] = a1[80]
    ortaa[6] = b1[54]
    ortaa[7] = b1[55]
    ortaa[8] = b1[56]
    ortaa[15] = b1[63]
    ortaa[16] = b1[64]
    ortaa[17] = b1[65]
    ortaa[24] = b1[72]
    ortaa[25] = b1[73]
    ortaa[26] = b1[74]
    ortaa[54] = c1[6]
    ortaa[55] = c1[7]
    ortaa[56] = c1[8]
    ortaa[63] = c1[15]
    ortaa[64] = c1[16]
    ortaa[65] = c1[17]




    orta1=(str(ortaa[0] + ortaa[1] + ortaa[2]+ ortaa[3]+ ortaa[4]+ ortaa[5]+ ortaa[6]+ ortaa[7]+ ortaa[8]+ ortaa[9]
               + ortaa[10]+ ortaa[11]+ ortaa[12]+ ortaa[13]+ ortaa[14]+ ortaa[15]+ ortaa[16]+ ortaa[17]+ ortaa[18]+ ortaa[19]
               + ortaa[20]+ ortaa[21]+ ortaa[22]+ ortaa[23]+ ortaa[24]+ ortaa[25]+ ortaa[26]+ ortaa[27]+ ortaa[28]+ ortaa[29]
               + ortaa[30]+ ortaa[31]+ ortaa[32]+ ortaa[33]+ ortaa[34]+ ortaa[35]+ ortaa[36]+ ortaa[37]+ ortaa[38]+ ortaa[39]
               + ortaa[40]+ ortaa[41]+ ortaa[42]+ ortaa[43]+ ortaa[44]+ ortaa[45]+ ortaa[46]+ ortaa[47]+ ortaa[48]+ ortaa[49]
               + ortaa[50]+ ortaa[51]+ ortaa[52]+ ortaa[53]+ ortaa[54]+ ortaa[55]+ ortaa[56]+ ortaa[57]+ ortaa[58]+ ortaa[59]
               + ortaa[60]+ ortaa[61]+ ortaa[62]+ ortaa[63]+ ortaa[64]+ ortaa[65]+ ortaa[66]+ ortaa[67]+ ortaa[68]+ ortaa[69]
               + ortaa[70]+ ortaa[71]+ ortaa[72]+ ortaa[73]+ ortaa[74]+ ortaa[75]+ ortaa[76]+ ortaa[77]+ ortaa[78]+ ortaa[79]
               + ortaa[80]))

    orta1 = solve2(orta1)
    dd[0] = orta1[60]
    dd[1] = orta1[61]
    dd[2] = orta1[62]
    dd[9] = orta1[69]
    dd[10] = orta1[70]
    dd[11] = orta1[71]

    d1 = (
        str(dd[0] + dd[1] + dd[2] + dd[3] + dd[4] + dd[5] + dd[6] + dd[7] + dd[8] + dd[9]
            + dd[10] + dd[11] + dd[12] + dd[13] + dd[14] + dd[15] + dd[16] + dd[17] + dd[
                18] + dd[19]+ dd[20] + dd[21] + dd[22] + dd[23] + dd[24] + dd[25] + dd[26] + dd[27] + dd[
                28] + dd[29]+ dd[30] + dd[31] + dd[32] + dd[33] + dd[34] + dd[35] + dd[36] + dd[37] + dd[
                38] + dd[39]+ dd[40] + dd[41] + dd[42] + dd[43] + dd[44] + dd[45] + dd[46] + dd[47] + dd[
                48] + dd[49]+ dd[50] + dd[51] + dd[52] + dd[53] + dd[54] + dd[55] + dd[56] + dd[57] + dd[
                58] + dd[59]+ dd[60] + dd[61] + dd[62] + dd[63] + dd[64] + dd[65] + dd[66] + dd[67] + dd[
                68] + dd[69]+ dd[70] + dd[71] + dd[72] + dd[73] + dd[74] + dd[75] + dd[76] + dd[77] + dd[
                78] + dd[79]+ dd[80]))



    Thread2 = threading.Thread(target= solve(b1))
    Thread2.start()
    threadTime2 = time.time()

    Thread3 = threading.Thread(target=solve(c1))
    Thread3.start()
    threadTime3 = time.time()

    #orta1 = str(orta[0] + orta[1] + orta[2] + orta[3] + orta[4] + orta[5] + orta[6] + orta[7] + orta[8])

    Thread4 = threading.Thread(target=solve(d1))
    Thread4.start()
    threadTime4 = time.time()

    Thread5 = threading.Thread(target=solve(orta1))
    Thread5.start()
    threadTime5 = time.time()

    Thread1.join()

    Thread2.join()

    Thread3.join()

    Thread4.join()

    Thread5.join()

    print("1. Thread ile harcanan zaman: " + str(time.time() - threadTime1))
    print("2. Thread ile harcanan zaman: " + str(time.time() - threadTime2))
    print("3. Thread ile harcanan zaman: " + str(time.time() - threadTime3))
    print("4. Thread ile harcanan zaman: " + str(time.time() - threadTime4))
    print("5. Thread ile harcanan zaman: " + str(time.time() - threadTime5))




def solve(grid):


    ans = search(olasi_degerler(grid))
    display(ans)


def solve2(grid):


    ans = search(olasi_degerler(grid))
    yeni= str(ans['A1']+ans['A2']+ans['A3']+ans['A4']+ans['A5']+ans['A6']+ans['A7']+ans['A8']+ans['A9']+ans['B1']+ans['B2']
              +ans['B3']+ans['B4']+ans['B5']+ans['B6']+ans['B7']+ans['B8']+ans['B9']+ans['C1']+ans['C2']+ans['C3']+ans['C4']
              +ans['C5']+ans['C6']+ans['C7']+ans['C8']+ans['C9']+ans['D1']+ans['D2']+ans['D3']+ans['D4']+ans['D5']+ans['D6']
              +ans['D7']+ans['D8']+ans['D9']+ans['E1']+ans['E2']+ans['E3']+ans['E4']+ans['E5']+ans['E6']+ans['E7']+ans['E8']
              +ans['E9']+ans['F1']+ans['F2']+ans['F3']+ans['F4']+ans['F5']+ans['F6']+ans['F7']+ans['F8']+ans['F9']
              + ans['G1'] + ans['G2'] + ans['G3'] + ans['G4'] + ans['G5'] + ans['G6'] + ans['G7'] + ans['G8'] + ans['G9'] + ans['H1'] + ans['H2']
              + ans['H3'] + ans['H4'] + ans['H5'] + ans['H6'] + ans['H7'] + ans['H8'] + ans['H9'] + ans['I1'] + ans[
                  'I2'] + ans['I3'] + ans['I4']+ ans['I5'] + ans['I6'] + ans['I7'] + ans['I8'] + ans['I9']
              )
    return yeni

def search(degerler):
    if degerler is False:
        return False
    if all(len(degerler[s]) == 1 for s in kare):
        return degerler

    n,s = min((len(degerler[s]), s) for s in kare if len(degerler[s]) > 1)
    return some(search(atama(degerler.copy(), s, d)) for d in degerler[s])



def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

def sudokuCoz2():
    deneme = 1
    while deneme:
        txt = "C:\\Users\\Gökçe Yılmaz\\Desktop\\SamuraiSudokuSolver\\sudoku.txt"
        try:
            f = open(txt, 'r')
            deneme = 0
        except FileNotFoundError:
            print("Dosya bulunamadı.")
    samurai_grid = f.read().split('\n')
    print(samurai_grid)

    degerler_ayristir(samurai_grid)

    print("5 Thread ile harcanan zaman: " + str(time.time() - threadTime))

