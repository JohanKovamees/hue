
##Script to communicate with hue

from os import getenv
from phue import Bridge
from flask import Flask, request
import sys

secret_key = getenv("FLASK_KEY")

hue_ip = getenv("HUE_IP")
b = Bridge(hue_ip)
b.get_api()
lights = b.get_light_objects('id')

def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/off')
    def turn_off_lights():
        for l in lights:
            b.set_light([l],'on', False)
        return "Turning Off"
        
    @app.route('/on')
    def turn_on_lights(): 
        for l in lights:
            b.set_light([l],'on', True)
            lights[l].brightness = 254
        return "Turning On"

    @app.route('/cozy')
    def cozy():
        for l in lights:
            b.set_light([l],'on', True)
            lights[l].brightness = 127
        return "Turning Cozy"
    
    @app.route('/night')
    def night():
        for l in lights:
            b.set_light([l],'on', True)
            lights[l].brightness = 1
        return "Night"

    if __name__ == '__main__':
        app.run(host='0.0.0.0',debug=False,use_debugger=False, use_reloader=False)
    
    return app

#elif script_arg=="print":
#    for l in lights:
#        print(l.name)
