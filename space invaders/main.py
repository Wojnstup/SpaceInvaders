import pygame
import random
import math
from bullet import Bullet
from enemy import Enemy

# icons and images by
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<div>Icons made by <a href="https://www.flaticon.com/authors/pixel-buddha" title="Pixel Buddha">Pixel Buddha</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<div>Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

def player_put():
    global playerX
    global playerY
    screen.blit(player, (playerX, playerY))

def calculate_distance(first_coor, second_coor):
    return math.sqrt( (first_coor[0]-second_coor[0])**2 + (first_coor[1]- second_coor[1])**2)


if __name__ == "__main__":

    #initializing the game
    pygame.init()

    #setting a display
    screen = pygame.display.set_mode((800,600))

    #title and icon

    pygame.display.set_caption("Space Invaders")

    icon = pygame.image.load("astronaut.png")
    pygame.display.set_icon(icon)

    #Player

    player = pygame.image.load("player.png")
    playerX = 380
    playerY = 520

    player_moving_left = False    
    player_moving_right = False    

    player_speed = 6

    #enemies
    enemies = []
    for Y_num in range(6):
        for X_num in range(9):
            enemies.append(Enemy(Y=Y_num*64, X= X_num * 64))
  
    #bullets
    bullets = []
    
    #background
    background = pygame.image.load("background.png")

    #game loop
    running = True
    game_over = False
    while running:
        screen.fill((0,0,0))
        screen.blit(background, (0,0))



       
        #EVENT LOOP
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #CHECKING FOR INPUT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player_moving_left = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player_moving_right = True
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet('bullet.png', playerX))
                   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                    player_moving_right = False
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player_moving_left = False

        #GAME OVER!
        if game_over:
            bullets.clear()
            enemies.clear()
            
            #continue

        player_put()

        #MOVING THE PLAYER
        if player_moving_left == True:
            if playerX >= 0: 
                playerX -= player_speed
        if player_moving_right == True:
            if playerX <= 738:
                playerX += player_speed

        #MOVING THE ENEMY
        for enemy in enemies:
            #CHANGING THE SPEED BASED ON THE NUMBER OF ENEMIES
            enemy.speed = enemy.speed_modifier*(2 - len(enemies)/ 36)
            enemy.render(screen)

            #CHECKING FOR GAME OVER
            if enemy.Y >=550:
                game_over = True

            #FLIPPING THE ENEMIES WHILE REACHING THE END OF A SCREEN
            if enemy.X >= 738 or enemy.X <=0:
                for _enemy in enemies:
                    _enemy.flip()
                break
                


        #MENAGING ALL THE BULLETS
        for bullet in bullets:
            #DELETING BULLETS
            if bullet.Y < -10:
                bullets.remove(bullet)
            else:
                bullet.put(screen)
                bullet.move()

            #COLISION WITH ALIENS
            for enemy in enemies:
                if calculate_distance( (enemy.X, enemy.Y), (bullet.X, bullet.Y) ) <= 32:
                    try:
                        enemies.remove(enemy)
                        bullets.remove(bullet)
                    except:
                        continue
                


        pygame.display.update()