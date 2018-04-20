#importing necessary libraries for game setup
import random
import curses


delay = input('Use arrow keys to control snake. Press enter to start game.')

#initializing the screen 

#and setting up cursor start position 
s = curses.initscr()
curses.curs_set(0)

#width and height - sh = screen height, sw = screen width, w = window
sh,sw= s.getmaxyx()

#new window using the height, width, and start point at top left of screen
w = curses.newwin(sh,sw,0,0)

#set keypad input to true
w.keypad(1)

#set screen refresh to every 100 ms
w.timeout(100)

#create initial position for snake 
snk_x = sw//4
snk_y = sh//2

#creating snake body parts

snake = [
    [snk_y,snk_x],
    [snk_y,snk_x -1],
    [snk_y,snk_x -2]
]

#creating tasty food for our python snake (at center of screen)
food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

#snake directions
key = curses.KEY_RIGHT

#event loop for every snake move
while True:
    #check to see what next key is 
    next_key = w.getch()
    #will give either nothing or the next key
    key = key if next_key == -1 else next_key
    
    #check to see if player loses (at edges of screen or collides w/itself)
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin() #stops window
        quit() #quits game
    
    #creates new snake head (old head of snake plus)
    new_head = [snake[0][0], snake[0][1]]
    
    #if key is pressed down, take position and change it by 1
    if key == curses.KEY_DOWN:
        new_head[0] += 1
        
    if key == curses.KEY_UP:
        new_head[0] -= 1
    
    if key == curses.KEY_LEFT:
        new_head[0] -= 1
    
    if key == curses.KEY_RIGHT:
        new_head[0] += 1

    snake.insert(0, new_head)
    
    #has snake eaten yet? Y --> select new food to eat
    if snake[0] == food:
        food = None
        while food is None:
            #create new piece of food
            newfood = [
                #places new food item in random spot
                random.randint(1,sh-1),
                random.randint(1, sw-1)
            ]

            #check if food hasn't been eaten
            food = newfood if newfood not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ') #setting up tail
        
    #add head of snake to the screen
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
   