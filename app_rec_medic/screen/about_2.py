import reflex as rx
@rx.page(route="/about2")
def aboutUser2Screen()-> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.link(rx.icon("arrow-left",margin_top="17px"),href="/about"),
            rx.color_mode.button(position="top-right"),
            rx.vstack(
                rx.image(src="/minions2.png", padding="25px", width="250px", margin_top="80px", margin_left="65px"),
                rx.text("Cuando quieres que te recuerde?", margin_bottom="50px"),
                rx.hstack(
                    rx.button("HORA:", background_color="transparent", margin_left="20px", color="purple"),
                    rx.spacer(),
                    rx.button("8:00 am", background_color="gray", margin_left="150px"),
                    margin_bottom="50px"),
                rx.hstack(
                    rx.button("DOSIS:", background_color="transparent", margin_left="20px", color="purple"),
                    rx.spacer(),
                    rx.button("1 dosis", background_color="gray", margin_left="154px",margin_bottom="90px")),
                rx.link(rx.button("GUARDAR", margin_left="137px", background_color="green"),href="/home")
                )))