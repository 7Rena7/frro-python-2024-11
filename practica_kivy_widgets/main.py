import kivy
from kivy.app import App
from datetime import datetime
import re
import pygame
from confetti import Confetti


class Widgets(App):

    def validate_dob(self, dob_text):
        try:
            dob = datetime.strptime(dob_text, '%d/%m/%Y')
            return dob.date()
        except ValueError:
            return False

    def validate_department(self, department_text):
        if department_text:
            pattern = '^[0-9]*[A-Za-z]*$'
            return bool(re.match(pattern, department_text))
        return False

    def validate_postal_code(self, postal_code_text):
        pattern = '^[A-HJ-NP-Z]{1}\d{4}$'
        return bool(re.match(pattern, postal_code_text))

    def validate_telephone(self, telephone_text):
        pattern = '^(\+54)?[0-9]{10}$'
        return bool(re.match(pattern, telephone_text))

    def validate_email(self, email_text):
        pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email_text))

    def on_form_submit(self):
        pygame.mixer.init()
        sound = pygame.mixer.Sound('submit_sound.mp3')
        if sound:
            sound.play()
        confetti = Confetti()
        current_screen = self.root.current_screen  # Get the current screen
        current_screen.add_widget(confetti)  # Add the Confetti widget to the current screen


if __name__ == '__main__':
    Widgets().run()