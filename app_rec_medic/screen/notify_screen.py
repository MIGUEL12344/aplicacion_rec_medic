import reflex as rx

def notifyScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.hstack(
            rx.color_mode.button(position="top-right"),
            rx.text("notificaciones", margin_top="15px", margin_bottom="10px"),
            style={
                "border_bottom":"2px solid #c56dfc"},
            margin_bottom="100px"),
            rx.vstack(
                rx.button("tines una dosis de paracetamol pendiente para tomar", height="50px", background_color="purple"),
                rx.button("tines una dosis de ibuprofeno pendiente para tomar", height="50px", background_color="purple"),
                rx.button("tines una dosis de clonazepan pendiente para tomar", height="50px", background_color="purple"),
                rx.button("tines una dosis de sertralina pendiente para tomar", height="50px", background_color="purple")
            )))