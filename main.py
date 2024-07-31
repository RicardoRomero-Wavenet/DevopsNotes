import flet
import js2py
from flet import ElevatedButton, Page, Text, TextField, Row, Column,colors,IconButton, NavigationRail,FloatingActionButton, NavigationRailDestination, NavigationRailLabelType, Icon, VerticalDivider, MainAxisAlignment, PopupMenuButton, icons, AppBar
"""
Hacer una aplicacion que use NavigationRail, y que tenga las opciones Nuevo, Guardar, About y Salir
"""
def main(page: Page):
    global code, compiled_code
    code = ""
    compiled_code = ""
    textbox_compiled = Text("Compiled code: ", size=20)
    textfield_code = TextField( border="none", max_lines=5000,multiline=True, min_lines=1,autofocus=True,expand=True)
    
    def compile_code(e):
        code = textfield_code.value
        compiled_code = js2py.eval_js(code)
        textbox_compiled.value = "Compiled code: \n" + str(compiled_code)
        page.update()
     
    rail = NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Second",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )
    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Column([ ElevatedButton("Compile", on_click=compile_code),textfield_code], alignment=MainAxisAlignment.START, expand=True),
                VerticalDivider(width=1),
                Column([ textbox_compiled,], alignment=MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )

flet.app(target=main)
