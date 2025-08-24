import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
def main():
	pygame.init()
	updatable = pygame.sprite.Group()
	drawable =  pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	asteroid_manager = AsteroidField()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill((0,0,0))
		for x in drawable:
			x.draw(screen)
		updatable.update(dt)
		for asteroid in asteroids:
			if player.collision(asteroid):
				return sys.exit("Game over!")
		for asteroid in asteroids:
			for shot in shots:
				if shot.collision(asteroid):
					split_results = asteroid.split()
					shot.kill()
					if split_results is not None:
						new_asteroid_pos, new_asteroid_neg = split_results
						asteroid_manager.spawn(new_asteroid_pos.radius, new_asteroid_pos.position, new_asteroid_pos.velocity)
						asteroid_manager.spawn(new_asteroid_neg.radius, new_asteroid_neg.position, new_asteroid_neg.velocity)
					else: 
						pass
		pygame.display.flip()
		dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main() 