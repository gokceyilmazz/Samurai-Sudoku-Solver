
rakamlar = '123456789'
satirlar = 'ABCDEFGHI'
sutunlar = rakamlar


def kontrol(degerler, sqrs):

    samurai = []

    for sqr in sqrs:
        samurai.append(sudoku_olustur(degerler, sqr))

    for sudoku in samurai:
        if not kontrol_sudoku(sudoku):
            print("Hatalı Sudoku.")
            return False

    corners_coordinate = [
        [[samurai[0], [6, 6]], [samurai[4], [0, 0]]],
        [[samurai[1], [6, 0]], [samurai[4], [0, 6]]],
        [[samurai[2], [0, 6]], [samurai[4], [6, 0]]],
        [[samurai[3], [0, 0]], [samurai[4], [6, 6]]]
    ]

    for corner in corners_coordinate:
        if not koseler_kontrol(corner[0], corner[1]):
            print("Hatalı sudoku!!!!")
            return False

    print("Çözüm kontrol edildi.")
    return True

def kontrol_sudoku(sudoku):

    box_coordinate = [
        [[0, 0], [0, 3], [0, 6]],
        [[3, 0], [3, 3], [3, 6]],
        [[6, 0], [6, 3], [6, 6]]
    ]

    for satir in box_coordinate:
        for sutun in satir:
            box = uceuckare(sudoku, sutun[0], sutun[1])
            if not liste_kontrol(matrix2list(box)):
                return False


    for satir in sudoku:
        if not liste_kontrol(satir):
            return False


    for sutun in range(9):
        sutun_liste = []
        for satir in range(9):
            sutun_liste.append(sudoku[satir][sutun])
        if not liste_kontrol(sutun_liste):
            return False

    return True


def koseler_kontrol(box1, box2):

    box1_list = uceuckare(box1[0], box1[1][0], box1[1][1])
    box2_list = uceuckare(box2[0], box2[1][0], box2[1][1])
    return box1_list == box2_list


def liste_kontrol(input):

    int_list = list(map(int, input))
    int_list.sort()
    return int_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def sudoku_olustur(degerler, sqr):
    sudoku = [[None]*9]*9
    i = 0
    for r in satirlar:
        sudoku[i] = [degerler[sqr[(ord(r) - 65) * 9 + int(c) - 1]] for c in sutunlar]
        i += 1

        if i == 9:
            i = 0
    return sudoku


def uceuckare(sudoku, satir, sutun):

    box = [[]*3]*3

    for i in range(len(box)):
        box[i] = sudoku[satir][sutun:sutun+3]
        satir += 1
    return box


def matrix2list(matrix):

    return [val for sublist in matrix for val in sublist]
