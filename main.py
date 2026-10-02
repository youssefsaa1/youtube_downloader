import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import yt_dlp

class DownloaderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text="Enter Video URL:", font_size=18)
        self.layout.add_widget(self.label)
        
        self.url_input = TextInput(hint_text="https://...", multiline=False)
        self.layout.add_widget(self.url_input)
        
        self.download_btn = Button(text="Download Video", size_hint=(1, 0.3))
        self.download_btn.bind(on_press=self.start_download_thread)
        self.layout.add_widget(self.download_btn)
        
        self.status_label = Label(text="", font_size=14)
        self.layout.add_widget(self.status_label)
        
        return self.layout

    def start_download_thread(self, instance):
        threading.Thread(target=self.download_video).start()

    def download_video(self):
        url = self.url_input.text.strip()
        if not url:
            self.status_label.text = "Please enter a valid URL!"
            return

        self.status_label.text = "Downloading..."
        
        ydl_opts = {
            'outtmpl': '/sdcard/Download/%(title)s.%(ext)s',
            'format': 'best',
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.status_label.text = "Success! Saved in Downloads."
        except Exception as e:
            self.status_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    DownloaderApp().run()
