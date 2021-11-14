# author HackMEAny
# email hackme.any@protonmail.com
# desc Widgets for qtile bar

from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)


def base(fg="text", bg="dark"):
    return {"foreground": colors[fg], "background": colors[bg]}


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg), text="", fontsize=42, padding=-3  # Icon: nf-oct-triangle_left
    )


def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg="light"),
            font="UbuntuMono Nerd Font",
            fontsize=20,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors["active"],
            inactive=colors["inactive"],
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            urgent_border=colors["urgent"],
            this_current_screen_border=colors["focus"],
            this_screen_border=colors["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
            disable_drag=True,
        ),
        separator(),
        widget.WindowName(**base(fg="focus"), fontsize=19, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    separator(),
    powerline("color4", "dark"),
    # Update Widget   Icon: nf-fa-download
    # You need to update your mirrorlist for this to work or add custom commands for updating mirror lists
    widget.WidgetBox(
        **base(bg="color4"),
        widgets=[
            widget.CheckUpdates(
                # distro="Arch",
                background=colors["color4"],
                colour_have_updates=colors["text"],
                colour_no_updates=colors["text"],
                no_update_string="0",
                display_format="{updates}",
                # update_interval=1800,
                # custom_command='checkupdates',
            )
        ],
        text_closed=" ",
        text_open="  ",
        fontsize=16,
    ),
    powerline("color3", "color4"),
    #  Internet Widget
    widget.WidgetBox(
        **base(bg="color3"),
        widgets=[
            widget.Net(
                **base(bg="color3"),
                # interface="enp2s0"    # Change to your network interface or leave blank for all interfaces you can list in by using `ip a`
            )
        ],
        text_closed=" ",
        text_open=" ",
        fontsize=19,
    ),
    powerline("color7", "color3"),
    # CPU usage widget
    widget.WidgetBox(
        **base(bg="color7"),
        widgets=[
            widget.CPU(
                **base(bg="color7"), format="CPU {freq_current}GHz {load_percent}% "
            )
        ],
        text_closed=" ",
        text_open=" ",
        fontsize=27,
    ),
    powerline("color5", "color7"),
    # Memory Widget
    widget.WidgetBox(
        **base(bg="color5"),
        widgets=[
            widget.Memory(
                **base(bg="color5"),
                measure_mem="G",
                format="{MemUsed:.1f}{mm} / {MemTotal:.0f}{mm} ",
            )
        ],
        text_closed="  ",
        text_open="  ",
        fontsize=20,
    ),
    powerline("color2", "color5"),
    widget.CurrentLayoutIcon(**base(bg="color2"), scale=0.65),
    powerline("color1", "color2"),
    #  /   Time & Date widgets
    widget.WidgetBox(
        **base(bg="color1"),
        widgets=[widget.Clock(**base(bg="color1"), format="%A %d/%m/%Y - %I:%M %p ")],
        text_closed=" ",
        text_open="  ",
        fontsize=25,
    ),
    powerline("color4", "color1"),
    # Backlight Widget
    widget.WidgetBox(
        **base(bg="color4"),
        widgets=[
            widget.Backlight(
                **base(bg="color4"),
                backlight_name="amdgpu_bl1",  # Change to your backlight name from `/sys/class/backlight/backlight_name`
            )
        ],
        text_closed=" ",
        text_open=" ",
        fontsize=20,
    ),
    # Comment this line if you want to uncomment the below widgets
    powerline("dark", "color4"),
    # Uncomment if you want to use the Volume widget
    # powerline('color9', 'color4'),
    # widget.WidgetBox(**base(bg='color9'), widgets=[widget.Volume(
    #     **base(bg='color9'), padding=5)], text_closed='墳 ', text_open='墳 ', fontsize=20),
    # powerline('color8', 'color9'),
    # Uncomment if you want to use the Bluetooth widget
    # widget.WidgetBox(**base(bg='color8'), widgets=[widget.Bluetooth(
    #     **base(bg='color8'))], text_closed=' ', text_open=' ', fontsize=20),
    # powerline('dark', 'color8'),
    # Battery Widget
    widget.Battery(
        **base(fg="light"),
        charge_char="",
        discharge_char="",
        full_char="",
        empty_char="",
        show_short_text=False,
        format="{char} {percent:2.0%}",
        notify_below=10,
    ),
    # System Tray Widget
    widget.Systray(background=colors["dark"], padding=5),
]


# For Secondary Display
# secondary_widgets = [
#     *workspaces(),
#     separator(),
#     powerline('color1', 'dark'),
#     widget.Memory(**base(bg='color5'), measure_mem='G'),
#     widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
#     widget.CurrentLayout(**base(bg='color1'), padding=5),
#     powerline('color2', 'color1'),
#     widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
#     widget.Volume(**base(bg='color3')),
#     powerline('dark', 'color2'),
# ]

widget_defaults = {
    "font": "UbuntuMono Nerd Font Bold",
    "fontsize": 14,
    "padding": 1,
}
extension_defaults = widget_defaults.copy()
