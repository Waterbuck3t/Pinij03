from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import json

class JSONDisplayApp(App):

    def build(self):
        # Load JSON data from file
        with open('data.json', 'r') as f:
            self.json_data = json.load(f)
        
        # Create UI
        layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Display JSON data
        for key, value in self.json_data.items():
            label_text = f"{key}: {value}"
            label = Label(text=label_text, size_hint_y=None, height=40)
            layout.add_widget(label)
        
        # Button to update age
        update_button = Button(text='Update Age', size_hint=(None, None), size=(150, 50))
        update_button.bind(on_press=self.update_age)
        layout.add_widget(update_button)
        
        return layout
    
    def update_age(self, instance):
        # Example function to update age in JSON and UI
        new_age = int(self.json_data['age']) + 1
        self.json_data['age'] = new_age
        
        # Update UI with new age
        for widget in self.root.children:
            if isinstance(widget, Label):
                if widget.text.startswith('age'):
                    widget.text = f"age: {new_age}"
        
        # Optionally, save updated JSON back to file
        with open('data.json', 'w') as f:
            json.dump(self.json_data, f)

if __name__ == '__main__':
    JSONDisplayApp().run()
