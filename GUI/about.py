"""Address Book About page

Authors: Austin Gheen, Travis Barnes

Window to displays developer and application information.
"""
import tkinter as Tk

class About_Window(object):

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title("About Us")

		# Team Cowsay logo
		self.photo = Tk.PhotoImage(master = top, file = "GUI/logo.gif")
		self.photo_label = Tk.Label(top, image = self.photo)
		self.photo_label.grid(row = 0, column = 0)

		# Application information
		self.label = Tk.Label(top, text = "Address Book by Team Cowsay\n Version 1.0\n Copyright © 2016")
		self.label.grid(row = 1, column = 0, padx = 10, pady =10 )


