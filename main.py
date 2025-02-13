# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import *
from constants import *
from player import *
from circleshape import *
from asteroidfield import *

def main() :
    pygame.init()
    print("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clk = pygame.time.Clock()
    dt = 0

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.checkCollisions(player) == True :
                print("Game over!")
                sys.exit()

            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.checkCollisions(shot) == True :
                        asteroid.split()

        for item in drawable:
            item.draw(screen)
    
        pygame.display.flip()
        dt = clk.tick(60)/1000

if __name__ == "__main__":
    main()