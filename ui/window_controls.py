import flet as ft

from ui.dialogs import open_nfo_window


def minimize_window(e, page: ft.Page):
    page.window.minimized = True
    page.update()


def close_window(e, page: ft.Page):
    page.window.close()


def build_title_bar(page: ft.Page):
    close_button = ft.IconButton(ft.Icons.CLOSE, on_click=lambda e: close_window(e, page))
    maximize_button = ft.IconButton(ft.Icons.MENU, on_click=lambda e: open_nfo_window(e, page))
    minimize_button = ft.IconButton(ft.Icons.REMOVE, on_click=lambda e: minimize_window(e, page))
    drag_area = ft.WindowDragArea(
        ft.Container(height=50, width=1000), expand=True, maximizable=False
    )

    return ft.Row(
        controls=[maximize_button, drag_area, minimize_button, close_button],
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.START,
    )
