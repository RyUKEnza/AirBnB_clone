import uuid
import datetime
import json
from typing import Dict, Any

class BaseModel:
    """BaseModel class for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        cls_name = self.__class__.__name__
        attributes = [(key, value) for key, value in self.__dict__.items()]
        attributes_str = ", ".join(f"{key}={value}" for key, value in attributes)
        return f"[{cls_name}] ({self.id}) {{{attributes_str}}}"

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Return a dictionary representation of the BaseModel instance"""
        cls_name = self.__class__.__name__
        attributes = self.__dict__
        attributes["__class__"] = cls_name
        attributes["created_at"] = self.created_at.isoformat()
        attributes["updated_at"] = self.updated_at.isoformat()
        return attributes

    def from_json_string(json_string: str) -> "BaseModel":
        """Return a BaseModel instance from a JSON string"""
        import json
        json_dict = json.loads(json_string)
        return BaseModel(**json_dict)
