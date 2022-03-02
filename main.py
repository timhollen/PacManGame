import random

import tkinter

root = tkinter.Tk()
root.resizable(height=False, width=False)

Mymap = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 9,
    0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 9,
    0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 9,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 9,
    0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 9,
    0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 5, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 6, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 9,
    0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 9,
    0, 0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 0, 0, 9,
    0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 9,
    0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 9,
    0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 9,
    0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9,

]
row = 0
column = -1
new_tile = True
lable_map = []

for tile in Mymap:
    board = tkinter.Label(root, height=3, width=8)
    column += 1
    if tile == 9:
        row += 1
        column = -1

    if tile == 0:
        board.config(bg='black')
        new_tile = True
    if tile == 1:
        board.config(bg='blue')
        new_tile = True

    if tile == 2:
        board.config(bg='blue', text='SP', fg='blue')
        new_tile = True

    if tile == 5:
        board.config(bg='orange')
        new_tile = True

    if tile == 6:
        board.config(bg='white')
        new_tile = True

    if tile == 3:
        board.config(bg='pink', foreground='pink', text='spawn')
        new_tile = True

    if new_tile:
        board.grid(row=row, column=column)
        new_tile = False
        lable_map.append(board)
    else:
        board.destroy()

row_change = 0
column_change = 0
pacman = tkinter.Label(root, height=3, width=8, bg='yellow')
pacman.grid(row=16, column=13)

points = 0
point_lable = tkinter.Label(root, text='Points: ' + str(points), font=('sans', 50), height=1, width=10, bg='black',
                            foreground='white')
point_lable.place(x=1200, y=1100)

hearts = []
heart_lable1 = tkinter.Label(root, height=3, width=8, bg='red')
heart_lable1.grid(row=22, column=7)

heart_lable2 = tkinter.Label(root, height=3, width=8, bg='red')
heart_lable2.grid(row=22, column=5)
heart_lable3 = tkinter.Label(root, height=3, width=8, bg='red')
heart_lable3.grid(row=22, column=3)
hearts.append(heart_lable1)
hearts.append(heart_lable2)
hearts.append(heart_lable3)

move = True
started = False
start = False
food_map = []


def Food():
    for tile in lable_map:
        if tile.cget('bg') == 'blue':
            if not tile.cget('text') == 'SP':
                food = tkinter.Label()
                food.grid(row=tile.grid_info()['row'], column=tile.grid_info()['column'])
                food.config(bg='yellow')
                food_map.append(food)
            else:
                food = tkinter.Label()
                food.grid(row=tile.grid_info()['row'], column=tile.grid_info()['column'])
                food.config(bg='yellow', height=2, width=6, text='SP', fg='yellow')
                food_map.append(food)


ghost = tkinter.Label(root, height=3, width=8, bg='pink')
ghost.grid(row=10, column=13)
ghost1 = tkinter.Label(root, height=3, width=8, bg='pink')
ghost1.grid(row=10, column=13)
ghost2 = tkinter.Label(root, height=3, width=8, bg='pink')
ghost2.grid(row=10, column=13)
ghost3 = tkinter.Label(root, height=3, width=8, bg='pink')
ghost3.grid(row=10, column=13)

ghosts = []
ghost_spawn = []

ghosts.append(ghost)
ghosts.append(ghost1)
ghosts.append(ghost2)
ghosts.append(ghost3)

ghost_spawn.append(ghost)
ghost_spawn.append(ghost1)
ghost_spawn.append(ghost2)
ghost_spawn.append(ghost3)

ghost_movement = [[0, 1], [0, -1], [1, 0], [-1, 0]]

capture_ghost = False
liv = 3
ghost_movement_randomizer = 0
capture_timer = 0
new_ghost = True
ghost_timer = 0
new_ghosts = False


def movement():
    global move, change, row_change, column_change, points, ghost, ghost_move, start, started, capture_ghost, liv, ghost_movement_randomizer, new_ghost, ghost_timer, ghost_spawn, capture_timer, new_ghosts
    root.after(150, movement)
    ghost_timer += 150

    if len(food_map) == 0:
        Food()
        if new_ghosts:
            ghost = tkinter.Label(root, height=3, width=8, bg='pink')
            ghost.grid(row=10, column=13)
            ghost1 = tkinter.Label(root, height=3, width=8, bg='pink')
            ghost1.grid(row=10, column=13)
            ghost2 = tkinter.Label(root, height=3, width=8, bg='pink')
            ghost2.grid(row=10, column=13)
            ghost3 = tkinter.Label(root, height=3, width=8, bg='pink')
            ghost3.grid(row=10, column=13)

            ghosts.append(ghost)
            ghosts.append(ghost1)
            ghosts.append(ghost2)
            ghosts.append(ghost3)

            ghost_spawn.append(ghost)
            ghost_spawn.append(ghost1)
            ghost_spawn.append(ghost2)
            ghost_spawn.append(ghost3)

    if ghost_timer > 1:
        new_ghost = True
        ghost_timer = 0
    if capture_ghost:
        capture_timer += 150

    if capture_timer > 15000:
        capture_ghost = False
        capture_timer = 0
        for ghost in ghosts:
            ghost.config(bg='pink')

    if capture_ghost:
        for ghost in ghosts:
            ghost.config(bg='light blue')
    if new_ghost:
        if len(ghost_spawn) > 0:
            random.shuffle(ghost_movement)
            ghost = random.choice(ghost_spawn)
            ghost.grid(row=8, column=13)
            ghost_spawn.pop(ghost_spawn.index(ghost))
            new_ghost = False

    if not started:
        started = True

    if move:
        pacman.grid(row=pacman.grid_info()['row'] + row_change, column=pacman.grid_info()['column'] + column_change)

    for food in food_map:
        if food.grid_info()['row'] == pacman.grid_info()['row']:
            if food.grid_info()['column'] == pacman.grid_info()['column']:
                if food.cget('text') == 'SP':
                    capture_ghost = True

                food.destroy()
                food_map.pop(food_map.index(food))
                points += 1
                point_lable.config(text='Points: ' + str(points))

    for tile_bg in lable_map:
        if tile_bg.grid_info()['row'] == pacman.grid_info()['row'] + row_change:
            if tile_bg.grid_info()['column'] == pacman.grid_info()['column'] + column_change:
                if tile_bg.cget('bg') == 'white':
                    pacman.grid(row=10, column=0)
                if tile_bg.cget('bg') == 'orange':
                    pacman.grid(row=10, column=26)

                if tile_bg.cget('bg') == 'black':
                    move = False
    for ghost in ghosts:
        if not capture_ghost:
            if pacman.grid_info()['row'] == ghost.grid_info()['row']:
                if pacman.grid_info()['column'] == ghost.grid_info()['column']:
                    liv -= 1
                    if liv == 0:
                        root.destroy()
                        break

                    hearts[liv].config(bg='white')
    for ghost in ghosts:
        if capture_ghost:
            if pacman.grid_info()['row'] == ghost.grid_info()['row']:
                if pacman.grid_info()['column'] == ghost.grid_info()['column']:
                    points += 1000
                    point_lable.config(text='Points: ' + str(points))
                    ghost.grid(row=8, column=12)
                    ghost.destroy()
                    ghosts.pop(ghosts.index(ghost))
                    if len(ghosts) == 0:
                        new_ghosts = True
                    break

    for ghost in ghosts:

        for tile in lable_map:
            if tile.grid_info()['row'] == ghost.grid_info()['row'] + ghost_movement[0][0]:
                if tile.grid_info()['column'] == ghost.grid_info()['column'] + ghost_movement[0][1]:
                    if tile.cget('bg') == 'blue':
                        ghost.grid(row=ghost.grid_info()['row'] + ghost_movement[0][0],
                                   column=ghost.grid_info()['column'] + ghost_movement[0][1])

                        break

                    if tile_bg.cget('bg') == 'white':
                        ghost.grid(row=10, column=0)
                    if tile_bg.cget('bg') == 'orange':
                        ghost.grid(row=10, column=26)

                    if tile.cget('bg') == 'black':
                        random.shuffle(ghost_movement)

                        continue


def keypress_w(event):
    global row_change, column_change, move, start

    start = True
    for tile in lable_map:
        if tile.grid_info()['row'] == pacman.grid_info()['row'] + -1:
            if tile.grid_info()['column'] == pacman.grid_info()['column'] + 0:
                if tile.cget('bg') == 'black':
                    pass
                else:
                    row_change = -1
                    column_change = 0
                    move = True


def keypress_s(event):
    global row_change, column_change, move, change, start
    start = True
    for tile in lable_map:
        if tile.grid_info()['row'] == pacman.grid_info()['row'] + 1:
            if tile.grid_info()['column'] == pacman.grid_info()['column'] + 0:
                if tile.cget('bg') == 'black':
                    pass
                else:
                    row_change = 1
                    column_change = 0
                    move = True


def keypress_d(event):
    global row_change, column_change, move, start
    start = True
    for tile in lable_map:
        if tile.grid_info()['row'] == pacman.grid_info()['row'] + 0:
            if tile.grid_info()['column'] == pacman.grid_info()['column'] + 1:
                if tile.cget('bg') == 'black':
                    pass
                else:
                    row_change = 0
                    column_change = 1
                    move = True


def keypress_a(event):
    global row_change, column_change, move, start
    start = True
    for tile in lable_map:
        if tile.grid_info()['row'] == pacman.grid_info()['row'] + 0:
            if tile.grid_info()['column'] == pacman.grid_info()['column'] + -1:
                if tile.cget('bg') == 'black':
                    pass
                else:
                    row_change = 0
                    column_change = -1
                    move = True


root.bind('<w>', keypress_w)
root.bind('<s>', keypress_s)
root.bind('<d>', keypress_d)
root.bind('<a>', keypress_a)
root.after(1, movement)
root.mainloop()
