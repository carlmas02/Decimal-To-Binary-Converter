from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton,MDRaisedButton
from kivymd.uix.dialog import MDDialog
from logic import decimal_to_binary

#string Builders
from builder import top
from builder import input_

class Decimal_to_BinaryApp(MDApp):
	def show_dailog(self,title_,text_,button_text):
		self.output = MDDialog(title = title_,
								text = text_,
								buttons=[MDRaisedButton(text=button_text,
								         on_release = self.pass_screen)] )
		self.output.open()

	def build(self):
		self.theme_cls.primary_palette = "Green"
		self.theme_cls.theme_style = "Dark"
		screen = Screen()

		box =  Builder.load_string(top)
		self.put_input = Builder.load_string(input_)
		get_input = MDRectangleFlatButton(text ="Show",
						pos_hint = {"center_x":0.5,"center_y":0.4},
						on_release = self.show_binary )

		screen.add_widget(box)
		screen.add_widget(self.put_input)
		screen.add_widget(get_input)

		return screen

	def show_binary(self,obj):
		try:
			number = decimal_to_binary(int(self.put_input.text))
			self.show_dailog("Decimal to Binary",str(number),"CLEAR")
			self.output.open()
		except ValueError :
			if self.put_input.text == "":
				self.show_dailog("Error","Input is empty !","CLEAR")
			else :
				self.show_dailog("Error","Please enter an integer !","CLEAR")

	def pass_screen(self,obj):
		self.put_input.text = ''
		self.output.dismiss()


if __name__ == '__main__':
	Decimal_to_BinaryApp().run()
