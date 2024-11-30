import reflex as rx

def splashScreen()-> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.image(src="/capsula.png", width="100px", padding="10px", margin_bottom="35px"),
                rx.text("R_notifica", size="6"),
                display="flex",
                align_items="center",
                margin_top="38vh",
                height="100vh"
            ),
        ),
    )