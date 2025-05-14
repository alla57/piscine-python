from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Kill a Baratheon"""
        self.is_alive = False

    def __str__(self):
        """Baratheon as a string"""
        return f"Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

    def __repr__(self):
        """Baratheon repr"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill a Lannister"""
        self.is_alive = False

    def __str__(self):
        """Lannister as a string"""
        return f"Vector: ({self.family_name!r}, {self.eyes!r}, {self.hairs!r})"

    def __repr__(self):
        """Lannister repr"""
        return self.__str__()

    @classmethod
    def create_Lannister(cls, first_name, is_alive=True):
        """Creates a Lannister and returns it"""
        return cls(first_name, is_alive)
