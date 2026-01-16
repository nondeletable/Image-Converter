import webbrowser

import flet as ft


def close_dialog(dialog, page: ft.Page):
    dialog.open = False
    page.update()


def open_nfo_window(e, page: ft.Page):
    def open_link(url):
        webbrowser.open(url)

    dialog = ft.AlertDialog(
        title=ft.Text("ABOUT", text_align=ft.TextAlign.CENTER, font_family="Rubik"),
        shape=ft.RoundedRectangleBorder(radius=8),
        content=ft.Container(
            height=300,
            width=270,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Hi! My name is Alexandra.\n"
                        "I'm a Python developer.\n"
                        "Thank you for using my app!",
                        size=20,
                        text_align=ft.TextAlign.CENTER,
                        font_family="Rubik2",
                        width=300,
                    ),
                    ft.Text(
                        "If you’d like to say thanks, leave feedback, report a bug, or discuss"
                        "collaboration, feel free to contact me via Discord, email, or GitHub.",
                        size=15,
                        text_align=ft.TextAlign.CENTER,
                        font_family="Rubik2",
                    ),
                    ft.Container(height=10),  # Небольшой отступ
                    # Ряд с круглыми кнопками
                    ft.Row(
                        controls=[
                            # Discord
                            ft.ElevatedButton(
                                content=ft.Image(src="images/discord.svg", width=80, height=80),
                                width=60,
                                height=60,
                                style=ft.ButtonStyle(
                                    padding=0, shape=ft.RoundedRectangleBorder(radius=40)
                                ),
                                on_click=lambda e: open_link("https://discord.gg/sxW29bUd"),
                            ),
                            # Email
                            ft.ElevatedButton(
                                content=ft.Image(src="images/email.svg", width=80, height=80),
                                width=60,
                                height=60,
                                style=ft.ButtonStyle(
                                    padding=0, shape=ft.RoundedRectangleBorder(radius=40)
                                ),
                                on_click=lambda e: open_link("mailto:nondeletable@gmail.com"),
                            ),
                            # GitHub
                            ft.ElevatedButton(
                                content=ft.Image(src="images/github.svg", width=80, height=80),
                                width=60,
                                height=60,
                                style=ft.ButtonStyle(
                                    padding=0, shape=ft.RoundedRectangleBorder(radius=40)
                                ),
                                on_click=lambda e: open_link(
                                    "https://github.com/nondeletable/Image-Converter"
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                    ),
                ],
                spacing=15,
            ),
        ),
        actions=[ft.TextButton("OK", on_click=lambda e: close_dialog(dialog, page))],
    )
    page.overlay.append(dialog)
    dialog.open = True
    page.update()


def open_qu_window(e, page: ft.Page):
    dialog = ft.AlertDialog(
        title=ft.Text("What's that?", text_align=ft.TextAlign.CENTER),
        shape=ft.RoundedRectangleBorder(radius=8),
        content=ft.Container(
            width=150,
            height=130,
            content=ft.Column(
                [
                    ft.Text(
                        "This is where you need to enter the mask-name "
                        "of your images, and then a sequential number "
                        "will be added that starts with 001",
                        size=18,
                    )
                ]
            ),
        ),
    )
    page.overlay.append(dialog)
    dialog.open = True
    page.update()
