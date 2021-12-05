
from kontrol import kontrol
import threading
import time


topleft = []
topright = []
bottomleft = []
bottomright = []
middle = []
threadTime = time.time()

def vektorel(A, B, c=''):
    "A ve B'deki elemanların vektörel çarpımı"
    return [a + b + c for a in A for b in B]


rakamlar = '123456789'
satir = 'ABCDEFGHI'
sutun = rakamlar

id_var = 'a'  # sol üst
kare_a = vektorel(satir, sutun, id_var)
birimliste_a = ([vektorel(satir, c, id_var) for c in sutun] +
              [vektorel(r, sutun, id_var) for r in satir] +
              [vektorel(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

id_var = 'b'  # sağ üst
kare_b = vektorel(satir, sutun, id_var)
birimliste_b = ([vektorel(satir, c, id_var) for c in sutun] +
              [vektorel(r, sutun, id_var) for r in satir] +
              [vektorel(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

id_var = 'c'  # sol alt
kare_c = vektorel(satir, sutun, id_var)
birimliste_c = ([vektorel(satir, c, id_var) for c in sutun] +
              [vektorel(r, sutun, id_var) for r in satir] +
              [vektorel(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

id_var = 'd'  # sağ alt
kare_d = vektorel(satir, sutun, id_var)
birimliste_d = ([vektorel(satir, c, id_var) for c in sutun] +
              [vektorel(r, sutun, id_var) for r in satir] +
              [vektorel(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])


def repl(c):
    "Ortadaki sudokunun köşelerdeki sudokular ile kesinşen kısımları için"
    a = b = 0
    s = ""
    if c[0] in 'ABCGHI' and c[1] in '123789':
        if c[0] in 'ABC':
            s += chr(ord(c[0]) + 6)
            a = 1
        elif c[0] in 'GHI':
            s += chr(ord(c[0]) - 6)
            a = 2
        if c[1] in '123':
            s += chr(ord(c[1]) + 6)
            b = 1
        elif c[1] in '789':
            s += chr(ord(c[1]) - 6)
            b = 2
    else:
        return c
    if a == 1 and b == 1:
        s += 'a'
    elif a == 1 and b == 2:
        s += 'b'
    elif a == 2 and b == 1:
        s += 'c'
    elif a == 2 and b == 2:
        s += 'd'
    return s


id_var = '+'  #orta
kare_orta = [repl(x) for x in vektorel(satir, sutun, id_var)]
birimliste_orta = ([kare_orta[x * 9:x * 9 + 9] for x in range(0, 9)] +
                [kare_orta[x::9] for x in range(0, 9)] +
                [vektorel(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
                 for cs in ('123', '456', '789')
                 if not (rs in 'ABCGHI' and cs in '123789')])

butunkareler = set(kare_a + kare_b + kare_c + kare_d + kare_orta)
butunbirimlerliste = birimliste_a + birimliste_b + birimliste_c + birimliste_d + birimliste_orta

birimler = dict((s, [u for u in butunbirimlerliste if s in u])
             for s in butunkareler)
iliskililer = dict((s, set(sum(birimler[s], [])) - set([s]))
             for s in butunkareler)




def olasidegerler(grid):
    """Olası değerleri çıkartma. İlk başta bir kare tüm değerleri alabilir"""
    degerler = dict((s, rakamlar) for s in butunkareler)
    for s, d in degerler_ayristir(grid).items():
        if d in rakamlar and not atamafonk(degerler, s, d):
            return False
    return degerler


def flatten(arr):
    return [x for sub in arr for x in sub]


def degerler_ayristir(grid):
    "Txt dosyasından alınan değerlerin hangi satırın hangi kareye ait olduğunu ayırıp dictionary tipinde tutar"
    a = flatten([x[:9] for x in grid[:9]])
    b = flatten([x[9:] for x in grid[:6]] + [x[12:] for x in grid[6:9]])
    c = flatten([x[:9] for x in grid[12:]])
    d = flatten([x[12:] for x in grid[12:15]] + [x[9:] for x in grid[15:]])
    orta = flatten([x[6:15] for x in grid[6:9]] + [x[:9] for x in grid[9:12]] + [x[6:15] for x in grid[12:15]])


    harfler = a + b + c + d + orta
    kareler = kare_a + kare_b + kare_c + kare_d + kare_orta
    assert len(harfler) == 405
    return dict(zip(kareler, harfler))





def atamafonk(degerler, s, d):
    """d değeri hariç diğer tüm değerleri eler degerler[s]ten """
    diger_degerler = degerler[s].replace(d, '')
    if all(elemefonk(degerler, s, d2) for d2 in diger_degerler):

        return degerler
    else:
        return False


def elemefonk(degerler, s, d):
    """d değerini degerler[s] ten eler"""
    if d not in degerler[s]:

        return degerler
    degerler[s] = degerler[s].replace(d, '')
    if len(degerler[s]) == 0:
        return False
    elif len(degerler[s]) == 1:
        d2 = degerler[s]
        if not all(elemefonk(degerler, s2, d2) for s2 in iliskililer[s]):
            return False
    for u in birimler[s]:
        dplaces = [s for s in u if d in degerler[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not atamafonk(degerler, dplaces[0], d):
                return False

    return degerler




def display(degerler, sqr):
    """
    Konsolda sudoku kısımlarını yazdırma
    """
    width = 1 + max(len(degerler[s]) for s in sqr)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in satir:
        print(''.join(degerler[sqr[(ord(r) - 65) * 9 + int(c) - 1]]
                      .center(width) + ('|' if c in '36' else '') for c in sutun))

        if r in 'CF': print(line)

    print()


def display_samurai(vals):
    """
    Konsolda sudokunun tamamını yazdırma
    """
    if not vals:
        print("Çözüm Bulunamadı :(")
        return
    print("Sol üst:")
    display(vals, kare_a)
    print("Sağ üst:")
    display(vals, kare_b)
    print("Sol alt:")
    display(vals, kare_c)
    print("Sağ alt:")
    display(vals, kare_d)
    print("Orta:")
    display(vals, kare_orta)


    kontrol(vals, [kare_a, kare_b, kare_c, kare_d, kare_orta])


    def solutiontopleft(letter):
        i = 1
        while i < 10:
            topleft.append(vals[letter + str(i) + "a"])
            i = i + 1

    solutiontopleft("A")
    solutiontopleft("B")
    solutiontopleft("C")
    solutiontopleft("D")
    solutiontopleft("E")
    solutiontopleft("F")
    solutiontopleft("G")
    solutiontopleft("H")
    solutiontopleft("I")

    def solutiontopright(letter):
        i = 1
        while i < 10:
            topright.append(vals[letter + str(i) + "b"])
            i = i + 1

    solutiontopright("A")
    solutiontopright("B")
    solutiontopright("C")
    solutiontopright("D")
    solutiontopright("E")
    solutiontopright("F")
    solutiontopright("G")
    solutiontopright("H")
    solutiontopright("I")

    def solutionbottomleft(letter):
        i = 1
        while i < 10:
            bottomleft.append(vals[letter + str(i) + "c"])
            i = i + 1

    solutionbottomleft("A")
    solutionbottomleft("B")
    solutionbottomleft("C")
    solutionbottomleft("D")
    solutionbottomleft("E")
    solutionbottomleft("F")
    solutionbottomleft("G")
    solutionbottomleft("H")
    solutionbottomleft("I")

    def solutionbottomright(letter):
        i = 1
        while i < 10:
            bottomright.append(vals[letter + str(i) + "d"])
            i = i + 1

    solutionbottomright("A")
    solutionbottomright("B")
    solutionbottomright("C")
    solutionbottomright("D")
    solutionbottomright("E")
    solutionbottomright("F")
    solutionbottomright("G")
    solutionbottomright("H")
    solutionbottomright("I")

    def solutionmiddle1(letter):
        i = 4
        while i < 7:
            middle.append(vals[letter + str(i) + "+"])
            i = i + 1

    solutionmiddle1("A")
    solutionmiddle1("B")
    solutionmiddle1("C")


    def solutionmiddle2(letter):
        i = 1
        while i < 10:
            middle.append(vals[letter + str(i) + "+"])
            i = i + 1

    solutionmiddle2("D")
    solutionmiddle2("E")
    solutionmiddle2("F")

    def solutionmiddle3(letter):
        i = 4
        while i < 7:
            middle.append(vals[letter + str(i) + "+"])
            i = i + 1

    solutionmiddle3("G")
    solutionmiddle3("H")
    solutionmiddle3("I")





def solve(grid):
    return search(olasidegerler(grid))



def search(values):
    """
    Dept-first search algoritmasıyla tüm olası değerleri dener
    """

    if values is False:
        return False
    if all(len(values[s]) == 1 for s in butunkareler):
        return values
    n, s = min((len(values[s]), s) for s in butunkareler if len(values[s]) > 1)
    return some(search(atamafonk(values.copy(), s, d))
                for d in values[s])



def some(seq):

    for e in seq:
        if e: return e
    return False





def sudokuCoz():
    threadTime = time.time()
    deneme = 1
    while deneme:
        txt = "C:\\Users\\Gökçe Yılmaz\\Desktop\\SamuraiSudokuSolver\\sudoku.txt"
        try:
            f = open(txt, 'r')
            deneme = 0
        except FileNotFoundError:
            print("Dosya bulunamadı.")
    samurai_grid = f.read().split('\n')

    ans = solve(samurai_grid)

    display_samurai(ans)

    print("harcanan zaman: " + str(time.time() - threadTime))


