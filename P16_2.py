from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.input = TextInput(hint_text="Type something...", multiline=False, font_size=20)
        self.layout.add_widget(self.input)

        self.button = Button(text="Display Text", font_size=24)
        self.button.bind(on_press=self.display_text)
        self.layout.add_widget(self.button)

        self.label = Label(text="", font_size=24)
        self.layout.add_widget(self.label)

        return self.layout

    def display_text(self, instance):
        self.label.text = f"You typed: {self.input.text}"

if __name__ == '__main__':
    TextInputApp().run()
