from dataclasses import dataclass
from enum import Enum
from datetime import date


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobbies(Enum):
    SPORTS = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


class State(Enum):
    NCR = 'NCR'
    UTTAR_PRADESH = 'Uttar Pradesh'
    HARYANA = 'Haryana'
    RAJASTHAN = 'Rajasthan'


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: Gender
    user_number: str
    date_of_birth: date
    subject: str
    hobbies: Hobbies
    file: any
    current_address: str
    state: State
    city: str


student = User(
    first_name='Lucy',
    last_name='Bechtel',
    user_email='aslavret87@gmail.com',
    gender=Gender.FEMALE,
    user_number='0123456789',
    date_of_birth=date(year=2005, month=7, day=20),
    subject='Arts, English',
    hobbies=Hobbies.READING,
    file='original.jpg',
    current_address='426 Jordy Lodge Cartwrightshire, SC 88120-6700',
    state=State.HARYANA,
    city='Noida'
)
