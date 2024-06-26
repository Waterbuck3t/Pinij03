import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import json

class FancyUIDisplay(App):
    def build(self):
        # Load data from data.json
        self.data = self.load_data()

        # Set the window background color to white
        Window.clearcolor = get_color_from_hex('#FFFFFF')

        # Main layout
        root_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Title label
        title_label = Label(text=self.data['title'], font_size=24, color=get_color_from_hex('#333333'), size_hint=(1, None), height=50)
        root_layout.add_widget(title_label)

        # Scroll view for data
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)
        grid_layout = self.create_grid_layout()
        scroll_view.add_widget(grid_layout)

        root_layout.add_widget(scroll_view)
        return root_layout

    def create_grid_layout(self):
        # Create a GridLayout for student data
        grid_layout = GridLayout(cols=5, spacing=10, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Add headers
        headers = ["Name", "Class", "Class Number", "Salary", "Job"]
        for header in headers:
            header_label = Label(text=header, color=get_color_from_hex('#333333'), bold=True, size_hint_y=None, height=40, valign='middle')
            grid_layout.add_widget(header_label)

        # Add student data
        for item in self.data['items']:
            name_label = Label(text=item['name'], color=get_color_from_hex('#6666ff'), size_hint_y=None, height=40, valign='middle')
            class_label = Label(text=item['class'], color=get_color_from_hex('#66cc66'), size_hint_y=None, height=40, valign='middle')
            num_label = Label(text=str(item['num']), color=get_color_from_hex('#ff6666'), size_hint_y=None, height=40, valign='middle')
            salary_label = Label(text=f"${item['salary']}", color=get_color_from_hex('#ffa500'), size_hint_y=None, height=40, valign='middle')
            job_label = Label(text=item['job'], color=get_color_from_hex('#9966cc'), size_hint_y=None, height=40, valign='middle')

            grid_layout.add_widget(name_label)
            grid_layout.add_widget(class_label)
            grid_layout.add_widget(num_label)
            grid_layout.add_widget(salary_label)
            grid_layout.add_widget(job_label)

        return grid_layout

    def load_data(self):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {'title': 'No Data Found', 'items': []}
        return data

if __name__ == '__main__':
    FancyUIDisplay().run()
