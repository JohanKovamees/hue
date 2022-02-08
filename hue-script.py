#!/usr/bin/python3

##Script to communicate with hue

from phue import Bridge
import sys

b = Bridge('192.168.1.219')
b.get_api()
#lights = b.lights
lights = b.get_light_objects('id')

script_arg = sys.argv[1]

def turn_off_lights():
    b.set_light([1,2,3,4],'on', False)
        
def turn_on_lights(): 
    b.set_light([1,2,3,4],'on', True)
    lights[1].brightness = 254
    lights[2].brightness = 254
    lights[3].brightness = 254
    lights[4].brightness = 254

if script_arg=='on':
    turn_on_lights()
elif script_arg=='off':
    turn_off_lights()
#elif script_arg=="print":
#    for l in lights:
#        print(l.name)