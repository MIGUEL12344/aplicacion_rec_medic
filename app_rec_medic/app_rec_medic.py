import reflex as rx
from .screen.splash_screen import splashScreen

from rxconfig import config


def index() -> rx.Component:
    return rx.container(
        splashScreen()
    )


app = rx.App()
app.add_page(index)
