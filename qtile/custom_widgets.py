# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
# 

## Internet Icon Widget
from qtile_extras.widget.decorations import (BorderDecoration,PowerLineDecoration,RectDecoration)
from libqtile import widget
import subprocess

class InternetIcon(widget.GenPollText):
    defaults = [
        ('update_interval', 5, 'Update interval in seconds'),
    ]

    def __init__(self, **config):
        widget.GenPollText.__init__(self, func=self.poll, **config)
        self.add_defaults(InternetIcon.defaults)

    def poll(self):
        if self.is_ethernet_connected():
            return 'network-wired'  # Ethernet icon
        signal_strength = self.get_wifi_signal_strength()
        return self.select_text(signal_strength)

    def is_ethernet_connected(self):
        try:
            # Check for Ethernet connection using nmcli
            result = subprocess.run(
                ["nmcli", "device", "status"],
                stdout=subprocess.PIPE,
                text=True
            ).stdout

            # Check if any Ethernet interface is connected
            for line in result.split('\n'):
                if 'ethernet' in line and 'connected' in line:
                    return True
            return False
        except Exception as e:
            return False

    def get_wifi_signal_strength(self):
        try:
            # Get the Wi-Fi signal strength using nmcli
            result = subprocess.run(
                ["nmcli", "-t", "-f", "ACTIVE,SIGNAL", "dev", "wifi"],
                stdout=subprocess.PIPE,
                text=True
            ).stdout

            # Find the line with ACTIVE:yes, which means the connected network
            active_wifi = [line for line in result.split('\n') if 'yes' in line]
            if active_wifi:
                signal_strength = int(active_wifi[0].split(':')[-1])
                return signal_strength
        except Exception as e:
            return 0

    def select_text(self, signal_strength):
        if signal_strength >= 66:
            text = 'wifi'
        elif signal_strength >= 33:
            text = 'wifi-fair'
        else:
            text = 'wifi-weak'
        
        return text

## Thermal Icon

class TemperatureIcon(widget.GenPollText):
    defaults = [
        ('update_interval', 300, 'Update interval in seconds'),
        ('sensor', 'Core 0', 'Temperature sensor to read from'),
    ]

    def __init__(self, **config):
        widget.GenPollText.__init__(self, func=self.poll, **config)
        self.add_defaults(TemperatureIcon.defaults)

    def poll(self):
        temperature = self.get_temperature()
        return self.select_icon(temperature)

    def get_temperature(self):
        try:
            # Read the temperature from the specified sensor
            result = subprocess.run(
                ["cat", f"/sys/class/thermal/{self.sensor}/temp"],
                stdout=subprocess.PIPE,
                text=True
            ).stdout.strip()
            temperature = int(result) / 1000.0  # Convert from millidegrees to degrees
            return temperature
        except Exception as e:
            return None

    def select_icon(self, temperature):
        if temperature is None:
            return ''  # Default to very cold icon if reading fails
        if temperature < 40:
            return ''
        elif temperature < 65:
            return ''
        elif temperature < 71:
            return ''
        else:
            return '<span color="#FF0000"></span>'  # Hot


### Tests
