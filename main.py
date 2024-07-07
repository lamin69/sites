from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.modalview import ModalView
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton
from ftplib import FTP, FTP_TLS
import paramiko
from pysmb.SMBConnection import SMBConnection
import os

# Set the default window background color
Window.clearcolor = (1, 1, 1, 1)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Adding Logo with Animation
        logo = Image(source='assets/logo.png', size_hint=(1, 0.3))
        layout.add_widget(logo)
        anim = Animation(opacity=1, duration=2, t='in_out_cubic')
        logo.opacity = 0
        anim.start(logo)

        self.server_input = TextInput(hint_text='Server Address', multiline=False, size_hint=(1, 0.1), padding_y=(10,10))
        self.port_input = TextInput(hint_text='Port', input_filter='int', multiline=False, size_hint=(1, 0.1), padding_y=(10,10))
        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint=(1, 0.1), padding_y=(10,10))
        self.password_input = TextInput(hint_text='Password', password=True, multiline=False, size_hint=(1, 0.1), padding_y=(10,10))
        
        self.login_btn = Button(text='Login', size_hint=(1, 0.1), background_color=(0.1, 0.5, 0.8, 1), on_press=self.do_login)
        layout.add_widget(self.server_input)
        layout.add_widget(self.port_input)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_btn)
        
        # Adding fade-in animation for the layout
        anim = Animation(opacity=1, duration=1)
        layout.opacity = 0
        anim.start(layout)

        self.add_widget(layout)

    def do_login(self, instance):
        # Placeholder for login validation
        app = App.get_running_app()
        app.root.current = 'file_browser'
        
class FileBrowserScreen(Screen):
    def __init__(self, **kwargs):
        super(FileBrowserScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Adding Header
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        back_btn = Button(text='Back', on_press=self.go_back, background_color=(0.1, 0.5, 0.8, 1))
        settings_btn = Button(text='Settings', on_press=self.open_settings, background_color=(0.1, 0.5, 0.8, 1))
        header.add_widget(back_btn)
        header.add_widget(Label(text='File Browser', font_size='20sp', color=(0.1, 0.1, 0.1, 1)))
        header.add_widget(settings_btn)
        
        layout.add_widget(header)
        
        self.file_chooser = FileChooserListView(size_hint=(1, 0.8))
        layout.add_widget(self.file_chooser)
        
        actions = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.upload_btn = Button(text='Upload', on_press=self.upload_file, background_color=(0.1, 0.7, 0.3, 1))
        self.download_btn = Button(text='Download', on_press=self.download_file, background_color=(0.1, 0.5, 0.8, 1))
        actions.add_widget(self.upload_btn)
        actions.add_widget(self.download_btn)
        
        layout.add_widget(actions)
        
        self.add_widget(layout)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'login'
    
    def open_settings(self, instance):
        app = App.get_running_app()
        app.root.current = 'settings'

    def upload_file(self, instance):
        # Placeholder for upload function
        pass

    def download_file(self, instance):
        # Placeholder for download function
        pass

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        header = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        back_btn = Button(text='Back', on_press=self.go_back, background_color=(0.1, 0.5, 0.8, 1))
        header.add_widget(back_btn)
        header.add_widget(Label(text='Settings', font_size='20sp', color=(0.1, 0.1, 0.1, 1)))
        
        layout.add_widget(header)
        
        # Settings form
        form = GridLayout(cols=2, spacing=10, size_hint=(1, 0.8))
        
        form.add_widget(Label(text='FTP Server', color=(0.1, 0.1, 0.1, 1)))
        self.ftp_server = TextInput(hint_text='FTP Server Address')
        form.add_widget(self.ftp_server)
        
        form.add_widget(Label(text='Port', color=(0.1, 0.1, 0.1, 1)))
        self.port = TextInput(hint_text='Port')
        form.add_widget(self.port)
        
        form.add_widget(Label(text='Username', color=(0.1, 0.1, 0.1, 1)))
        self.username = TextInput(hint_text='Username')
        form.add_widget(self.username)
        
        form.add_widget(Label(text='Password', color=(0.1, 0.1, 0.1, 1)))
        self.password = TextInput(hint_text='Password', password=True)
        form.add_widget(self.password)
        
        save_btn = Button(text='Save', on_press=self.save_settings, background_color=(0.1, 0.7, 0.3, 1))
        form.add_widget(save_btn)
        
        layout.add_widget(form)
        self.add_widget(layout)

    def go_back(self, instance):
        app = App.get_running_app()
        app.root.current = 'file_browser'
    
    def save_settings(self, instance):
        # Placeholder for saving settings
        popup = Popup(title='Settings Saved', content=Label(text='Settings have been saved successfully!'), size_hint=(0.6, 0.4))
        popup.open()

class LFTApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(FileBrowserScreen(name='file_browser'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm

if __name__ == '__main__':
    LFTApp().run()
