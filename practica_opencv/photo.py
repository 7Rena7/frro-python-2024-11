from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
import time
import cv2

class Photo(App):
    def capture(self):
        camera = self.root.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("images/IMG_{}.png".format(timestr))
        print("Foto tomada", "images/IMG_{}.png".format(timestr))

    #     layout = BoxLayout(orientation='vertical')
    #     self.image = Image()
    #     layout.add_widget(self.image)
    #     layout.add_widget(Button(text="Tomar foto"))
    #     self.capture = cv2.VideoCapture(0)
    #     Clock.schedule_interval(self.load_video, 1.0/60.0)
    #     return layout
    #
    # def load_video(self, *args):
    #     ret, frame = self.capture.read()
    #     self.image_frame = frame
    #     buffer = cv2.flip(frame, 0).tostring()
    #     texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #     texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
    #     self.image.texture = texture


if __name__ == '__main__':
    Photo().run()
