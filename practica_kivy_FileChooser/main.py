import os
import platform
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView

class FileChooser(BoxLayout):
    def __init__(self, **kwargs):
        super(FileChooser, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label = Label(text='Seleccione un archivo')
        self.add_widget(self.label)

        self.filechooser = FileChooserListView()
        self.filechooser.bind(on_selection=self.on_file_select)
        self.add_widget(self.filechooser)

        self.open_button = Button(text='Abrir')
        self.open_button.bind(on_press=self.open_file)
        self.add_widget(self.open_button)

    def on_file_select(self, filechooser, selection):
        if selection:
            self.label.text = selection[0]

    def open_file(self, instance):
        if self.filechooser.selection:
            selected_file = self.filechooser.selection[0]
            self.open_with_default_app(selected_file)

    def open_with_default_app(self, file_path):
        try:
            if platform.system() == 'Darwin':  # macOS
                os.system(f'open "{file_path}"')
            elif platform.system() == 'Windows':  # Windows
                os.system(f'start "" "{file_path}"')
            else:  # Linux
                os.system(f'xdg-open "{file_path}"')
        except Exception as e:
            print(f'Error opening file: {e}')

class FileChooserApp(App):
    def build(self):
        return FileChooser()

if __name__ == '__main__':
    FileChooserApp().run()
