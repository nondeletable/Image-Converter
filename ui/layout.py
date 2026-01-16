import flet as ft

from ui.forms import build_form
from ui.window_controls import build_title_bar


def build_layout(page: ft.Page):
    page.window.center()
    page.title = "Image Converter"
    page.window.width = 445
    page.window.height = 750
    page.window.resizable = False
    page.window.title_bar_hidden = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary="#805a96"))
    page.assets_dir = "assets"
    page.fonts = {
        "Rubik": "fonts/rubik/Rubik-Medium.ttf",
        "Rubik2": "fonts/rubik/Rubik-Regular.ttf",
    }

    MARGIN_TOP = 80
    MARGIN_IMG_TXT = 50
    MARGIN_MIDDLE = 15
    MARGIN_BOTTOM = 7

    # header
    image = ft.Image(src="images/image.png", width=150, height=150)
    title = ft.Text("IMAGE CONVERTER", font_family="Rubik", size=26, weight=ft.FontWeight.BOLD)

    margin_top = ft.Container(height=MARGIN_TOP, width=400)
    margin_img_txt = ft.Container(height=MARGIN_IMG_TXT, width=400)
    margin_middle = ft.Container(height=MARGIN_MIDDLE, width=400)
    margin_bottom = ft.Container(height=MARGIN_BOTTOM, width=400)

    header_column = ft.Column(
        [image, margin_img_txt, title],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # form
    form = build_form(page)

    # footer
    footer = ft.Text(
        "DEVELOPED BY NONDELETABLE",
        color=ft.Colors.GREY_500,
        text_align=ft.TextAlign.CENTER,
    )

    container = ft.Column(
        controls=[
            build_title_bar(page),
            margin_top,
            header_column,
            margin_middle,
            form,
            margin_bottom,
            footer,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    page.add(container)
