#!/usr/bin/python3
"""
The console
"""
import cmd
class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "

	def do_quit(self, line):
		"""method to quit the program"""
		return True;
	def do_EOF(self):
		"""method to end program using (Ctrl + D)"""
		return true;

	def do_help_quit(self,line):
		print("Quit command to exit the program")
		
	def do_empty_line(self):
		pass
		

if __name__ == '__main__':
    HBNBCommand().cmdloop()
