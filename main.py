# Standard imports
import sys

# Third-party imports
import pygame

# Local imports
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    player_object = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collisions(player_object):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collisions(shot):
                    asteroid.split()
                    shot.kill()
         
        screen.fill("black")

        for obj in drawable:
            #print("Drawing:", type(obj).__name__)
            obj.draw(screen)

        pygame.display.flip()
    
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()