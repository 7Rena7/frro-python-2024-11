from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock
from random import randint


class ConfettiParticle(Widget):
    def __init__(self, parent_width, parent_height, **kwargs):
        super(ConfettiParticle, self).__init__(**kwargs)
        self.size = (10, 10)
        self.pos = (randint(0, parent_width), parent_height)
        with self.canvas:
            Color(randint(0, 255) / 255.0, randint(0, 255) / 255.0, randint(0, 255) / 255.0)
            self.shape = Ellipse(pos=self.pos, size=self.size)
        self.speed_y = randint(-5, -1)
        self.speed_x = randint(-5, 5)

    def move(self):
        self.pos = (self.pos[0] + self.speed_x, self.pos[1] + self.speed_y)
        self.shape.pos = self.pos


class Confetti(Widget):
    def __init__(self, **kwargs):
        super(Confetti, self).__init__(**kwargs)
        self.particles = []
        Clock.schedule_once(self.create_particles, 0)  # Schedule the creation of particles

    def create_particles(self, dt):
        for _ in range(100):  # Number of particles
            particle = ConfettiParticle(self.width, self.height)
            self.particles.append(particle)
            self.add_widget(particle)
        Clock.schedule_interval(self.update, 1/60.)  # Update at 60 FPS

    def update(self, dt):
        for particle in self.particles:
            particle.move()
            if particle.y < 0:  # If particle is off the screen, reset its position
                particle.center = (randint(0, self.width), self.top)
