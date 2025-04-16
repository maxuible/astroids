import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (updatables, drawables, shots)
    AsteroidField.containers = (updatables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()





    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        for astroid in asteroids:
            for shot in shots:
                if astroid.collision(shot):
                    shot.kill()
                    astroid.split()
                    
            if astroid.collision(player):
                print("Gamer over!")
                sys.exit(0)

        screen.fill(color="black")
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()