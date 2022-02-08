#!/usr/bin/python3

##Script to communicate with hue

from phue import Bridge
import sys

b = Bridge('192.168.1.219')
b.get_api()
lights = b.lights

input = sys.argv[1]

def turn_off_lights():
    b.set_light([1,2,3,4],'on', False)
    for l in lights:
        l.brightness(254)
        
def turn_on_lights(): 
    b.set_light([1,2,3,4],'on', True)

if input=='on':
    turn_on_lights()
elif input=='off':
    turn_off_lights()