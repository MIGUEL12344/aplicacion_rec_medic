import reflex as rx
from .screen.splash_screen import splashScreen
from .screen.home_screen import homeScreen
from .screen.search_screen import searchScreen
from .screen.about_user_screen import aboutUserScreen
from .screen.about_2 import aboutUser2Screen
from .screen.notify_screen import notifyScreen
from rxconfig import config


def index() -> rx.Component:
    return rx.mobile_and_tablet(
        splashScreen()
    ) 

app = rx.App()
app.add_page(index)
