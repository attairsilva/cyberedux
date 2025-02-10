from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import os

class HomeScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Slategray"
        try:
            KV_PATH = os.path.join(os.path.dirname(__file__), "interface", "homed.kv")
            print(f"Tentando carregar arquivo KV de: {KV_PATH}")
            return Builder.load_file(KV_PATH)  # Tente carregar e retornar
        except Exception as e:  # Se ocorrer um erro
            print(f"Erro ao carregar arquivo KV: {e}")
            # Se o carregamento falhar, retorne um widget simples para evitar a tela preta
            return MDScreen(MDLabel(text="Erro ao carregar o layout."))
        finally:
            print("Fim da tentativa de carregamento do arquivo KV.")

if __name__ == '__main__':
    MyApp().run()