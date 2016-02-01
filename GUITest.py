import threading
import AddressBook as ab
import gui
import tkinter as Tk

class EventGen(threading.Thread):
	def __init__(self, target):
		threading.Thread.__init__(self)
		self.target = target
	
	def run(self):
		#let gui start
		import time
		time.sleep(0.2)



		try:
			#force focus to widget
			self.target.add_button.focus_force()

			self.target.add_button.event_generate('<Motion>', warp=True, x=10, y=10)

			self.target.add_button.update()


			#generate mouse 1
			self.target.add_button.event_generate("<Button-1>",x=10, y=10)

			self.target.add_button.update()

			self.target.add_button.event_generate("<ButtonRelease-1>", x=10, y=10)

			self.target.add_button.update()
			print("add succeeded")
		except:
			print("add failed")

		try:
			#force focus to widget
			self.target.delete_button.focus_force()

			self.target.delete_button.event_generate('<Motion>', warp=True, x=10, y=10)

			self.target.delete_button.update()


			#generate mouse 1
			self.target.delete_button.event_generate("<Button-1>",x=10, y=10)

			self.target.delete_button.update()

			self.target.delete_button.event_generate("<ButtonRelease-1>", x=10, y=10)

			self.target.delete_button.update()
			print("delete succeeded")
		except:
			print("delete failed")

		
		try:
			#force focus to widget
			self.target.sort_option_menu.focus_force()

			self.target.sort_option_menu.event_generate('<Motion>', warp=True, x=10, y=10)

			self.target.sort_option_menu.update()
			
			
			#generate mouse 1
			self.target.sort_option_menu.event_generate("<Button-1>",x=10, y=10)

			self.target.sort_option_menu.update()

			self.target.sort_option_menu.event_generate("<ButtonRelease-1>", x=10, y=10)

			self.target.sort_option_menu.update()
			print("sort succeeded")
		except:
			print("sort failed")

		self.target.quit()








if __name__ == "__main__":
	ab.new_book()
	root = Tk.Tk()
	gui = gui.mainWindow(root)
	
	egen = EventGen(gui)
	
	egen.start()
	root.mainloop()

