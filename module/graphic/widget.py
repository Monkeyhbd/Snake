def board_init(master, h=20, w=40):
    board = tkinter.Canvas(master)
    GUI.board = board
    for a in range(h):
        Public.board_dead_point.append([-W, a * W])  # W
        Public.board_dead_point.append([w * W, a * W])  # E
    for b in range(w):
        Public.board_dead_point.append([b * W, -W])  # N
        Public.board_dead_point.append([b * W, h * W])  # S
    board.size = [w, h]
    board.place(x=W, y=W, width=w * W, height=h * W)
    for a in range(h):
        for b in range(w):
            if a % 2 - b % 2 == 0:
                tkinter.Label(board, bg='white').place(x=b * W, y=a * W, width=W, height=W)

    return board
