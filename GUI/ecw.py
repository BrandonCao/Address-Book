"""Edit Contact Window

Authors: Austin Gheen, Travis Barnes

Window that pops up when user chooses to edit a contact.
"""

import tkinter as Tk
import AddressBook as ab
import editcw
import addcw
import gui

class EditContactWindow(object):

	def popup_confirmation(self, field_list, entry_id):
		"""Open confirmation window

		Keyword arguments:
		field_list -- A list containing contact information
		entry_id -- The rowid for the contact being edited
		"""
		self.c=editcw.ConfirmationWindow(self.master, field_list, entry_id)
		self.master.wait_window(self.c.top)


	def field_return(self):
		"""Grabs contact form data and returns it to popup_confirmation()"""

		# List to hold form data
		field_list = ['','','','','','','','','','','','']

		# Get form data
		first = self.first_name.get()
		last = self.last_name.get()
		st1 = self.address1.get()
		st2 = self.address2.get()
		city = self.city.get()
		state = self.state.get()
		zip = self.zip.get()
		home = self.home.get()
		mobile = self.mobile.get()
		email = self.email.get()
		bday = self.birthday.get()
		notes = self.notes.get()

		field_vars = [first, last, st1, st2, city, state, zip, home, mobile,
			 email, bday, notes]

		# Add form data to field_list
		for i in range(12):
			field_list[i] = field_vars[i]

		# If contact entry has a first name, ask user to confirm edit. 
		#	Else, warn user there is no first name.
		if field_list[0] != '':
			self.popup_confirmation(field_list, self.entry_id)

		else: 
			self.c=addcw.ConfirmationWindow(self.master)

		gui.mainWindow(self.master).search_query(gui.mainWindow(
			self.master).sort.get())
		self.close_window()


	def close_window(self):
		self.top.destroy()


	def grab_contact(self):
		"""Inserts contact information into fields."""

		name_entry = ab.get_contact(self.name)

		self.first_name.insert(0,str(name_entry[0]))
		self.last_name.insert(0,str(name_entry[1]))
		self.address1.insert(0,str(name_entry[2]))
		self.address2.insert(0,str(name_entry[3]))
		self.city.insert(0,str(name_entry[4]))
		self.state.insert(0,str(name_entry[5]))
		self.zip.insert(0,str(name_entry[6]))
		self.home.insert(0,str(name_entry[7]))
		self.mobile.insert(0,str(name_entry[8]))
		self.email.insert(0,str(name_entry[9]))
		self.birthday.insert(0,str(name_entry[10]))
		self.notes.insert(0,str(name_entry[11]))


	def clear_text_entries(self):
		"""Clears any value in text fields."""

		self.first_name.delete(0,Tk.END)
		self.last_name.delete(0,Tk.END)
		self.address1.delete(0,Tk.END)
		self.address2.delete(0,Tk.END)
		self.city.delete(0,Tk.END)
		self.state.delete(0,Tk.END)
		self.zip.delete(0,Tk.END)
		self.home.delete(0,Tk.END)
		self.mobile.delete(0,Tk.END)
		self.email.delete(0,Tk.END)
		self.birthday.delete(0,Tk.END)
		self.notes.delete(0,Tk.END)
		

	def __init__(self, master, name, entry_id):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		self.name = name
		self.entry_id = entry_id
		top.title('Edit Contact')

		self.first_name_label = Tk.Label(top, text = 'First Name:')
		self.first_name_label.grid()

		#input for contacts first name
		self.first_name = Tk.Entry(top)
		self.first_name.grid(row = 0, column = 1, padx = 10)

		self.last_name_label = Tk.Label(top, text = 'Last Name:')
		self.last_name_label.grid(row = 1) 

		#input for contacts last name
		self.last_name = Tk.Entry(top)
		self.last_name.grid(row = 1, column = 1)

		self.address1_label = Tk.Label(top, text = 'Address 1:')
		self.address1_label.grid(row = 2)

		#input for contacts address1
		self.address1 = Tk.Entry(top)
		self.address1.grid(row = 2, column = 1)

		self.address2_label = Tk.Label(top, text = 'Address 2:')
		self.address2_label.grid(row = 3)

		#input for contacts address2
		self.address2 = Tk.Entry(top)
		self.address2.grid(row = 3, column = 1)

		self.city_label = Tk.Label(top, text = 'City:')
		self.city_label.grid(row = 4)

		#input for contacts city
		self.city = Tk.Entry(top)
		self.city.grid(row = 4, column = 1)

		self.state_label = Tk.Label(top, text = 'State:')
		self.state_label.grid(row = 5)

		#input for contacts state
		self.state = Tk.Entry(top)
		self.state.grid(row = 5, column = 1 )

		self.zip_label = Tk.Label(top, text= 'Zip:')
		self.zip_label.grid(row = 6)

		#input for the contacts zip
		self.zip = Tk.Entry(top)
		self.zip.grid(row = 6, column = 1)

		# Input for contact home phone
		self.home_label = Tk.Label(top, text = 'Home Phone:')
		self.home_label.grid(row = 7)

		self.home = Tk.Entry(top)
		self.home.grid(row = 7, column = 1)

		# Input for contact mobile phone
		self.mobile_label = Tk.Label(top, text = 'Mobile Phone:')
		self.mobile_label.grid(row = 8)

		self.mobile = Tk.Entry(top)
		self.mobile.grid(row = 8, column = 1)
		
		self.email_label = Tk.Label(top, text = 'Email:')
		self.email_label.grid(row = 9)

		#input for contacts email
		self.email = Tk.Entry(top)
		self.email.grid(row = 9, column = 1)

		self.birthday_label = Tk.Label(top, text = 'Birthday:')
		self.birthday_label.grid(row = 10)

		#input for contacts birthday
		self.birthday = Tk.Entry(top)
		self.birthday.grid(row = 10, column = 1)

		self.notes_label = Tk.Label(top, text = "Notes")
		self.notes_label.grid(row = 11)

		#input for notes on contact
		self.notes = Tk.Entry(top)
		self.notes.grid(row = 11, column = 1)

		self.clear_text_entries()
		self.grab_contact()

		self.save_button = Tk.Button(top, text= 'Save', command = self.field_return )
		self.save_button.grid(row = 12, column = 1, padx = 10 ,sticky = Tk.E)

		self.cancel_button = Tk.Button(top, text = 'Cancel', command = self.close_window )
		self.cancel_button.grid(row = 12, column = 1)

