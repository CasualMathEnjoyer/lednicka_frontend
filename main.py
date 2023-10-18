# kivymd-1.1.1
# Installing collected packages: kivy-deps.sdl2, kivy-deps.glew, kivy-deps.angle, pypiwin32, docutils, Kivy-Garden, kivy
# Successfully installed Kivy-Garden-0.1.5 docutils-0.20.1 kivy-2.2.1 kivy-deps.angle-0.3.3 kivy-deps.glew-0.3.1 kivy-deps.sdl2-0.6.0 pypiwin32-223

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import MDScreen


class SampleApp(MDApp):
    def build(self):
        screen = MDScreen()
        btn = MDRectangleFlatButton(text="Lednicka!",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                    )
        screen.add_widget(btn)
        return screen


SampleApp().run()