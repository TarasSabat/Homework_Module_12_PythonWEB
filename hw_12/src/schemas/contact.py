from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional

from src.schemas.user import UserResponse


class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_info: Optional[str] = None


class ContactCreate(ContactBase):
    pass


class ContactUpdate(ContactBase):
    pass


class Contact(ContactBase):
    id: int


    class Config:
        from_attributes = True
