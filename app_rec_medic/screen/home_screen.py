import reflex as rx

def homeScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.text("notificaciones", margin_top="15px"),
            rx.vstack(
                rx.text("VIENVENIDO A SALUD NOTIFICA", size="6", font_size="poppins"),
                rx.text("aqui podras ver los medicamentos que quieras que te recordemos", size="4", text_align="center"),
                rx.button("BUSCAR MEDICAMENTO", font_size="poppins", background_color="gray", margin_top="15px",
                          _hover={"background_color": "lightgreen"}),
                display="flex",
                align_items="center",
                margin_top="32vh",
                height="100vh"
            ),
        ),
    )