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
