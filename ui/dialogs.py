import webbrowser

import flet as ft


def close_dialog(dialog, page: ft.Page):
    dialog.open = False
    page.update()


def open_nfo_window(e, page: ft.Page):
    def open_link(url):
        webbrowser.open(url)

    dialog = ft.AlertDialog(
        title=ft.Text("My contacts", text_align=ft.TextAlign.CENTER),
        shape=ft.RoundedRectangleBorder(radius=8),
        content=ft.Container(
            height=320,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Hi! My name is Alexandra. I'm a Python developer. "
                        "It's one of my apps. If you like my work, "
                        "there are contacts below where you can contact me!",
                        size=18,
                    ),
                    ft.Row(
                        [
                            ft.Text("My website:", expand=1, size=18),
                            ft.IconButton(
                                icon=ft.Icons.WEB,
                                # on_click=lambda e: open_link("https://mywebsite.com"),
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text("My mail:", expand=1, size=18),
                            ft.IconButton(
                                icon=ft.Icons.EMAIL,
                                on_click=lambda e: open_link("mailto:nondeletable@gmail.com"),
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text("My github:", expand=1, size=18),
                            ft.IconButton(
                                icon=ft.Icons.HUB,
                                on_click=lambda e: open_link("https://github.com/nondeletable"),
                            ),
                        ]
                    ),
                ],
                spacing=20,
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
