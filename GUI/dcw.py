"""Delete Confirmation Window

Authors: Austin Gheen, Brandon Cao, Travis Barnes

Confirmation window that pops up when a user chooses to delete a contact.
"""

import tkinter as Tk
import gui
import db

class ConfirmationWindow(object):
	
	def yes(self):
		"""Confirm the deletion of a contact."""
		name = self.name

		gui.mainWindow(self.master).delete_contact(name)
		db.db_commit()
		self.top.destroy()


	def no(self):
		"""Decline the deletion of a contact."""
		gui.mainWindow(self.master).search_query(gui.mainWindow(
			self.master).sort.get())
		self.top.destroy()

	
	def __init__(self, master, name):
		top = self.top = Tk.Toplevel(master)
		self.master = master
		self.name = name
		top.title('Confirm')

		self.label = Tk.Label(top, text = '''Are you sure you want to delete this contact?''')
		self.label.grid(row = 0, column = 1, padx = 20, pady = 10)

		self.yes_button = Tk.Button(top, text = 'Yes', command = self.yes )
		self.yes_button.grid(row = 1, column = 1)

		self.no_button = Tk.Button(top, text = 'No', command = self.no)
		self.no_button.grid(row = 2, column = 1,pady = 10)