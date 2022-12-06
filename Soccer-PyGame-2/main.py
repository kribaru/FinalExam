import pygame, sys
from pygame.locals import QUIT

#Instructions
print("\nHow to Play:")
print("Click into the Soccer Practice window.")
print("Use the up/down arrow keys to move the player.")
print("To shoot, press and hold space bar.")
print("Avoid hitting the defender and shooting out of bounds.")
print("When prompted, press Y or N to continue.\n\n")

#PyGame Map Setup
pygame.init()
screen = pygame.display.set_mode((363, 480))
pygame.display.set_caption('Soccer Practice!')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Files/font/Pixeltype.ttf', 30)
  
#Character Creation
#Map + Score Setup
ground_surface = pygame.image.load('Files/soccerField.png').convert()
score = 0
score_surf = test_font.render('Score: '+str(score), False, 'black')
score_rect = score_surf.get_rect(center = (150,12.5))

#Defense Setup
snail_surf = pygame.image.load('Files/soccerDefense.png').convert_alpha()
snail_y_pos = 200
snail_rect = snail_surf.get_rect(midbottom = (120,200))

#Player Setup
player_surf = pygame.image.load('Files/soccerPlayer.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (25,120))

#Soccer Ball Setup
ball_surf = pygame.image.load('Files/soccerBall.png').convert_alpha()
ball_rect = ball_surf.get_rect(midleft = (50,120))

#Goal Setup
goal_surf = pygame.image.load('Files/soccergoal.png').convert_alpha()
goal_rect = goal_surf.get_rect(topleft = (322,216))

while True:
    for event in pygame.event.get():
        #Press X in top right to exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #Arrow Keys control movement of player
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_DOWN:
            player_rect.bottom += 12
            ball_rect.bottom += 12
          if event.key == pygame.K_UP:
            player_rect.bottom -= 12
            ball_rect.bottom -= 12
          if event.key == pygame.K_ESCAPE:
            print("Thanks for playing!")
            pygame.quit()
            sys.exit()
            
    #Positioning and color of map + score
    screen.blit(ground_surface,(0,0))
    pygame.draw.rect(screen, '#77DD77',score_rect)
    pygame.draw.rect(screen, '#77DD77',score_rect,10)
    screen.blit(score_surf,score_rect)
  
    #Movement of defender
    snail_rect.y += 3
    if snail_rect.bottom <= 0: 
      snail_rect.bottom = 490
    if snail_rect.bottom > 480:
      snail_rect.bottom = 0

    #Position of def, player, ball
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)
    screen.blit(ball_surf,ball_rect)
    screen.blit(goal_surf,goal_rect)
  
    #Spacebar controls ball
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
      ball_rect.x += 3
      
    #Player Boundaries
    if player_rect.bottom >= 505:
      player_rect.bottom = 505
    if player_rect.top <= 0:
      player_rect.top = 0

    
    #Ball Boundaries (bottom, top, right)
    if ball_rect.bottom >= 480:
      ball_rect.bottom = 480
    if ball_rect.top <= 25:
      ball_rect.top = 25
    if ball_rect.right >= 326:
      ball_rect.left = 50
      # myFinalLocation = ball_rect.right
      #print("My final location", myFinalLocation)
      again = input("Re-try? Y/N\n")
      if again == 'Y' or again == 'y':
        
        ball_rect.left = 50
      else:
        print("Thanks for playing!")
        pygame.quit()
        sys.exit()
    
    # ball_pos = pygame.Rect.get_pos()
    # print('collision')
    # if ball_rect.collidepoint((322,241)):
    # if myFinalLocation >241 and myFinalLocation<322:
    #   score += 1
    #   myScore(score_surf, score_rect, score)
      
    if ball_rect.colliderect(snail_rect):
      ball_rect.x -= 10
      print('This is not the goal.')
    if ball_rect.colliderect(goal_rect):
      print('GOAL!')
      score += 1
      score_surf = test_font.render('Score: '+str(score), False, 'black')
      score_rect = score_surf.get_rect(center = (150,12.5))

  
    # mouse_pos = pygame.mouse.get_pos()
    # print(mouse_pos)
    # if player_rect.collidepoint(mouse_pos):
    #   print('collision')
  #322,241
    pygame.display.update()
    clock.tick(60)

