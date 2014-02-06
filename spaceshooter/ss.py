import math, random
from livewires import games, color

games.init(screen_width = 640, screen_height = 480, fps = 50)

class Wrapper(games.Sprite):
    """ A sprite that wraps around the screen. """
    def update(self):
        """ Wrap sprite around screen. """    
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0
            
        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Destroy self. """
        self.destroy()   

class Collider(Wrapper):
    """ A Wrapper that can collide with another object. """
    def update(self):
        """ Check for overlapping sprites. """
        super(Collider, self).update()
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

class Fly(Wrapper):
    """ Alien floats across the screen. """
    image = games.load_image("fly1.bmp", transparent = True)
    
    SPEED = 2
    SPAWN = 2
    POINTS = 30
    total =  0
    
    def __init__(self, game, x, y):
        """ Initialize Fly sprite"""
        Fly.total += 1
        
        super(Fly, self).__init__(
            image = Fly.image,
            x = random.randint(40, 500),
            y = 50,
            dx = (random.randint(3, 6) -.75),
            dy = (random.randint(1, 2) -.75))

        self.game = game

    def update(self):
        """ Check for collision / Bounce of edges"""
        games.screen._update_display()
        if self.right > games.screen.width:
            self.dx = -self.dx
        if self.left <= 0:
            self.dx = -self.dx
        if self.bottom >= 450:
            games.screen.clear()
            self.destroy()
            self.game.end()

    def die(self):
        """ Destroy Fly. """
        Fly.total -= 1
        self.destroy()
        new_explosion = Explosion(x = self.x, y = self.y)
        games.screen.add(new_explosion)
        self.destroy()

        self.game.score.value += Fly.POINTS
        self.game.score.right = games.screen.width - 10

        self.game.advance()


class Ship(Collider):
    """ The player's ship. """
    image = games.load_image("ship.bmp", transparent = True)
    MISSILE_DELAY = 25

    def __init__(self, game, x, y):
        """ Initialize ship sprite. """
        super(Ship, self).__init__(image = Ship.image, x = 300, y = 420)
        self.game = game
        self.missile_wait = 0

    def update(self):
        """ fire missiles and move based on keys pressed. """
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= 5
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += 5

        if self.x > 615:
            self.x = 615
            
        if self.x < 29:
            self.x = 29
            
        if self.missile_wait > 0:
            self.missile_wait -= 1
              
        if (games.keyboard.is_pressed(games.K_SPACE)) and (self.missile_wait == 0):
            new_missile = Missile(self.x, self.y, dy = 7)
            games.screen.add(new_missile)        
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        self.game.end()
        super(Ship, self).die()

class Missile(Collider):
    """ A missile launched by the your ship. """
    image = games.load_image("missile.bmp", transparent = True)
    sound = games.load_sound("missile.wav")
    BUFFER = -50
    VELOCITY_FACTOR = -7
    LIFETIME = 50

    def __init__(self, ship_x, ship_y, dy):
        """ Initialize missile sprite. """
        Missile.sound.play()

        # Calc Start Position
        x = ship_x
        y = ship_y + Missile.BUFFER

        # Velocity
        dy = Missile.VELOCITY_FACTOR
        
        # create the missile
        super(Missile, self).__init__(image = Missile.image,
                                      x = x,
                                      y = y,
                                      dy = dy)
        self.lifetime = Missile.LIFETIME
                                      
    def update(self):
        """ Move the missile. """
        super(Missile, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    """ Explosion animation. """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images = Explosion.images,
                                        x = x, y = y,
                                        repeat_interval = 4, n_repeats = 1,
                                        is_collideable = False)
        Explosion.sound.play()


class Game(object):
    """ The game itself. """
    def __init__(self):
        """ Initialize Game object. """
        # set level, score , ship sound and add it to the screen. Then make ship
        self.level = 0
        self.sound = games.load_sound("level.wav")
        self.score = games.Text(value = 0,
                                size = 30,
                                color = color.white,
                                top = 5,
                                right = games.screen.width - 10,
                                is_collideable = False)
        games.screen.add(self.score)
        self.ship = Ship(game = self, 
                         x = games.screen.width/2,
                         y = games.screen.height/2)
        games.screen.add(self.ship)


    def play(self):
        """ Play the game. """
        games.music.load("theme.mid")
        games.music.play(-1)
        wall_image = games.load_image("background.bmp")
        games.screen.background = wall_image
        self.advance()
        games.screen.mainloop()

    def advance(self):
        """ Advance to the next game level. """
        self.level += 1
        
        # amount of space around ship to preserve when creating asteroids
        BUFFER = 150
     
        # create new asteroids 
        if Fly.total >= 1:
            #min distance
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # x and y axis
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)
            
            # location and wrap
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            x %= games.screen.width
            y %= games.screen.height


            new_fly = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly)
            Fly.total -= 1
            new_fly_2 = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly_2w )
            Fly.total -= 1
            
            new_fly_3 = Fly(game = self,x = x, y = y)
            new_fly_4 = Fly(game = self,x = x, y = y)
            new_fly_5 = Fly(game = self,x = x, y = y)

        else:
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)
            x = self.ship.x + x_distance
            y = self.ship.y + y_distance
            x %= games.screen.width
            y %= games.screen.height
            new_fly_1 = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly_1)
            Fly.total -= 1
            
            new_fly_2 = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly_2)
            Fly.total -= 1
            
            new_fly_3 = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly_3)
            Fly.total -= 1
            
            new_fly_4 = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly_4)
            Fly.total -= 1
            
            new_fly_5 = Fly(game = self,x = x, y = y)
            games.screen.add(new_fly_5)
            Fly.total -= 1

        level_message = games.Message(value = "Ready? FIGHT! " + str(self.level),
                                      size = 40,
                                      color = color.yellow,
                                      x = games.screen.width/2,
                                      y = games.screen.width/10,
                                      lifetime = 3 * games.screen.fps,
                                      is_collideable = False)
        games.screen.add(level_message)

        if self.level > 1:
            self.sound.play()
            
    def end(self):
        """ End the game. """
        end_message = games.Message(value = "Game Over.",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit,
                                    is_collideable = False)
        games.screen.add(end_message)


swarm = Game()
swarm.play()

