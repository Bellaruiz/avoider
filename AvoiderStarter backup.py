# Starter code for an avoider game.
# Isabella Ruiz and Jai Davis,
#
import sys, pygame, math, time

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_piskell_sprite(sprite_folder_name, number_of_frames):
    frame_counts = []
    padding = math.ceil(math.log(number_of_frames-1,10))
    for frame in range(number_of_frames):
        folder_and_file_name = "./"+sprite_folder_name + "/sprite_" + sprite_folder_name + str(frame).rjust(padding,'0') +".png"
        frame_counts.append(pygame.image.load(folder_and_file_name).convert_alpha())
                             
    return frame_counts

# This function moves rect slowly between start_pos and end_pos. The num_frame parameter
# says how many frames of animation are needed to do the bounce, so a bigger number means
# the rect moves slower. frame_count is the current overall frame count from the game.
def bounce_rect_between_two_positions( rect, start_pos, end_pos, num_frame, frame_count ):
    if frame_count%num_frame < num_frame/2:
        new_pos_x = start_pos[0] + (end_pos[0] - start_pos[0]) * (frame_count%(num_frame/2))/(num_frame/2)
        new_pos_y = start_pos[1] + (end_pos[1] - start_pos[1]) * (frame_count%(num_frame/2))/(num_frame/2)
    else:
        new_pos_x = end_pos[0] + (start_pos[0] - end_pos[0]) * (frame_count%(num_frame/2))/(num_frame/2)
        new_pos_y = end_pos[1] + (start_pos[1] - end_pos[1]) * (frame_count%(num_frame/2))/(num_frame/2)

    rect.center = (new_pos_x, new_pos_y)

# The main loop handles most of the game    
def main():
                             
    # Initialize pygame                                 
    pygame.init()

    # Get a font
    myfont = pygame.font.SysFont("monospace", 24)

    screen = pygame.display.set_mode((800,800))

    #hero is facing
    is_facing_right = True

    # Load in the background image
    map1 = pygame.image.load("./map/map0.png").convert_alpha()
    map2 = pygame.image.load("./map/map1.png").convert_alpha()
    win = pygame.image.load("./victory/sprite_victory0.png").convert_alpha()
    gameover = pygame.image.load("./gameover/sprite_gameover0.png").convert_alpha()
    bone = pygame.image.load("./bone/sprite_bone0.png").convert_alpha()
    # Store window width and height in different forms for easy access
    map_size = map1.get_size()
    # The map rect is basically the whole screen, and we will draw to it to fill the background with the image
    map_rect = map1.get_rect()

    gameover_rect = gameover.get_rect()
    win_rect = win.get_rect()
    # create the window the same size as the map image

    # Load Sprite (player)
    hero = load_piskell_sprite("doge", 2)
    hero_rect = hero[0].get_rect()

    catto = load_piskell_sprite("Catto", 2)
    catto_rect = catto[0].get_rect()

    sprinkler = load_piskell_sprite("sprinkler", 4)
    sprinkler_rect = sprinkler[0].get_rect()

    # Sprite Character
    # The frame_count counts all the frames that have passed since the start of the game.
    # Look at the print statements in the loop to see how to use the count with a mod function
    # to get cycles of different lengths.
    frame_count = 0
        

    # The clock helps us manage the frames per second of the animation
    clock = pygame.time.Clock()

    # The game should not start until the start color is clicked. Until then game_started is False
    game_started = False

    # is_alive means that the game loop should continue. Winning or losing the game sets is_alive to False.
    is_alive = True


    level = map1
    # Loop while the player is still active
    is_bone_taken = False

    pygame.mouse.set_pos([0,0])
##    start_ticks=pygame.time.get_ticks() #starter tick
    while is_alive:
        # Check events by looping over the list of events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_alive = False
<<<<<<< HEAD
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
            seconds>10 # if more than 10 seconds close the game
            break
        print (seconds) #print how many seconds

        
=======
            if event.type == pygame.MOUSEBUTTONDOWN:
        time = pygame.time.get_ticks()
        if time >= 5000:
            is_alive = False
            print('gameover')
>>>>>>> 26d1b9960776ee56903142016adf44c9bfc731a3
        screen.blit(level, map_rect)
        if not is_bone_taken:
            screen.blit(bone, (600,700))


        # This grabs the current color under the cursor from the screen. Note that anything
        # drawn on the screen before this statement adds to the color. I could have also
        # taken the color from the map if I just wanted that.
        cursor_color = screen.get_at(pygame.mouse.get_pos())
        if cursor_color == (255,248,248,255):
            is_bone_taken = True
        if cursor_color == (111,0,0,255) or cursor_color == (86,1,1,255):
            level = map2
        if cursor_color == (127,127,127,255):
            screen.fill((255,255,255))
            screen.blit(win, win_rect)
            pygame.display.update()
            break

        if cursor_color == (118,26,12,255) or cursor_color == (118,26,12,255):
            is_alive = False
            print('gameover')

            
        # Note that the color has 4 values - the 4th is alpha. If you want to compare colors
        # make sure that you compare all the values. An example would be
        # cursor_color == (255, 0, 0, 255)
        # to see if the cursor is over a pure red area.
        print("Color:", cursor_color)

        # You may have sprites with different numbers of frames. We can make cycles
        # of different lengths by using mod on the frame_count. This is easier than
        # maintaining a different frame count variable for each different sprite.
        print("Cycle of length 3:", frame_count%3) # counts 0,1,2,0,1,2
        print("Cycle of length 4:", frame_count%4) # counts 0,1,2,3,0,1,2,3

        # Render text to the screen
##        label = myfont.render("Click the Grey", True, (255,100,0))
##        screen.blit(label, (20,20))

        ##Set FPS
        fps = clock.get_fps()


        #render text to the screen
        FPS = myfont.render("FPS:"+ str(int(fps)),
        True,(255,255,0))
        screen.blit(FPS,(500,20))

        Timer = myfont.render("Count:"+ str(int(time)),
        True, (255,255,0))
        screen.blit(Timer,(700,20))

        # Do drawing to the screen
        hero_sprite = hero[frame_count%len(hero)]
        
        if is_facing_right:
            hero_sprite = pygame.transform.flip(hero_sprite, True, False)
        hero_rect.center = pygame.mouse.get_pos()
        screen.blit(hero_sprite, hero_rect)

##<<<<<<< HEAD


##        catto_sprite = catto[frame_count%len(catto)]
##        screen.blit(catto_sprite, catto_rect)

##=======
        
        if level is map2:
            sprinkler = load_piskell_sprite("sprinkler", 4)
            sprinkler_rect = sprinkler[0].get_rect()
            sprinkler_rect.center = (200,700)
            sprinkler_sprite = sprinkler[frame_count%len(sprinkler)]
            screen.blit(sprinkler_sprite, sprinkler_rect)
            if hero_rect.colliderect(sprinkler_rect):
                is_alive = False
                print('gameover')

        if level is map2:
            sprinkler = load_piskell_sprite("sprinkler", 4)
            sprinkler_rect = sprinkler[0].get_rect()
            sprinkler_rect.center = (300,350)
            sprinkler_sprite = sprinkler[frame_count%len(sprinkler)]
            screen.blit(sprinkler_sprite, sprinkler_rect)
            if hero_rect.colliderect(sprinkler_rect):
                is_alive = False
                print('gameover')

        if level is map2:
            sprinkler = load_piskell_sprite("sprinkler", 4)
            sprinkler_rect = sprinkler[0].get_rect()
            sprinkler_rect.center = (700,80)
            sprinkler_sprite = sprinkler[frame_count%len(sprinkler)]
            screen.blit(sprinkler_sprite, sprinkler_rect)
            if hero_rect.colliderect(sprinkler_rect):
                is_alive = False
                print('gameover')
            
        bounce_rect_between_two_positions( catto_rect, (600,250), (600,550), 24, frame_count )
        catto_sprite = catto[frame_count%len(catto)]
        screen.blit(catto_sprite, catto_rect)


        if hero_rect.colliderect(catto_rect):
            is_alive = False
            print('gameover')
##>>>>>>> 78f326752d94ff352f933f2f180fbcef63d9498d


        if not is_alive:
            screen.fill((255,255,255))
            screen.blit(gameover, gameover_rect)

        
        # Bring drawn changes to the front
        pygame.display.update()
            

        # We are basically done this with frame of animation, so update the count.
        frame_count += 1

        # This tries to force the loop to run at 1/2 fps. The is artifically slow so the output above
        # can be inspected. You should change this speed. Something like 30 is more normal.
        clock.tick(20)

    # This happens once the loop is finished - the game is over.
    pygame.quit()
    sys.exit()


# Start the program
main()
