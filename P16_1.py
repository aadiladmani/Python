from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.count = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text=f"Count: {self.count}", font_size=32)
        layout.add_widget(self.label)

        self.button = Button(text="Increment", font_size=24)
        self.button.bind(on_press=self.increment_counter)
        layout.add_widget(self.button)

        return layout

    def increment_counter(self, instance):
        self.count += 1
        self.label.text = f"Count: {self.count}"

if __name__ == '__main__':
    CounterApp().run()
