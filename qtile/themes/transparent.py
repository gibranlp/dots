# _____             _                 _____ _____ 
#|   __|___ ___ ___| |_ ___ _ _ _____|     |   __|
#|__   | . | -_|  _|  _|  _| | |     |  |  |__   |
#|_____|  _|___|___|_| |_| |___|_|_|_|_____|_____|
#      |_|   
# SpectrumOS - Embrace the Chromatic Symphony!
# By: gibranlp <thisdoesnotwork@gibranlp.dev>
# MIT licence 
#
from functions import *
from custom_widgets import InternetIcon, TemperatureIcon, VolumeIcon

widget_defaults = dict(
  font=main_font,
  fontsize=font_size,
  padding=4,
)
# Theme

## Screens
def init_widgets_list():
  widgets_list = [
    widget.GroupBox(
      fontshadow=color[0],
      fontsize=groups_font,
      disable_drag=True,
      hide_unused=hide_unused_groups,
      borderwidth=0,
      active=secondary_color[4], #Program opened in that group
      inactive=secondary_color[6], # Empty Group
      rounded=False,
      highlight_method="text",
      this_current_screen_border=secondary_color[1],
      center_aligned = True,
      other_curren_screen_border=secondary_color[1],   
      urgent_border="fc0000",
      block_highlight_text_color=color[1],
    ),

    widget.Spacer(
      length=4,
    ),

    widget.Visualizer(
      bar_colour=secondary_color[2],
      bars=30,
      framerate=60,
      spacing=0,
      width=200,
      channels='stereo',
    ),

    widget.Spacer(
      length=4,
    ),

    widget.Chord(
      background=color[0]+"FF",
      fontshadow=color[0],
      foreground=secondary_color[3],
    ),
    
    widget.Prompt(
      background=color[0]+"DD",
      fontshadow=color[0],
      prompt=prompt,
      foreground=secondary_color[4],
      cursor_color=secondary_color[4],
      visual_bell_color=[4],
      visual_bell_time=0.2,
    ),
    
    widget.Spacer(
      length=bar.STRETCH,
    ),

    # widget.Visualizer(
    #   fontshadow=color[0],
    #   bar_colour=secondary_color[2],
    # ),

    widget.Mpris2(
      fontshadow=color[0],
      mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle("music")},
      objname=None,
      foreground=secondary_color[2],
      width=widget_width,
      format='{xesam:artist} - {xesam:title}',
      stopped_text="Stop",
      paused_text='  ',
      scroll=True,
      scroll_repeat=True,
      scroll_delay=0.1,
    ),

    widget.Spacer(
      length=bar.STRETCH,
    ),

    widget.CPUGraph(
       border_color=transparent,
       type='line',
       graph_color=secondary_color[1],
       line_width=2,
    ),

    widget.Spacer(
      length=4,
    ),

    TemperatureIcon(
       background=color[0]+"DD",
       fontshadow=color[0],
       fontsize=font_size+3,
       foreground=secondary_color[5],
       mouse_callbacks = {'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && sensors; exec zsh'")},
       update_interval=1, 
       tag_sensor='Composite',
    ),
    
    widget.ThermalSensor(
      background=color[0]+"AA",
      fontshadow=color[0],
      format='{temp:.1f}{unit}',
      foreground=secondary_color[5],
      tag_sensor='Composite',
      mouse_callbacks = {'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && sensors; exec zsh'")},
      update_interval=1,
    ),

    widget.Spacer(
      length=4,
    ),

    widget.Wttr(
      fontshadow=color[0],
      foreground=secondary_color[3],
      location={'': ''},
      update_interval=300,
      format='%c',
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'curl wttr.in; exec zsh'")},
    ),

    widget.Wttr(
      fontshadow=color[0],
      foreground=secondary_color[3],
      location={'':''},
      update_interval=300,
      format='%t',
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'curl wttr.in; exec zsh'")},
    ),

    widget.Spacer(
      length=4,
    ),
    
    InternetIcon(
      background=color[0]+"DD",
      fontshadow=color[0],
      update_interval=1,
      foreground=secondary_color[4],
      font=symbols_font,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),
    
    widget.Wlan(
      background=color[0]+"AA",
      fontshadow=color[0],
      interface=wifi,
      format='{essid}',
      disconnected_message='󰱟',
      foreground=secondary_color[4],
      width=widget_width -20,
      scroll=True,
      scroll_repeat=True,
      scroll_interval=0.1,
      scroll_step=1,
      update_interval=1,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),
    
    widget.Net(
      prefix='M',
      interface=wifi,
      format='{down:1.1f}M',
      foreground=secondary_color[4],
      use_bits=True,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
      background=color[0]+"AA",
      fontshadow=color[0],
    ),

    widget.Spacer(
      length=4,
    ),

    widget.Spacer(
      length=4,
    ),

    VolumeIcon(
      fontshadow=color[0],
      foreground=secondary_color[4],
      mouse_callbacks={'Button1': lambda: qtile.function(audio_widget),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
    ),

    widget.Spacer(
      length=4,
    ),

    widget.Clock(
      background=color[0]+"AA",
      fontshadow=color[0],
      foreground=color[6],
      format="%a %d %H:%M",
      update_interval=1,
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
    ),

    widget.Spacer(
      length=4,
    ),
    widget.StatusNotifier(
      fontshadow=color[0],
    ),

    widget.Spacer(
      length=4,
      background=color[0]+"AA",
    ),

    widget.UPowerWidget(
      background=color[0]+"AA",
      fontshadow=color[0],
      border_charge_colour=secondary_color[7],
      border_colour=secondary_color[3],
      border_critical_colour='#cc0000',
      fill_critical='#cc0000',
      fill_low='#FF5511',
      fill_normal=secondary_color[3],
      foreground=secondary_color[3],
      percentage_critical=0.2,
      percentage_low=0.4,
      text_charging=' ({percentage:.0f}%) {ttf} to ',
      text_discharging=' ({percentage:.0f}%) {tte} Left',
    ),
    widget.Spacer(
      length=4,
      background=color[0]+"AA",
    ),
    ]
  return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1

def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=color[0]+"66",margin=[bar_margin[0], bar_margin[1],bar_margin[2],bar_margin[3]]))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=color[0]+"66",margin=[bar_margin[0], bar_margin[1],bar_margin[2],bar_margin[3]]))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()