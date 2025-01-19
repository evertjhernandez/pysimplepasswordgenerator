import random
import reflex as rx
from reflex.components.radix.themes.components.icon_button import icon_button

from rxconfig import config

class State(rx.State):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
    random_password: str = ""
    slider_value: int = 25

    def generate_password(self):
        self.random_password = ''.join(random.choice(self.characters) for _ in range(self.slider_value))

    @rx.event
    def set_slider_value(self, value: list[int]):
        self.slider_value = value[0]

def index():
    return rx.flex(
        rx.vstack(
            rx.heading("Random Password Generator", font_size="2em"),
            rx.text(
                State.random_password,
                color="gray",
            ),
            rx.heading(State.slider_value, font_size="1.5em"),
            rx.slider(
                default_value=25,
                min_=0,
                max=50,
                on_change=State.set_slider_value.throttle(100),
                style={"cursor": "pointer"},
            ),
            rx.button(
                "Generate Password",
                color_scheme="grass",
                on_click=State.generate_password,
                style={"cursor": "pointer"},
            ),
            spacing="4",
        ),
        justify="center",
        align="center",
        height="100vh"
    )

app = rx.App()
app.add_page(index)