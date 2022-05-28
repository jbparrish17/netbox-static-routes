from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


staticroute_buttons = [
    PluginMenuButton(
        link='plugins:netbox_static_routes:staticroute_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_static_routes:staticroute_list',
        link_text='Static Routes',
        buttons=staticroute_buttons
    ),
)
