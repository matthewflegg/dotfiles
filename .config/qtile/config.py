# -*- coding: utf-8 -*-

# IMPORTS
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
)
from libqtile import (
    bar,
    layout,
    widget,
    qtile,
)

mod = "mod4"            # Set the windows key as the mod key.
terminal = "alacritty"  # Set Alacritty as the default terminal.

# KEYBINDINGS
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Bindings for the volume keys.
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    # Bindings for screenshotting.
    # Use Win + Shift + S to save a screenshot to .screenshots.
    Key([mod, "shift"], "s",
        lazy.spawn("maim -s -u | xclip -selection clipboard -t image/png -i"),
        desc="Screenshot a selected area of the screen and save it to the clipboard."
    ),
]


# GROUPS
#
# Initialise an empty list to keep groups in.
# Set the names of the groups, along with their default layout.
groups = []
group_names = [
    ("www",  {"layout": "max"}),        # Web browsing.
    ("dev",  {"layout": "monadtall"}),  # Programming.
    ("sys",  {"layout": "monadtall"}),  # System monitoring, etc.
    ("doc",  {"layout": "max"}),        # Documentation.
    ("virt", {"layout": "monadtall"}),  # VMs.
    ("chat", {"layout": "monadtall"}),  # Email, messenger, etc.
    ("mus",  {"layout": "max"}),        # Music.
    ("vid",  {"layout": "max"}),        # Videos.
    ("game", {"layout": "max"}),        # Gaming.
]

# Create the groups and set keybindings for switching between them,
# as well as moving windows between them.
for num_key, (name, params) in enumerate(group_names, 1):
    groups.append(Group(name, **params))

    # Number each group and bind its number to a key.
    # For instance, if "SYS" is group 3, Mod + 3 switches to it.
    keys.append(Key([mod], str(num_key), lazy.group[name].toscreen()))         # Switch to another group.
    keys.append(Key([mod, "shift"], str(num_key), lazy.window.togroup(name)))  # Send window to another group.


# LAYOUTS
# 
# Set some themes that all work the same.
# Change `theme` to one of the ones below to change the colors.  
hybrid = {
    "bar_color":  "1d1f21",
    "text_color": "c5c8c6",
    "color_0":    "282a2e",
    "color_1":    "a54242",
    "color_2":    "8c9440",
    "color_3":    "de935f",
    "color_4":    "5f819d",
    "color_5":    "85678f",
    "color_6":    "5e8d87",
    "color_7":    "707880",
}
ashes = {
    "bar_color":  "1c2023",
    "text_color": "c7ccd1",
    "color_0":    "1c2023",
    "color_1":    "c7ae95",
    "color_2":    "95c7ae",
    "color_3":    "aec795",
    "color_4":    "ae95c7",
    "color_5":    "c795ae",
    "color_6":    "95aec7",
    "color_7":    "c7ccd1",
}
kasugano = {
    "bar_color":  "1b1b1b",
    "text_color": "ffffff",
    "color_0":    "3d3d3d",
    "color_1":    "6673bf",
    "color_2":    "3ea290",
    "color_3":    "b0ead9",
    "color_4":    "31658c",
    "color_5":    "596196",
    "color_6":    "8292b2",
    "color_7":    "c8cacc",
}
vacuous2 = {
    "bar_color":  "101010",
    "text_color": "d2c5bc",
    "color_0":    "202020",
    "color_1":    "b91e2e",
    "color_2":    "81957c",
    "color_3":    "f9bb80",
    "color_4":    "356579",
    "color_5":    "2d2031",
    "color_6":    "0b3452",
    "color_7":    "909090",
}
astromouse = {
    "bar_color":  "000000",
    "text_color": "ffffff",
    "color_0":    "1c1c1c",
    "color_1":    "d770af",
    "color_2":    "9acc79",
    "color_3":    "d0d26b",
    "color_4":    "77b6c5",
    "color_5":    "a488d9",
    "color_6":    "7fcab3",
    "color_7":    "8d8d8d",
}
ivory_dark = {
    "bar_color":  "2d2c28",
    "text_color": "a4a6ab",
    "color_0":    "5b5955",
    "color_1":    "c4756e",
    "color_2":    "559a6a",
    "color_3":    "9b8a4b",
    "color_4":    "6a8dca",
    "color_5":    "b577ac",
    "color_6":    "019baa",
    "color_7":    "dbdde2",
}

theme = hybrid

# Change this to true if you'd like gaps between
# your windows.
use_gaps = True

# Define some common aesthetics and functionality that
# most layouts will have in common.
layout_defaults = {
    "border_width":  1,
    "border_focus":  theme["color_1"],
    "border_normal": theme["color_0"],
    "margin":        12 if use_gaps else 0, 
}

layouts = [
    layout.Stack(**layout_defaults),
    layout.Max(),
    layout.MonadTall(**layout_defaults),
]

# WIDGETS
#
# Set some default settings for widgets.
# These can be unpacked as they are passed into constructors.
widget_defaults = {
    "font":       "Ubuntu Mono Bold",
    "fontsize":   12,
    "padding":    6,
    "foreground": theme["text_color"],
}

# This is redundant as of now.
extension_defaults = widget_defaults.copy()


# Define some useful functions for creating widgets
# that are repeated.
def separator(background: str):
    """
    Create a separator widget to put between other widgets.

    background (str): Hexadecimal code for the background color.
    """
    return widget.Sep(
        linewidth=0,
        padding=10,
        background=background,
    )


def left_arrow(foreground: str, background: str, padding: int=-4):
    """
    Create a left-facing powerline-style arrow (◀).
    
    foreground (str): Hexadecimal code for the foreground color.
    background (str): Hexadecimal code for the background color.
    """
    return widget.TextBox(
        font="Ubuntu Mono",
        text="\u25c0",
        foreground=foreground,
        background=background,
        padding=padding,
        fontsize=37,
    )


def right_arrow(foreground: str, background: str, padding: int=-4):
    """
    Create a right-facing powerline-style arrow (◀).
    
    foreground (str): Hexadecimal code for the foreground color.
    background (str): Hexadecimal code for the background color.
    """
    return widget.TextBox(
        font="Ubuntu Mono",
        text="\u25b6",
        foreground=foreground,
        background=background,
        padding=padding,
        fontsize=37,
    )


def icon(icon: str, foreground: str, background: str):
    """
    Create an icon to be displayed in the bar.

    icon       (str): The icon to show.
    foreground (str): Hexadecimal code for the foreground color.
    background (str): Hexadecimal code for the background color.
    """
    return widget.TextBox(
        font="Ubuntu Mono",
        text=icon,
        foreground=foreground,
        background=background,
        padding=3,
        fontsize=16,
    )


# Configure the bar/panel with widgets and decorations.
# Change the colors, etc, in the above sections.
screens = [
    Screen(
        top=bar.Bar(
            [
                # Right hand side of the bar.
                separator(theme["bar_color"]),
                icon("\u2318", theme["text_color"], theme["bar_color"]),
                widget.TextBox(
                    text=" Workspaces:",
                    **widget_defaults,
                ),
                right_arrow(theme["bar_color"], theme["color_0"]),
                separator(theme["color_0"]),
                widget.GroupBox(
                    font="Ubuntu Mono",
                    highlight_method="line",
                    highlight_color=theme["color_0"],
                    padding_y=2,
                    margin_x=8,
                    padding_x=3,
                    borderwidth=1,
                    active=theme["text_color"],
                    inactive=theme["color_1"],
                    this_current_screen_border=theme["text_color"],
                    background=theme["color_0"],
                    fontsize=widget_defaults["fontsize"],
                    paddin=widget_defaults["padding"],
                ),
                right_arrow(theme["color_0"], theme["color_1"]),
                separator(theme["color_1"]),
                icon("\u2387", theme["text_color"], theme["color_1"]),
                widget.CurrentLayout(
                    background=theme["color_1"],
                    **widget_defaults,
                ),
                separator(theme["color_1"]),
                widget.Prompt(
                    background=theme["color_1"],
                    cursor_color=theme["text_color"],
                    **widget_defaults,
                ),
                right_arrow(theme["color_1"], theme["color_0"]),
                right_arrow(theme["color_0"], theme["bar_color"]),
                separator(theme["bar_color"]),
                widget.WindowName(
                    **widget_defaults,
                ),
                separator(theme["bar_color"]),

                # Right hand side of the bar.
                # Use arrows for a powerline-style effect.
                separator(theme["bar_color"]),
                left_arrow(theme["color_0"], theme["bar_color"], padding=-5),
                left_arrow(theme["color_1"], theme["color_0"]),
                icon("\u26c1", theme["text_color"], theme["color_1"]),
                widget.Net(
                    interface="wlan0",
                    format="{down} ↓↑ {up}",
                    background=theme["color_1"],
                    **widget_defaults,
                ),
                separator(theme["color_1"]),
                left_arrow(theme["color_4"], theme["color_1"]),
                widget.CPU(
                    format="CPU: {load_percent}%",
                    background=theme["color_4"],
                    **widget_defaults,
                ),
                separator(theme["color_4"]),
                left_arrow(theme["color_1"], theme["color_4"]),
                widget.Memory(
                    measure_mem="G",
                    format="Mem: {MemUsed:.1f}/{MemTotal:.1f}GB",
                    background=theme["color_1"],
                    **widget_defaults,
                ),
                separator(theme["color_1"]),
                left_arrow(theme["color_4"], theme["color_1"]),
                widget.NvidiaSensors(
                    format="GPU: {perf} {temp}°C",
                    background=theme["color_4"],
                    **widget_defaults,
                ),
                separator(theme["color_4"]),
                left_arrow(theme["color_1"], theme["color_4"]),
                icon("\u231b", theme["text_color"], theme["color_1"]),
                widget.Clock(
                    format="%A, %B %d - %H:%M",
                    background=theme["color_1"],
                    **widget_defaults,
                ),
                separator(theme["color_1"]),
            ],
            24,
            background=theme["bar_color"],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
