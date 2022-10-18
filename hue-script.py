#!/usr/bin/python3

##Script to communicate with hue

from phue import Bridge
import sys

b = Bridge('10.0.1.195')
b.get_api()

lights = b.get_light_objects('id')

script_arg = sys.argv[1]

def turn_off_lights():
    for l in lights:
        b.set_light([l],'on', False)
        
def turn_on_lights(): 
    for l in lights:
        b.set_light([l],'on', True)
        lights[l].brightness = 254

def cozy():
    for l in lights:
        b.set_light([l],'on', True)
        lights[l].brightness = 127

if script_arg=='on':
    turn_on_lights()
elif script_arg=='off':
    turn_off_lights()
elif script_arg=="cozy":
    cozy()

#elif script_arg=="print":
#    for l in lights:
#        print(l.name)
