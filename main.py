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
root.mainloop()