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
import psutil
from libqtile.widget import base, GenPollText
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

class ThermalSensor(base.InLoopPollText):
    """Widget to display temperature sensor information"""

    defaults = [
        ("format", "{temp:.1f}{unit}", "Display string format. Three options available: ``{temp}`` - temperature, ``{tag}`` - tag of the temperature sensor, and ``{unit}`` - °C or °F"),
        ("metric", True, "True to use metric/C, False to use imperial/F"),
        ("update_interval", 2, "Update interval in seconds"),
        ("tag_sensor", None, 'Tag of the temperature sensor. For example: "temp1" or "Core 0"'),
        ("threshold", 70, "If the current temperature value is above, then change to foreground_alert colour"),
        ("foreground_alert", "ff0000", "Foreground colour alert"),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(ThermalSensor.defaults)
        temp_values = self.get_temp_sensors()

        if temp_values is None:
            self.data = "sensors command not found"
        elif len(temp_values) == 0:
            self.data = "Temperature sensors not found"
        elif self.tag_sensor is None:
            for k in temp_values:
                self.tag_sensor = k
                break

    def _configure(self, qtile, bar):
        self.unit = "°C" if self.metric else "°F"
        base.InLoopPollText._configure(self, qtile, bar)
        self.foreground_normal = self.foreground

    def get_temp_sensors(self):
        temperature_list = {}
        temps = psutil.sensors_temperatures(fahrenheit=not self.metric)
        empty_index = 0
        for kernel_module in temps:
            for sensor in temps[kernel_module]:
                label = sensor.label
                if not label:
                    label = "{}-{}".format(kernel_module if kernel_module else "UNKNOWN", str(empty_index))
                    empty_index += 1
                temperature_list[label] = sensor.current

        return temperature_list

    def poll(self):
        temp_values = self.get_temp_sensors()
        if (temp_values is None) or (self.tag_sensor not in temp_values):
            return "N/A"

        temp_value = temp_values.get(self.tag_sensor)
        if temp_value > self.threshold:
            self.layout.colour = self.foreground_alert
        else:
            self.layout.colour = self.foreground_normal

        val = dict(temp=temp_value, tag=self.tag_sensor, unit=self.unit)
        return self.format.format(**val)

class TemperatureIcon(GenPollText):
    defaults = [
        ('update_interval', 300, 'Update interval in seconds'),
        ('sensor', 'Core 0', 'Temperature sensor to read from'),
    ]

    def __init__(self, **config):
        GenPollText.__init__(self, func=self.poll, **config)
        self.add_defaults(TemperatureIcon.defaults)
        self.thermal_sensor = ThermalSensor(tag_sensor=self.sensor, metric=True)

    def poll(self):
        temperature = self.get_temperature()
        return self.select_icon(temperature)

    def get_temperature(self):
        temp_values = self.thermal_sensor.get_temp_sensors()
        if temp_values and self.sensor in temp_values:
            return temp_values[self.sensor]
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

# Audio Icon

class VolumeIcon(GenPollText):
    defaults = [
        ('font', 'FontAwesome', 'Font to use'),
        ('fontsize', None, 'Font pixel size. Calculated if None.'),
        ('padding', None, 'Padding between icon and text. Calculated if None.'),
        ('foreground', 'ffffff', 'Foreground color'),
    ]

    icons = {
        'low': '',     # FontAwesome icon for low volume
        'medium': '',  # FontAwesome icon for medium volume
        'high': '',    # FontAwesome icon for high volume
    }

    update_interval = 1
    low_threshold = 30
    medium_threshold = 60

    def __init__(self, **config):
        GenPollText.__init__(self, **config)
        self.add_defaults(VolumeIcon.defaults)

    def poll(self):
        volume = self.get_volume()
        if volume is None:
            return ''
        return self.select_icon(volume)

    def get_volume(self):
        try:
            result = subprocess.run(
                ["pactl", "get-sink-volume", "@DEFAULT_SINK@"],
                stdout=subprocess.PIPE,
                text=True
            ).stdout

            if not result:
                return None

            # Extract the volume percentage from the pactl output
            volume = int(result.split('/')[1].strip().replace('%', ''))
            return volume
        except Exception as e:
            return None

    def select_icon(self, volume):
        if volume < self.low_threshold:
            return self.icons['low']
        elif volume < self.medium_threshold:
            return self.icons['medium']
        else:
            return self.icons['high']