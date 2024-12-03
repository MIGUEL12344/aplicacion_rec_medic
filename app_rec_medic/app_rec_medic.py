import reflex as rx
from .screen.splash_screen import splashScreen
from rxconfig import config


def index() -> rx.Component:
    return rx.mobile_and_tablet(
        splashScreen()
    ) 

app = rx.App()
app.add_page(index)
