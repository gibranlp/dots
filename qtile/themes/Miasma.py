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
from custom_widgets import InternetIcon, VolumeIcon

widget_defaults = dict(
    font=main_font,
    fontsize=font_size,
    padding=4,
)

# Theme
## Screens

def init_widgets_list():
  widgets_list = [
    widget.TextBox(
      foreground=color[1],
      background=transparent,
      padding=-1,
      fontsize=font_size+5,
      text="░▒▓",
    ),
    widget.CurrentLayout(
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
      background=color[1],
      foreground=color[0],
      scale=0.8,
    ),
    widget.TextBox(
      foreground=color[2],
      background=color[1],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.CPU(
      foreground=color[0],
      background=color[2],
      format='{load_percent}%',
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
    ),
    widget.TextBox(
      foreground=color[3],
      background=color[2],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.Memory(
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      background=color[3],
      foreground=color[0],
      format='{MemUsed:.0f}{mm}',
      measure_mem='M',
    ),
    widget.TextBox(
      foreground=color[4],
      background=color[3],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.WindowName(
      background=color[4],
      foreground=color[0],
      width=widget_width,
      format='{state} {name}',
      scroll=True,
      scroll_delay=2,
      scroll_repeat=True,
      scroll_step=1,
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
    ),
    widget.TextBox(
      foreground=color[5],
      background=color[4],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.Mpris2(
      background=color[5],
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal  + " -e cava")},
      objname=None,
      foreground=color[0],
      width=widget_width,
      format='{xesam:artist}  {xesam:title}',
      stopped_text="Stop",
      paused_text='  ',
      scroll=True,
      scroll_repeat=True,
      scroll_delay=0.1,
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
    ),
    widget.TextBox(
      foreground=color[6],
      background=color[5],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.Pomodoro(
      background=color[6],
      foreground=color[0],
      color_active=color[0],
      color_break=color[0],
      color_inactive=color[0],
      length_long_break=30,
      length_pomodori=45,
      length_short_break=15,
      notification_on=True,
      num_pomodori=3,
      prefix_active='󰦖 ',
      prefix_inactive='󰦖',
      prefix_break='',
      prefix_long_break='󱐟',
      prefix_paused='󱖒',
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
    ),
    widget.TextBox(
      foreground=secondary_color[1],
      background=color[6],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.Prompt(
      background=secondary_color[1],
      prompt=prompt,
      foreground=color[0],
      cursor_color=color[0],
      visual_bell_color=[0],
      visual_bell_time=0.2,
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
    ),
    widget.TextBox(
      foreground=secondary_color[1],
      background=transparent,
      padding=-1,
      fontsize=font_size+5,
      text="▓▒░",
    ),
    widget.WidgetBox(
      decorations=[RectDecoration(colour=color[0], radius=8, filled=True, padding_x=4, padding_y=8)],
      text_closed='',
      text_open='',
      foreground=color[2],
      widgets=[
          widget.Spacer(
          length=5,
          background=transparent,
    ),
          widget.Systray(),]
    ),
    widget.Spacer(
      length=bar.STRETCH,
      background=transparent,
    ),
    widget.TextBox(
      foreground=color[0],
      background=transparent,
      padding=-1,
      fontsize=font_size+5,
      text="░▒▓",
    ),
    widget.GroupBox(
      background=color[0],
      fontsize=groups_font,
      disable_drag=True,
      hide_unused=hide_unused_groups,
      borderwidth=0,
      active=color[6], #Program opened in that group
      inactive=secondary_color[0], # Empty Group
      rounded=False,
      highlight_method="block",
      this_current_screen_border=color[1],
      center_aligned = True,
      other_curren_screen_border=color[1],   
      urgent_border="fc0000",
      decorations=[BorderDecoration(colour=color[1], border_width=2)],
      block_highlight_text_color=color[0],
      #visible_groups=['Escape','1','2','3','4'],
    ),
    widget.TextBox(
      foreground=color[0],
      background=transparent,
      padding=-1,
      fontsize=font_size+5,
      text="▓▒░",
    ),
    widget.Spacer(
      length=bar.STRETCH,
      background=transparent,
    ),
    widget.TextBox(
      foreground=secondary_color[3],
      background=transparent,
      padding=-1,
      fontsize=font_size+5,
      text="░▒▓",
    ),
    ## Network
    InternetIcon(
      font=symbols_font,
      background=secondary_color[3],
      update_interval=1,
      foreground=color[0],
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
      decorations=[BorderDecoration(colour=color[0], border_width=[2,0,2,2])],
      padding=5,
    ),
    widget.Wlan(
      background=secondary_color[3],
      interface=wifi,
      format='{essid} {percent:2.0%}',
      disconnected_message='󰱟',
      foreground=color[0],
      width=widget_width -50,
      scroll=True,
      scroll_repeat=True,
      scroll_interval=0.1,
      scroll_step=1,
      update_interval=1,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
      decorations=[BorderDecoration(colour=color[0], border_width=[2,0,2,0])],
      padding=5,
    ),
    widget.Net(
      prefix='M',
      interface=wifi,
      format='{down:1.1f}M',
      foreground=color[0],
      use_bits=True,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
      background=secondary_color[3],
      decorations=[BorderDecoration(colour=color[0], border_width=[2,2,2,0])],
      padding=5,
    ),
    widget.TextBox(
      foreground=color[5],
      background=secondary_color[3],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    VolumeIcon(
      background=color[5],
      foreground=color[0],
      mouse_callbacks={'Button1': lambda: qtile.function(audio_widget),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
    ),
    widget.ALSAWidget(
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      background=color[5],
      device='Master',
      bar_colour_high=color[0],
      bar_colour_normal=color[0],
      bar_colour_mute=color[1],
      hide_interval=2,
      update_interval=0.1,
      bar_width=50,
      mode='bar',
      text_format=' ',
    ),
    widget.TextBox(
      foreground=color[3],
      background=secondary_color[2],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.Clock(
      foreground=color[0],
      format="%a %d %H:%M",
      update_interval=1,
      background=color[3],
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
      decorations=[BorderDecoration(colour=color[0], border_width=2)],
      padding=5,
    ),
    widget.TextBox(
      background=color[3],
      foreground=secondary_color[2],
      padding=-1,
      fontsize=font_size+5,
      text="░",
    ),
    widget.UPowerWidget(
        border_charge_colour=secondary_color[0],
        border_colour=color[0],
        border_critical_colour='#cc0000',
        fill_critical='#cc0000',
        fill_low='#FF5511',
        decorations=[BorderDecoration(colour=color[0], border_width=2)],
        fill_normal=color[0],
        foreground=color[0],
        background=secondary_color[2],
        percentage_critical=0.2,
        percentage_low=0.4,
        text_charging=' ({percentage:.0f}%) {ttf} to ',
        text_discharging=' ({percentage:.0f}%) {tte} Left',
        margin=5,
    ),
    widget.TextBox(
      foreground=secondary_color[2],
      background=transparent,
      padding=-1,
      text="▓▒░",
      fontsize=font_size+5,
    ),
    ]
  return widgets_list

def screen1_widgets():
    widgets_screen1=init_widgets_list()
    return widgets_screen1


def init_screens_bottom():
    return[Screen(bottom=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

def init_screens_top():
    return[Screen(top=bar.Bar(widgets=screen1_widgets(),size=bar_size,background=transparent,margin=bar_margin))]

if bar_position == "top":
    screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()