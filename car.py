from pyglet.sprite import Sprite
import math
from pyglet.shapes import Line
class Radar:
    max_length_pixels = 200

    def __init__(self, angle, batch):
        self.angle = angle
        self.beam = Line(0,0,0,0,width = 2, color = (255,255,255,127), batch=batch)

class Car:
    max_speed = 6.0
    slipping_speed = max_speed * 0.5

    def __init__(self,network, track, image, batch):
        self.network = network
        self.track = track
        image.anchor_x = 25
        image.anchor_y = 25
        self.body = Sprite(image, batch=batch)
        self.body.x, self.body.y = track.checkpoints[0]
        self.radars = Radar(-70, batch), Radar(-35, batch), Radar(0, batch), Radar(35, batch), Radar(70, batch)
        self.speed = 0.0
        self.rotation = 0.0
        self.is_running = True
        self.last_checkpoint_passed = 0
        self.least_edge_distance = 100

    def update(self, delta_time):
        render_speed = delta_time * 60
        self.speed -=0.05 #friction
        if self.is_running:
            measurements = [self.probe(radar)/radar.max_length_pixels for radar in self.radars]
            acceleration, steer_position = self.network.feed_forward(measurements)
            
            if acceleration > 0:
                self.speed +=0.1
        
            if self.speed > self.max_speed:
                self.speed = self.max_speed

            if self.speed > self.slipping_speed: 
                steer_impact = -self.speed / self.max_speed + self.slipping_speed / self.max_speed + 1
            
            else:
                steer_impact = 1


            self.rotation -= steer_position * self.speed * steer_impact * render_speed * 3
        
        else:
            self.speed -= 0.05 * self.speed

        if self.speed < 0:
            self.speed = 0
            self.shut_off()
        

       
        self.body.rotation = -self.rotation
        self.body.x +=self.speed * render_speed * math.cos(math.radians(self.rotation))
        self.body.y +=self.speed * render_speed * math.sin(math.radians(self.rotation))

    def probe(self, radar):
        probe_length = 0
        radar.beam.x = self.body.x
        radar.beam.y = self.body.y
        x2 = radar.beam.x
        y2 = radar.beam.y
        while probe_length < radar.max_length_pixels and self.track.is_road(x2, y2):
            probe_length += 2
            x2 =self.body.x + probe_length*math.cos(math.radians(self.rotation + radar.angle))
            y2 =self.body.y + probe_length*math.sin(math.radians(self.rotation + radar.angle))
        radar.beam.x2 = x2
        radar.beam.y2 = y2
        if probe_length < self.least_edge_distance:
            self.least_edge_distance = probe_length
        return probe_length   
    
    def hit_checkpoint(self, id):
        #print(id)
        if id - self.last_checkpoint_passed == 1:
            self.last_checkpoint_passed = id

        elif id < self.last_checkpoint_passed:
            self.shut_off()
     
    def shut_off(self):
        self.is_running = False
        self.radars = None