import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.recycleview import RecycleView
from flowerbase import FlowerBase


class MainScreen(Screen):
    pass


fb = FlowerBase("database.txt")

class AddingPlantScreen(Screen):
    plant_name = ObjectProperty(None)
    water_freq = ObjectProperty(None)
    last_water_date = ObjectProperty(None)
    last_water_hour = ObjectProperty(None)

    def reset(self):
        self.plant_name.text = ""
        self.water_freq.text = ""
        self.last_water_date.text = ""
        self.last_water_hour.text = ""

    def submit(self):
        print(self.plant_name.text, self.water_freq.text, self.last_water_date.text, self.last_water_hour.text)
        fb.add_plant(self.plant_name.text, self.water_freq.text, self.last_water_date.text, self.last_water_hour.text)
        self.reset()

class PlantListScreen(Screen):
    pass

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

class FlowerSurvivalApp(App):

    def build(self):
        Builder.load_file("flowersurvival.kv")
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddingPlantScreen(name='add_plant'))
        sm.add_widget(PlantListScreen(name='plant_list'))
        return sm

if __name__ == '__main__':
    FlowerSurvivalApp().run()
