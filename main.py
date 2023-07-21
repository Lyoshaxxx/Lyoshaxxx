from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        entry = TextInput(font_size=40, readonly=True, multiline=False)

        button_layout = GridLayout(cols=4, spacing=5, padding=10)

        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
            ("C",)
        ]

        for row in buttons:
            for text in row:
                button = Button(text=text, font_size=40, on_press=self.on_button_click)
                button_layout.add_widget(button)

        main_layout.add_widget(entry)
        main_layout.add_widget(button_layout)

        return main_layout

    def on_button_click(self, instance):
        text = instance.text
        entry = self.root.children[0]
        if text == "=":
            try:
                result = eval(entry.text)
                entry.text = str(result)
            except Exception as e:
                entry.text = "Error"
        elif text == "C":
            entry.text = ""
        else:
            entry.text += text


if __name__ == "__main__":
    CalculatorApp().run()
