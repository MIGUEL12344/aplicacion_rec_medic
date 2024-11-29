import reflex as rx

def splashScreen()-> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.button("hola"),
            rx.text("R_notifica"),
                display="flex",
                align_items="center",
                margin_top="38vh",
                height="100vh"
        ),
    )