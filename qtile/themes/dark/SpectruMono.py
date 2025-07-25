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
from qtile_extras import widget

pbackground = secondary_color[0]
pforeground = secondary_color[1]

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
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      foreground=pforeground,
      text="",
      font=symbols_font,
    ),
    
    widget.CPU(
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
      foreground=pbackground,
      format='{load_percent}%'
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.TextBox(
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      foreground=pforeground,
      text="",
      font=symbols_font,
    ),
    
    widget.Memory(
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
      foreground=pbackground,
      format='{MemUsed:.0f}{mm}',
      measure_mem='M',
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.TextBox(
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      foreground=pforeground,
      text="",
      font=symbols_font,
    ),
    
    widget.WindowName(
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
      foreground=pbackground,
      width=widget_width,
      format='{name}',
      scroll=True,
      scroll_delay=2,
      scroll_repeat=True,
      scroll_step=1,
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.TextBox(
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      text="󰝚",
      foreground=pforeground,
      font=symbols_font,
    ),
    
    widget.Mpris2(
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
      mouse_callbacks={'Button1': lazy.group['scratchpad'].dropdown_toggle("music")},
      objname=None,
      foreground=pbackground,
      width=widget_width,
      format='{xesam:artist} - {xesam:title}',
      stopped_text="Stop",
      paused_text='  ',
      scroll=True,
      scroll_repeat=True,
      scroll_delay=0.1,
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.Pomodoro(
      decorations=[RectDecoration(colour=pforeground, radius=7, filled=True)],
      foreground=pbackground,
      color_active=pbackground,
      color_break=pbackground,
      color_inactive=pbackground,
      length_long_break=30,
      length_pomodori=45,
      length_short_break=15,
      notification_on=True,
      font=symbols_font,
      num_pomodori=3,
      prefix_active='󰦖 ',
      prefix_inactive='󰦖',
      prefix_break='',
      prefix_long_break='󱐟',
      prefix_paused='󱖒',
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    widget.WidgetBox(
      decorations=[RectDecoration(colour=pforeground, radius=4, filled=True)],
      text_closed='',
      text_open='',
      foreground=pbackground,
      width=26,
      widgets=[
          widget.Spacer(
          length=5,
          background=transparent,
    ),
    
    widget.StatusNotifier(),]
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.Prompt(
      decorations=[RectDecoration(colour=pbackground, radius=7, filled=True)],
      prompt=prompt,
      foreground=pforeground,
      cursor_color=pforeground,
      visual_bell_color=[4],
      visual_bell_time=0.2,
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.Chord(
      decorations=[RectDecoration(colour=pbackground, radius=7, filled=True)],
      foreground=color[1],
    ),
    
    widget.Spacer(
      length=bar.STRETCH,
      background=transparent,
    ),
    
    widget.GroupBox(
      decorations=[RectDecoration(colour=pbackground, radius=8, filled=True)],
      fontsize=groups_font,
      disable_drag=True,
      hide_unused=hide_unused_groups,
      borderwidth=0,
      active=color[1], #Program opened in that group
      inactive=third_color[0], # Empty Group
      rounded=False,
      highlight_method="text",
      this_current_screen_border=pforeground,
      center_aligned = True,
      other_curren_screen_border=pforeground,   
      urgent_border="fc0000",
    ),
    
    widget.Spacer(
      length=bar.STRETCH,
      background=transparent,
    ),

    widget.CheckUpdates(
       decorations=[RectDecoration(colour=color[2], radius=7, filled=True)],
       distro='Arch_paru',
       colour_have_updates=color[0],
       colour_no_updates=color[0],
       display_format='󰁠',
       no_update_string='󱧧',
       update_interval=60,
       execute='paru -Syu',
       fontsize=font_size+3,
       mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'source ~/.zshrc && paru -Syu --noconfirm --nocheck; exec zsh'")},
       width=24
    ),

    widget.Spacer(
      length=5,
      background=transparent,
    ),

    widget.DoNotDisturb(
      decorations=[RectDecoration(colour=pforeground, radius=7, filled=True)],
      foreground=color[0],
      enabled_icon="󰂛",
      disabled_icon="󰂞",
      width=24,
    ),

    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    *([widget.Wttr(
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      foreground=pforeground,
      location={'': ''},
      update_interval=300,
      format='%c',
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'curl wttr.in; exec zsh'")},
    )] if weather_widget else []),

    *([widget.Wttr(
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
      foreground=pbackground,
      location={'':''},
      update_interval=300,
      format='%t',
      mouse_callbacks={'Button1': lambda: qtile.spawn(terminal + " -e zsh -c 'curl wttr.in; exec zsh'")},
    )] if weather_widget else []),
    
    *([widget.Spacer(
      length=5,
      background=transparent,
    )] if weather_widget else []),

    InternetIcon(
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      update_interval=1,
      foreground=pforeground,
      font=symbols_font,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)}
    ),
    
    widget.Wlan(
      decorations=[RectDecoration(colour=pforeground, radius=0, filled=True)],
      interface=wifi,
      format='{essid}',
      disconnected_message='󰱟',
      foreground=pbackground,
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
      foreground=pbackground,
      use_bits=True,
      mouse_callbacks={'Button1':lambda: qtile.function(network_widget)},
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    VolumeIcon(
      decorations=[RectDecoration(colour=pbackground, radius=[7,0,0,7], filled=True)],
      foreground=pforeground,
      mouse_callbacks={'Button1': lambda: qtile.function(audio_widget),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
      width=23
    ),
    
    widget.ALSAWidget(
      decorations=[RectDecoration(colour=pbackground, radius=0, filled=True)],
      device='Master',
      bar_colour_high=pforeground,
      bar_colour_normal=pforeground,
      bar_colour_mute=pforeground,
      hide_interval=2,
      update_interval=0.1,
      bar_width=50,
      mode='bar',
      text_format=' ',
    ),
    
    widget.TextBox(
      decorations=[RectDecoration(colour=pbackground, radius=[0,7,7,0], filled=True)],
      text=" ",
      foreground=pforeground,
      mouse_callbacks={'Button1': lambda: qtile.spawn('pavucontrol'),'Button4': lambda: qtile.spawn("amixer -q set Master 5%+ && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True),'Button5': lambda: qtile.spawn("amixer -q set Master 5%- && dunstify -a Volume ' '$(pamixer --get-volume-human) -h int:value:$(pamixer --get-volume)", shell=True)},
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.Clock(
      foreground=pbackground,
      format="%a",
      update_interval=1,
      decorations=[RectDecoration(colour=pforeground, radius=[7,0,0,7], filled=True)],
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
    ),
    
    widget.Clock(
      foreground=pforeground,
      format="%d",
      update_interval=1,
      decorations=[RectDecoration(colour=pbackground, radius=0,filled=True)],
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},
    ),
    
    widget.Clock(
      foreground=pbackground,
      format="%H:%M",
      update_interval=1,
      decorations=[RectDecoration(colour=pforeground, radius=[0,7,7,0], filled=True)],
      mouse_callbacks={'Button1': lambda: qtile.function(calendar_notification),'Button4': lambda: qtile.function(calendar_notification_prev),'Button5': lambda: qtile.function(calendar_notification_next)},              
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    
    widget.UPowerWidget(
      border_charge_colour=pforeground,
      border_colour=pbackground,
      border_critical_colour='#cc0000',
      fill_critical='#cc0000',
      fill_low='#FF5511',
      fill_normal=pforeground,
      foreground=pforeground,
      decorations=[RectDecoration(colour=pbackground,radius=7,filled=True)],
      percentage_critical=0.2,
      percentage_low=0.3,
      text_charging=' ({percentage:.0f}%) {ttf} to ',
      text_discharging=' ({percentage:.0f}%) {tte} Left',
    ),
    
    widget.Spacer(
      length=5,
      background=transparent,
    ),
    ## Lock, Logout, Poweroff
    
    widget.TextBox(
      decorations=[RectDecoration(colour=pforeground, radius=7, filled=True)],
      foreground=pbackground,
      text="",
      mouse_callbacks={'Button1': lambda: qtile.function(session_widget)},
      width=24
    )]
    
  return widgets_list

def screen1_widgets():
  widgets_screen1=init_widgets_list()
  return widgets_screen1

def bar_config(position):
    bar_instance = bar.Bar(
        widgets=screen1_widgets(),
        size=bar_size,
        background=transparent,
        margin=[bar_margin[0],
                bar_margin[1],
                bar_margin[2],
                bar_margin[3]]
    )
    return {position: bar_instance}

def init_screens_bottom():
    if single_monitor:
        return [Screen(**bar_config("bottom"))]
    else:
        return [Screen(**bar_config("bottom")) for _ in range(get_screen_count())]

def init_screens_top():
    if single_monitor:
        return [Screen(**bar_config("top"))]
    else:
        return [Screen(**bar_config("top")) for _ in range(get_screen_count())]

if bar_position == "top":
  screens=init_screens_top()
else:
  screens=init_screens_bottom()

widgets_list = init_widgets_list()
widgets_screen1 = screen1_widgets()