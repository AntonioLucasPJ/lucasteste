from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
KV = """
<ScreenOne>:
    name :"s1"
    md_bg_color: 1, 0.5, 1, 1
    MDRaisedButton:
        text:"Next Screen"
        pos_hint : {'center_x': .5,'center_y': .5}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current='s2'             

<ScreenTwo>:
    name :'s2'
    md_bg_color: .2, .5, 1, 1
    MDRaisedButton:
        text:"back"
        pos_hint : {'center_x': .5,'center_y': .5}
        on_release:
            root.manager.transition.diretion ='up'
            root.manager.current='s1'

"""
class ScreenOne(MDScreen):
    pass
class ScreenTwo(MDScreen):
    pass
class MainApp(MDApp):
    def build(self):
        Builder.load_string(KV)
        sm = MDScreenManager()
        sm.add_widget(ScreenOne())
        sm.add_widget(ScreenTwo())
        return sm 

MainApp().run()