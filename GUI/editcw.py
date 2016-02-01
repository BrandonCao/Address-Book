"""Edit Confirmation Window

Authors: Austin Gheen, Brandon Cao, Travis Barnes

Confirmation window that pops up when user chooses to edit a contact.
"""
import tkinter as Tk
import AddressBook as ab
import db

class ConfirmationWindow(object):
	
	def yes(self):
		field_list = self.field_list
		ab.edit_contact(self.entry_id, field_list)
		db.db_commit()
		self.top.destroy()


	def no(self):
		self.top.destroy()

	
	def __init__(self,master,field_list, entry_id):
		top = self.top = Tk.Toplevel(master)
		self.master = master
		self.field_list = field_list
		self.entry_id = entry_id
		top.title('Confirm')

		self.label = Tk.Label(top, text = 'Are you sure you want to edit this contact?')
		self.label.grid(row = 0, column = 1, padx = 10, pady = 10)

		self.yes_button = Tk.Button(top, text = 'Yes', command = self.yes )
		self.yes_button.grid(row = 1, column = 1)

		self.no_button = Tk.Button(top, text = 'No', command = self.no)
		self.no_button.grid(row = 2, column = 1)