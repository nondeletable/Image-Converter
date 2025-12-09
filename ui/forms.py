import logging
import os
from tkinter import Tk, filedialog

import flet as ft

from config_loader import config
from ui.dialogs import open_qu_window
from utils.files import ALLOWED_EXTENSIONS, rename_and_convert, sanitize_mask

ACCENT = "#8945ab"
log = logging.getLogger("app")


def build_form(page: ft.Page):
    txt_directory = ft.TextField(
        hint_text="Directory path",
        hint_style=ft.TextStyle(color=ACCENT),
        border_color=ACCENT,
        focused_border_color=ACCENT,
        width=330,
    )

    def open_directory_picker(e):
        root = Tk()
        root.withdraw()
        directory = filedialog.askdirectory()
        root.destroy()
        if directory:
            txt_directory.value = directory
            page.update()

    pick_directory_btn = ft.ElevatedButton(
        content=ft.Icon(ft.Icons.FOLDER_OPEN, color=ft.Colors.WHITE, size=28),
        bgcolor=ACCENT,
        width=60,
        height=50,
        on_click=open_directory_picker,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    directory_row = ft.Row(
        [txt_directory, pick_directory_btn],
        spacing=10,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    dropdown_format = ft.Dropdown(
        label="Select a format",
        options=[
            ft.dropdown.Option("JPG"),
            ft.dropdown.Option("PNG"),
            ft.dropdown.Option("JPEG"),
        ],
        value="JPG",
        width=400,
        border_color=ACCENT,
        color=ACCENT,
    )

    txt_mask = ft.TextField(
        hint_text="File name mask",
        hint_style=ft.TextStyle(color=ACCENT),
        border_color=ACCENT,
        focused_border_color=ACCENT,
        width=400,
        height=50,
        suffix=ft.IconButton(
            icon=ft.Icons.QUESTION_MARK_ROUNDED,
            on_click=lambda e: open_qu_window(e, page),
        ),
    )

    def on_convert(e):
        directory = txt_directory.value.strip()
        target_format = dropdown_format.value
        mask = sanitize_mask(txt_mask.value)
        txt_mask.value = mask
        log.info(
            "User triggered convert: dir=%s, format=%s, mask=%s", directory, target_format, mask
        )
        page.update()

        def notify(message: str, color):
            sb = ft.SnackBar(ft.Text(message), open=True, duration=4000, bgcolor=color)
            page.overlay.append(sb)
            sb.open = True
            page.update()

        # валидация
        if not os.path.isdir(directory):
            notify("The specified directory does not exist!", ft.Colors.BLACK)
            return

        try:
            stats, report = rename_and_convert(
                directory,
                target_format,
                mask,
                create_report=False,
                config=config,
            )

            converted = stats.get("converted", 0)
            renamed = stats.get("renamed", 0)
            skipped = stats.get("skipped", 0)

            processed = converted + renamed

            if processed == 0 and skipped == 0:
                notify("No supported images found in the selected folder.", ft.Colors.BLACK)
                log.info("No supported images found in %s", directory)
            elif processed == 0 and skipped > 0:
                supported = ", ".join(sorted(ext.upper() for ext in ALLOWED_EXTENSIONS))
                notify(
                    f"All files were skipped ({skipped}). Supported: {supported}.", ft.Colors.BLACK
                )
                log.warning("All files skipped in %s (count=%d)", directory, skipped)
            else:
                notify(
                    f"Converted: {converted}, Renamed: {renamed}, Skipped: {skipped}.",
                    ft.Colors.BLACK,
                )
                log.info("Done. Converted=%d, Renamed=%d, Skipped=%d", converted, renamed, skipped)

        except Exception as ex:
            notify(f"Error: {ex}", ft.Colors.BLACK)
            log.error("Error during convert: %s", ex)

    btn_convert = ft.ElevatedButton(
        "CONVERT",
        on_click=on_convert,
        bgcolor=ACCENT,
        color=ft.Colors.WHITE,
        width=120,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )

    return ft.Column(
        [directory_row, dropdown_format, txt_mask, btn_convert],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
