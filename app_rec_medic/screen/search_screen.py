import reflex as rx
@rx.page(route="/search")
def searchScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.link(rx.icon("arrow-left",margin_top="19px"),href="/home"),
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.input(placeholder="Buscar medicamento...", width="70%", border_width="2px", margin_top="-40px"),
                rx.link(rx.button("paracetamol----250ml----generico", height="50px", background_color="gray", margin_top="50px"),href="/about"),
                rx.text("aqui apareceran los medicamentos que busques", text_align="center", color="gray", margin_top="250px", margin_left="-50px", size="4"),
                margin_top="15px",
                margin_left="50px"
            ),
            )
        )