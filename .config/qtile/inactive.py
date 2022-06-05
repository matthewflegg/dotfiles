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
    ("WWW",  {"layout": "max"}),        # Web browsing.
    ("DEV",  {"layout": "monadtall"}),  # Programming.
    ("SYS",  {"layout": "monadtall"}),  # System monitoring, etc.
    ("DOC",  {"layout": "max"}),        # Documentation.
    ("VIRT", {"layout": "monadtall"}),  # VMs.
    ("GAME", {"layout": "max"}),        # Gaming.
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
low_contrast = {
    "primary": {
        "bg": "2d2d2d",
        "fg": "d3d0c8",
    },
    "dark": {
        0: "5f5f5f",
        1: "d96468",
        2: "a2d964",
        3: "d9c964",
        4: "64a2d9",
        5: "9a64d9",
        6: "64d9d5",
        7: "989898",
    },
    "light": {
        0: "828282",
        1: "d98f93",
        2: "b8d98f",
        3: "d9cf8f",
        4: "8f99d9",
        5: "b08fd9",
        6: "8fd9d5",
        7: "c5c5c5",
    },
}

numix_darkest = {
    "primary": {
        "bg": "282828",
        "fg": "a2a2a2",
    },
    "dark": {
        0: "555555",
        1: "9c3528",
        2: "61bc3b",
        3: "f3b43a",
        4: "0d68a8",
        5: "744560",
        6: "288e9c",
        7: "a2a2a2",
    },
    "light": {
        0: "888888",
        1: "d64937",
        2: "86df5d",
        3: "fdd75a",
        4: "0f75bd",
        5: "9e5e83",
        6: "37c3d6",
        7: "f9f9f9",
    },
}

tartan = {
    "primary": {
        "bg": "2b2b2b",
        "fg": "dedede",
    },
    "dark": {
        0: "2e3436",
        1: "cc0000",
        2: "4e9a06",
        3: "c4a000",
        4: "3465a4",
        5: "75507b",
        6: "06989a",
        7: "d3d7cf",
    },
    "light": {
        0: "555753",
        1: "ef2929",
        2: "8ae234",
        3: "fce94f",
        4: "729fcf",
        5: "ad7fa8",
        6: "34e2e2",
        7: "eeeeec",
    },
}

colorful_colors = {
    "primary": {
        "bg": "000000",
        "fg": "ffffff",
    },
    "dark": {
        0: "151515",
        1: "ff8eaf",
        2: "a6e25f",
        3: "f8e578",
        4: "a6e2f0",
        5: "e85b92",
        6: "5f868f",
        7: "d5f1f2",
    },
    "light": {
        0: "696969",
        1: "ed4c7a",
        2: "a6e179",
        3: "ffdf6b",
        4: "79d2ff",
        5: "bb5d79",
        6: "87a8af",
        7: "e2f1f6",
    },
}

rezza = {
    "primary": {
        "bg": "222222",
        "fg": "dddddd",
    },
    "light": {
        0: "191919",
        1: "803232",
        2: "5b762f",
        3: "aa9943",
        4: "324c80",
        5: "706c9a",
        6: "92b19e",
        7: "ffffff",
    },
    "dark": {
        0: "252525",
        1: "982b2b",
        2: "89b83f",
        3: "efef60",
        4: "2b4f98",
        5: "826ab1",
        6: "a1cdcd",
        7: "dddddd",
    },
}

theme = rezza

# Change this to true if you'd like gaps between
# your windows.
use_gaps = True

# Define some common aesthetics and functionality that
# most layouts will have in common.
layout_defaults = {
    "border_width":  1,
    "border_focus":  theme["dark"][1],
    "border_normal": theme["dark"][0],
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
    "foreground": theme["primary"]["fg"],
}
colored_widget_defaults = {
    "font":       "Ubuntu Mono Bold",
    "fontsize":   12,
    "padding":    6,
    "foreground": theme["primary"]["bg"]
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
                separator(theme["primary"]["bg"]),
                icon("\u2318", theme["primary"]["fg"], theme["primary"]["bg"]),
                widget.TextBox(
                    text=" Workspaces:",
                    **widget_defaults,
                ),
                right_arrow(theme["primary"]["bg"], theme["dark"][0]),
                right_arrow(theme["dark"][0], theme["light"][1]),
                separator(theme["light"][1]),
                widget.GroupBox(
                    font="Ubuntu Mono",
                    highlight_method="line",
                    highlight_color=theme["light"][1],
                    padding_y=2,
                    margin_x=8,
                    padding_x=3,
                    borderwidth=1,
                    active=theme["light"][7],
                    inactive=theme["primary"]["bg"],
                    this_current_screen_border=theme["primary"]["fg"],
                    background=theme["light"][1],
                    fontsize=widget_defaults["fontsize"],
                    paddin=widget_defaults["padding"],
                ),
                right_arrow(theme["light"][1], theme["dark"][1]),
                separator(theme["dark"][1]),
                icon("\u2387", theme["primary"]["bg"], theme["dark"][1]),
                widget.CurrentLayout(
                    background=theme["dark"][1],
                    **colored_widget_defaults,
                ),
                separator(theme["dark"][1]),
                widget.Prompt(
                    background=theme["dark"][1],
                    cursor_color=theme["primary"]["fg"],
                    **widget_defaults,
                ),
                right_arrow(theme["dark"][1], theme["light"][1]),
                right_arrow(theme["light"][1], theme["dark"][0]),
                right_arrow(theme["dark"][0], theme["primary"]["bg"]),
                separator(theme["primary"]["bg"]),
                widget.WindowName(
                    **widget_defaults,
                ),
                separator(theme["primary"]["bg"]),

                # Right hand side of the bar.
                # Use arrows for a powerline-style effect.
                separator(theme["primary"]["bg"]),
                left_arrow(theme["dark"][0], theme["primary"]["bg"], padding=-5),
                left_arrow(theme["light"][1], theme["dark"][0], padding=-5),
                left_arrow(theme["dark"][1], theme["light"][1]),
                icon("\u26c1", theme["primary"]["bg"], theme["dark"][1]),
                widget.Net(
                    interface="wlan0",
                    format="{down} ↓↑ {up}",
                    background=theme["dark"][1],
                    **colored_widget_defaults,
                ),
                separator(theme["dark"][1]),
                left_arrow(theme["light"][2], theme["dark"][1]),
                left_arrow(theme["dark"][2], theme["light"][2]),
                widget.CPU(
                    format="CPU: {load_percent}%",
                    background=theme["dark"][2],
                    **colored_widget_defaults,
                ),
                separator(theme["dark"][2]),
                left_arrow(theme["light"][3], theme["dark"][2]),
                left_arrow(theme["dark"][3], theme["light"][3]),
                widget.Memory(
                    measure_mem="G",
                    format="Mem: {MemUsed:.1f}/{MemTotal:.1f}GB",
                    background=theme["dark"][3],
                    **colored_widget_defaults,
                ),
                separator(theme["dark"][3]),
                left_arrow(theme["light"][4], theme["dark"][3]),
                left_arrow(theme["dark"][4], theme["light"][4]),
                widget.NvidiaSensors(
                    format="GPU: {perf} {temp}°C",
                    background=theme["dark"][4],
                    **colored_widget_defaults,
                ),
                separator(theme["dark"][4]),
                left_arrow(theme["light"][5], theme["dark"][4]),
                left_arrow(theme["dark"][5], theme["light"][5]),
                icon("\u231b", theme["primary"]["bg"], theme["dark"][5]),
                widget.Clock(
                    format="%A, %B %d - %H:%M",
                    background=theme["dark"][5],
                    **colored_widget_defaults,
                ),
                separator(theme["dark"][5]),
            ],
            24,
            background=theme["primary"]["bg"],
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
