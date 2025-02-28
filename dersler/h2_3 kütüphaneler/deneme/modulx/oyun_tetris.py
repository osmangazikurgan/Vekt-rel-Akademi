def tetri_basla():
    import random
    import turtle
    
    W, H = 10, 20; S = 15
    
    def board_to_canvas(x, y):
        return ((x - W//2) * S, (y - H//2) * S)
    
    def draw_text(text, x, y, color):
        turtle.color(color)
        turtle.goto(*board_to_canvas(x, y))
        turtle.write(text)
    
    def draw_rect(x, y, w, h, color):
        turtle.color(color)
        x1, y1 = board_to_canvas(x, y)
        x2, y2 = x1 + w*S - 1, y1 + h*S - 1,
        turtle.goto(x1, y1)
        turtle.down()
        turtle.begin_fill()
        turtle.goto(x2, y1)
        turtle.goto(x2, y2)
        turtle.goto(x1, y2)
        turtle.goto(x1, y1)
        turtle.up()
        turtle.end_fill()
    
    
    board = [[None] * W for _ in range(H)]
    
    def draw_board():
        draw_rect(-1, -1, 1, H+1, 'black')
        draw_rect(W, -1, 1, H+1, 'black')
        draw_rect(0, -1, W, 1, 'black')
        for i, row in enumerate(board):
            for j, color in enumerate(row):
                if color:
                    draw_rect(j, i, 1, 1, color)
    
    def find_completed_rows():
        for row in board:
            if all(row):
                yield row
    
    
    BLOCKS = [[] for _ in range(7)]
    for i, line in enumerate('''
        oo   o      o   oo  oo    o
    oooo oo   ooo  ooo  oo    oo  ooo'''.split('\n')):
        for j, char in enumerate(line):
            if char == 'o':
                BLOCKS[j // 5].append((j%5 - 1, -i + 2))
    
    def draw_block(block, x0, y0):
        for dx, dy in block:
            x, y = x0 + dx, y0 + dy
            if y < H:
                draw_rect(x, y, 1, 1, 'blue')
    
    def can_place_block_clipped(block, x0, y0):
        for dx, dy in block:
            x, y = x0 + dx, y0 + dy
            if not (0 <= x < W and 0 <= y) or (y < H and board[y][x]):
                return False
        return True
    
    def place_block(block, x0, y0):
        complete = True
        for dx, dy in block:
            x, y = x0 + dx, y0 + dy
            if 0 <= x < W and 0 <= y < H:
                board[y][x] = 'blue'
            else:
                complete = False
        return complete
    
    
    score = 0
    t = 0
    falling_period = 0
    state = 'normal'
    block = next_block = None
    x, y = 0, 0
    falling_generator = None
    deleting_rows_generator = None
    
    def move_block(dx, dy):
        global x, y
        new_x, new_y = x + dx, y + dy
        possible = can_place_block_clipped(block, new_x, new_y)
        if possible:
            x, y = new_x, new_y
        return possible
    
    def rotate_block():
        global block
        new_block = [(-y, x) for x, y in block]
        possible = can_place_block_clipped(new_block, x, y)
        if possible:
            block = new_block
        return possible
    
    def reset_block():
        global falling_period, block, next_block, x, y, state
        falling_period = [10, 9, 8, 7, 6, 5, 4][min(t // 100, 6)]
        new_block = None
        while not new_block:
            new_block, next_block = next_block, BLOCKS[random.randrange(7)]
        x, y = W // 2, H - 1
        if not can_place_block_clipped(new_block, x, y):
            state = 'game_over'
            return
        block = new_block
        begin_falling(falling_period)
    
    def begin_falling(period):
        global falling_generator
        def fall():
            global falling_generator
            while True:
                for t in range(period):
                    yield
                if not move_block(0, -1):
                    break
            falling_generator = None
            place_block_and_begin_deleting()
            yield
        falling_generator = fall()
    
    def place_block_and_begin_deleting():
        global block, state
        old_block = block
        block = None
        if not place_block(old_block, x, y):
            state = 'game_over'
            return
        begin_deleting_rows()
    
    def begin_deleting_rows():
        global deleting_rows_generator
        if any(find_completed_rows()):
            duration = falling_period
            def delete():
                global deleting_rows_generator, score
                for t in range(duration):
                    if t in (0, duration // 2):
                        color = ('red', 'blue')[t // (duration//2)]
                        for row in find_completed_rows():
                            row[:] = [color] * W
                    yield
                incomplete_rows = [row for row in board if not all(row)]
                n_deleted = H - len(incomplete_rows)
                board[:] = incomplete_rows + [[None] * W for _ in range(n_deleted)]
                score += (n_deleted**2) * 100
                reset_block()
                deleting_rows_generator = None
                yield
            deleting_rows_generator = delete()
        else:
            reset_block()
    
    def update_stage():
        global t
        if block and falling_generator:
            next(falling_generator)
        if deleting_rows_generator:
            next(deleting_rows_generator)
        t += 1
    
    def render_stage():
        turtle.clear()
        draw_board()
        draw_text(f'SCORE: {score}', W + 3, H - 2, 'black')
        draw_text('NEXT BLOCK', W + 3, H - 6, 'black')
        draw_block(next_block, W + 4, H - 8)
        if block:
            draw_block(block, x, y)
        if state == 'game_over':
            draw_text('GAME OVER', W//2 - 2, -3, 'red')
    
    def on_key_left():
        if block:
            move_block(-1, 0)
    def on_key_right():
        if block:
            move_block(1, 0)
    def on_key_down():
        if block:
            if not move_block(0, -1):
                place_block_and_begin_deleting()
    def on_key_space():
        if block:
            begin_falling(period=0)
    def on_key_up():
        if block:
            rotate_block()
    
    
    turtle.tracer(0, 0)
    turtle.hideturtle()
    turtle.up()
    turtle.listen()
    turtle.onkey(turtle.bye, 'Escape')
    turtle.onkey(on_key_left, 'Left')
    turtle.onkey(on_key_right, 'Right')
    turtle.onkey(on_key_down, 'Down')
    turtle.onkey(on_key_space, 'space')
    turtle.onkey(on_key_up, 'Up')
    reset_block()
    def render():
        turtle.ontimer(render, 100)
        update_stage()
        # This is required because turtle.write() always triggers ScrolledCanvas.update().
        old_canvas_update = turtle.ScrolledCanvas.update
        turtle.ScrolledCanvas.update = lambda self: None
        render_stage()
        turtle.ScrolledCanvas.update = old_canvas_update
        turtle.update()
    render()
    turtle.mainloop()