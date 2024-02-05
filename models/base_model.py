#!/usr/bin/python3
"""
The root class:class BaseModel
"""
import uuid
from datetime import datetime

class BaseModel:
	def __init__(self, *args, **kwargs):
		"""initialization of BaseModel"""

		self.id = str(uuid.uuid4())
		current_time = datetime.utcnow()
		self.created_at = current_time
		self.updated_at = current_time
	def __str__(self):
		"""string representation of BaseModel"""

		return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
	def save(self):
		"""update the 'update_at' attribute"""
		self.updated_at = datetime.utcnow()
	def to_dict(self):
		"""creats dictionar of the instance"""
		instance_dict = self.__dict__.copy()
		instance_dict['__class__'] = self.__class__.__name__
		for key, value in instance_dict.items():
			if key == 'created_at':
				instance_dict[key] = value.isoformat()
			elif key == 'updated_at':
				instance_dict[key] = value.isoformat()
		return instance_dict

		
