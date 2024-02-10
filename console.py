#!/usr/bin/python3
"""
The console
"""
import cmd
import uuid
from models.base_model import BaseModel
from models import storage
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re

class HBNBCommand(cmd.Cmd):
	objects = {'BaseModel': BaseModel, 'User': User,
		   'Place' : Place, 'State' : State,
		   'City' : City, 'Amenity' : Amenity, 'Review' :Review
		  }

	prompt = "(hbnb) "

	def do_quit(self, line):
		"""method to quit the program"""
		return True;
	def do_EOF(self,line):
		"""method to end program using (Ctrl + D)"""
		return True;

	def do_help_quit(self,line):
		"""Quit command to exit"""

		print("Quit command to exit the program")
		
	def do_empty_line(self):
		"""handles empty line"""
		pass
	def do_create(self,class_name):
		"""Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
		Ex: $ create BaseModel
		"""
		if class_name == "":
			print("** class name missing **")
		else:
			try:
				class_obj = eval(class_name)
				new_instance = class_obj()
				new_instance.save()
				print(new_instance)
				print(new_instance.id)
			except(NameError):
				print("** class doesn't exist **")
	def do_show(self, line):
		"""Prints the string representation of an instance based on the class name and id.
		Ex: $ show BaseModel 1234-1234-1234.
		"""
		class_name_id = line.split()

		if len(class_name_id) == 0:
			print("** class name missing **")

		elif class_name_id[0] in HBNBCommand.objects.keys():
			if len(class_name_id) < 2 or class_name_id[1] == "":
				print("** instance id missing **")
				return
			all_objs = storage.all()
			key1 = f"{class_name_id[0]}.{class_name_id[1]}"
			obj_keys = list(all_objs.keys())
			if key1 not in obj_keys:
				print("** no instance found **")
				return
			else:
				print(all_objs[key1])
		else:
    			print("** class doesn't exist **")
    			return
	def do_destroy(self,line):
		"""Deletes an instance based on the class name and id 
		(save the change into the JSON file). 
		Ex: $ destroy BaseModel 1234-1234-1234.
		"""
		class_name_id = line.split()
		if len(class_name_id) == 0:
			print("** class name missing **")
			return
		elif class_name_id[0] in HBNBCommand.objects.keys():
			if len(class_name_id) < 2:
				print("** instance id missing **")
				return
			all_objs = storage.all()
			key1 = f"{class_name_id[0]}.{class_name_id[1]}"
			obj_keys = list(all_objs.keys())
			if key1 not in obj_keys:
				print("** no instance found **")
			else:
				del all_objs[key1]
				storage.save()
		else:
			print("** class doesn't exist **")

	def do_all(self, args):
		"""Prints all string representation of all instances based or not on the class name.
		Ex: $ all BaseModel or $ all.
		"""
		token = args.split()
		if args == "" or token[0] in HBNBCommand.objects.keys():
			all_objs = storage.all()
			str_rep = []
			for obj_id in all_objs.keys():
				str_rep.append(str(all_objs[obj_id]))
			if str_rep:
				print(str_rep)
			else:
				print("** no instances found **")
		else:
			print("** class doesn't exist **")

			
	def do_update(self,line):
		"""updates instance based on classname and id.
		Usage: update <class name> <id> <attribute name> "<attribute value>"
		save: saves the updated instance to json file
		"""
		args_lists = line.split()
		if len(args_lists) == 0:
			print("** class name missing **")
			return
		if args_lists[0] in HBNBCommand.objects.keys():
			
			if len(args_lists) < 2:
				print("** instance id missing **")
			obj_dict = storage.all()
			keys = f"{args_lists[0]}.{args_lists[1]}"
			obj_keys = list(obj_dict.keys())
			if keys not in obj_keys:
 				print("** no instance found ** ")
			else:
				if len(args_lists) < 3:
					print("** attribute name missing **")
					return
				if len(args_lists) < 4:
					print("** value missing **")
					return
				if args_lists[3].startswith('"') and args_lists[3].endswith('"'):
					args_lists[3] = args_lists[3][1:-1]
				instance = obj_dict[keys]
				attribute_name = args_lists[2]
				attribute_value = args_lists[3]
				setattr(instance, attribute_name, attribute_value)
				storage.save()
		else:
			print("** class doesn't exist **")
			return
	
	def default(self, line):
		"""
		default is called when unknown command is passed
		"""
		unknown_command = line.split(".")
		if unknown_command[0] in HBNBCommand.objects.keys():
			if len(unknown_command) != 2:
				return
			splited_command  = unknown_command[1].strip(')').split('(')
			cmd_command = splited_command[0]
			if unknown_command[1] == "all()":
				str_rep = []
				obj_dict = storage.all()
				for class_name_id in obj_dict.keys():
					class_name = class_name_id.split('.')[0]
					if class_name == unknown_command[0]:
						str_rep.append(str(obj_dict[class_name_id]))
				print(str_rep)
			
			elif unknown_command[1] == "count()":
				num_instance = 0
				obj_dict = storage.all()
				for class_name_id in obj_dict.keys():
					class_name = class_name_id.split('.')[0]
					if class_name == unknown_command[0]:
						num_instance = num_instance + 1
				print(num_instance)

			elif cmd_command == "show":
				if len(splited_command) < 2:
					print("** instance id missing **")
				else:
					id = splited_command[1][1:-1]
				obj_id = '{} {}'.format(unknown_command[0], id)
				self.do_show(obj_id)
			elif cmd_command == "destroy":
				if len(splited_command) < 2:
					print("** instance id missing **")
				else:
					id = splited_command[1][1:-1]
					obj_id = '{} {}'.format(unknown_command[0], id)
					self.do_destroy(obj_id)

			elif cmd_command == "update":
				if len(splited_command) < 4:
					print("** attributes missing **")
				else:
					id = splited_command[1][1:-1]
					attribute_name = splited_command[2][1:-1]
					attribute_value = splited_command[3][1:-1]
					all_objs = storage.all()
					obj_id = '{} {}'.format(unknown_command[0], id)
					obj_keys = list(all_objs.keys())
					if obj_id in obj_keys:
						self.do_update('{} {} "{}" "{}"'.format(obj_id, attribute_name, attribute_value))

			else:
				print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
