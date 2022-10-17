#!/usr/bin/python3

##Script to communicate with hue

from phue import Bridge
import sys

b = Bridge('10.0.1.195')
b.get_api()
#lights = b.lights
lights = b.get_light_objects('id')

script_arg = sys.argv[1]

def turn_off_lights():
    b.set_light([8,9,10,11,12,13],'on', False)
        
def turn_on_lights(): 
    b.set_light([8,9,10,11,12,13],'on', True)
    lights[8].brightness = 254
    lights[9].brightness = 254
    lights[10].brightness = 254
    lights[11].brightness = 254
    lights[12].brightness = 254
    lights[13].brightness = 254

def cozy():
    b.set_light([8,9,10,11,12,13],'on', True)
    lights[8].brightness = 120
    lights[9].brightness = 120
    lights[10].brightness = 120
    lights[11].brightness = 120
    lights[12].brightness = 120
    lights[13].brightness = 120

if script_arg=='on':
    turn_on_lights()
elif script_arg=='off':
    turn_off_lights()
elif script_arg=="cozy":
    cozy()

#elif script_arg=="print":
#    for l in lights:
#        print(l.name)
