import os
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

class LiveApp(MDApp, App):
    """ Hi Windows users """
    DEBUG = 1 # set this to 0 make live app not working
    KV_FILES = {
        os.path.join(os.getcwd(), "tela/screenmanager.kv"),
        os.path.join(os.getcwd(), "login/loginscreen.kv"),
    }
    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "tela.screenmanager",
        "LoginScreen": "login.loginscreen",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    def build_app(self):
        self.theme_cls.primary_palette = "Green"
        return Factory.MainScreenManager()

if __name__ == "__main__":
    LiveApp().run()