#!/usr/bin/python3
"""
This is a file storage class
"""
from models.base_model import BaseModel
import json

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
		try:
			with open(self.__file_path, "r") as file:
				loaded_object = json.load(file)
				for key, value in loaded_object.items():
					self.__objects[key] = BaseModel(**value)
					print(self.__objects[key])

		except FileNotFoundError:
        		pass
			

		
	
