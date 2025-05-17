import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random ID string of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A dataclass representing a student"""
    name: string
    surname: string
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        if self.name and isinstance(self.name, str):
            self.login = self.name[0] + self.surname
        else:
            self.login = self.surname
        self.id = generate_id()
