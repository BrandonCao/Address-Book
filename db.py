"""Address Book Database

Author: Travis Barnes, January 16 2016

This program creates, modifies (insert, delete, update), and queries a
SQLite database filled with address book entries.
"""

import sqlite3 as sql
import os.path as path
import config as cfg


def db_init(db_name):
	"""Create/Open and initialize a database.

	Keyword arguments:
	db_name -- Name of the new database file
	"""	

	if db_exists(db_name) == True:
		cfg.DB = sql.connect(db_name + '.ab')
		cfg.C = cfg.DB.cursor()
		print('Database already exists')

	else:
		cfg.DB = sql.connect(db_name + '.ab')
		cfg.C = cfg.DB.cursor()
		create_table = '''CREATE TABLE Contacts(First TEXT, 
					Last TEXT, Street1 TEXT, Street2 TEXT, City TEXT, State TEXT,
					Zip TEXT, Home TEXT, Mobile TEXT, Email TEXT, Birthday TEXT, 
					Notes TEXT) '''	
		cfg.C.execute(create_table)
		cfg.DB.commit()
		print('New table created')
	

def db_exists(db_name):
	"""Checks whether db exists.

	Keyword arguments:
	db_name -- Name of a database file
	"""

	if (path.isfile(db_name + '.ab')):
		return True
	else:
		return False


def get_id(entry):
	"""Gets database ID number from an entry

	Keyword arguments:
	entry - A list object
	"""

	entry_id = "SELECT rowid, * FROM Contacts WHERE First = ? AND Last = ?"
	cfg.C.execute(entry_id, [entry[0], entry[1]])

	for row in cfg.C:
		return row[0]


def insert_entry(entry):
	"""Inserts a new entry into database.

	Keyword arguments:
	entry -- A list object 
	"""

	cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
		entry)

	cfg.DB.commit()


def delete_entry(entry_id):
	"""Removes entry from database.

	Keyword arguments:
	entry_id -- Corresponding ID number for an entry
	"""

	cfg.C.execute("DELETE FROM Contacts WHERE rowid = ?", [entry_id])


def get_entry(entry_id):
	"""Queries entry from database.

	Keyword arguments:
	entry_id -- Corresponding ID number for an entry
	"""

	cfg.C.execute("SELECT * FROM Contacts WHERE rowid = ?", [entry_id])

	return cfg.C


def db_commit():
	"""Commits all changes to database."""
	cfg.DB.commit()


def edit_entry(entry_id, entry):
	"""Updates entry in database.

	Keyword arguments:
	entry_id -- Corresponding ID number for an entry
	entry -- A list object
	"""
	entry_update = '''UPDATE Contacts SET First = ?, Last = ?, Street1 = ?,
			Street2 = ?, City = ?, State = ?, Zip = ?, Home = ?, Mobile = ?, 
			Email = ?, Birthday = ?, Notes = ? WHERE rowid = ? '''

	cfg.C.execute(entry_update, [entry[0], entry[1], entry[2], entry[3], 
		entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10],
		entry[11], '{}'.format(entry_id)])


def query_entrylist(sort):
	"""Prints the full list of entries in database.

	Keyword arguments:
	sort -- String containing sorting method
	"""
	if sort == 'Last Name':
		last_name = '''SELECT * FROM Contacts ORDER BY Last ASC, First ASC'''
		cfg.C.execute(last_name)

	elif sort == 'Zip':
		zip_code = '''SELECT * FROM Contacts ORDER BY Zip ASC, Last ASC'''
		cfg.C.execute(zip_code)

	return cfg.C


def search_entry(str, sort):
	"""Searches the database for an entry.

	Keyword arguments:
	str -- A string containing search term
	sort -- String containg sorting method
	"""
	if sort == 'Last Name':
		search_last = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
				Street2 || City || State || Zip || Home || Mobile || Email || 
				Birthday || Notes) LIKE '%' || ? || '%' ORDER BY Last ASC, First ASC'''
		cfg.C.execute(search_last, [str]) 

	elif sort == 'Zip':
		search_zip = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
				Street2 || City || State || Zip || Home || Mobile || Email || 
				Birthday || Notes) LIKE '%' || ? || '%' ORDER BY Zip ASC, Last ASC'''
		cfg.C.execute(search_zip, [str]) 

	return cfg.C