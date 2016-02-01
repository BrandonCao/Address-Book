"""No Entry Selected Window

Authors: Austin Gheen, Travis Barnes

Window that pops up when user tries to edit or delete with no entry selected.
"""
import tkinter as Tk

class ConfirmationWindow(object):
	
	def ok(self):
		self.top.destroy()
	

	def __init__(self, master):
		top = self.top = Tk.Toplevel(master)
		self.master = master
		top.title('Oops!')

		self.label = Tk.Label(top, text = 'No entry selected')
		self.label.grid(row = 0, column = 0, padx = 10, pady = 10)

		self.yes_button = Tk.Button(top, text = 'Ok', command = self.ok )
		self.yes_button.grid(row = 1)