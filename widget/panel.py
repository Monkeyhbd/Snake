def panel_init(master, snake):
    def snake_change_next_way(event):
        if event.keysym == 'Up':
            snake.next_way_change('N')
        if event.keysym == 'Down':
            snake.next_way_change('S')
        if event.keysym == 'Left':
            snake.next_way_change('W')
        if event.keysym == 'Right':
            snake.next_way_change('E')

    def suspend_continue_event(event):
        if event.keysym == 'space':
            suspend_continue()

    def suspend_continue():
        if snake.condition == 1:  # 正在运行-->暂停
            snake.condition = 2
        elif snake.condition == 2:  # 暂停-->正在运行
            snake.condition = 1

    master.bind('<Up>', snake_change_next_way)
    master.bind('<Down>', snake_change_next_way)
    master.bind('<Left>', snake_change_next_way)
    master.bind('<Right>', snake_change_next_way)

    master.bind('<space>', suspend_continue_event)
