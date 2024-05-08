from kivy.app import App
import time


class Photo(App):
    def capture(self):
        camera = self.root.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("images/IMG_{}.png".format(timestr))
        print("Foto tomada", "images/IMG_{}.png".format(timestr))


if __name__ == '__main__':
    Photo().run()
