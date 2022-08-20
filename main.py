from tkinter import Tk, Canvas
from random import shuffle

# Размер игрового поля (4x4)
BOARD_SIZE = 4
# Размер одного блока в пикселях
SQUARE_SIZE = 80
# Значение пустого блока. В нашем случае пустым будет последний блок
EMPTY_SQUARE = BOARD_SIZE ** 2
# Главное окно
root = Tk()
root.title('Пятнашки')
# Область для рисования
c = Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
                 height=BOARD_SIZE * SQUARE_SIZE,
                 bg='#808080')
c.pack()

def draw_board():
    # убираем все, что нарисовано на холсте
    c.delete('all')
    # Наша задача сгруппировать пятнашки из списка в квадрат
    # со сторонами BOARD_SIZE x BOARD_SIZE
    # i и j будут координатами для каждой отдельной пятнашки
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # получаем значение, которое мы должны будем нарисовать
            # на квадрате
            index = str(board[BOARD_SIZE * i + j])
            # если это не клетка которую мы хотим оставить пустой
            if index != str(EMPTY_SQUARE):
                # рисуем квадрат по заданным координатам
                c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#43ABC9',
                                   outline='#FFFFFF')
                # пишем число в центре квадрата
                c.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2,
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                              fill='#FFFFFF')

board = list(range(1, EMPTY_SQUARE + 1))

draw_board()
root.mainloop()