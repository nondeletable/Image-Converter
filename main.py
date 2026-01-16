import logging
import logging.handlers
import os

import flet as ft

from ui.layout import build_layout

os.makedirs("logs", exist_ok=True)

# настроить логгер
log_file = "logs/app.log"
handler = logging.handlers.RotatingFileHandler(
    log_file, maxBytes=1_000_000, backupCount=3, encoding="utf-8"
)

logging.basicConfig(
    level=logging.INFO,
    handlers=[handler],
    format="%(asctime)s [%(levelname)s] %(message)s",
)

log = logging.getLogger("app")


def main(page: ft.Page):
    build_layout(page)


if __name__ == "__main__":
    import multiprocessing as mp

    mp.freeze_support()
    mp.set_start_method("spawn")
    ft.app(target=main)
