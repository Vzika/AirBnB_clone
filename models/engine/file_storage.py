#!/usr/bin/python3
"""
This is a file storage class
"""
from models.base_model import BaseModel
import json
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
	__file_path = 'file.json'
	__objects = {}
	def all(self):
		"""Returns all the __object dict"""
		return self.__objects
	def new(self, obj):
		""" Adds a new obj to __object dict.This ensures that each object is stored with a unique identifier in the dictionary."""
		key = f"{obj.__class__.__name__}.{obj.id}"
		self.__objects[key] = obj
	def save(self):
		"""serializes __object to json file __file_path"""
		serialized_objects = {}
		for key, value in self.__objects.items():
			serialized_objects[key] = value.to_dict()
		with open(self.__file_path, "w") as file:
			json.dump(serialized_objects, file)
	def reload(self):
		"""Deserializes the json files back to python __objects"""
		current_classes = {'BaseModel': BaseModel, 'User': User,
				   'Place' : Place, 'State' : State,
				   'City' : City, 'Amenity' : Amenity, 'Review' : Review
				  }
		try:
			with open(self.__file_path, "r") as file:
				loaded_object = json.load(file)
				for key, value in loaded_object.items():
					class_name, obj_id = key.split('.')
					if class_name in current_classes:
						class_obj_name = current_classes[class_name]
						instance = class_obj_name(**value)
						self.__objects[key] =  instance
		except FileNotFoundError:
        		pass

		
	
