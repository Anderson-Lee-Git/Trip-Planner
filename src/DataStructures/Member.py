class Member:
    """
    Represent a Member with name, color, and balance

    Attributes
    ----------
    name : str
        The name of this member
    color : str
        The color of this member
    balance : float
        The current balance of this member
    """
    def __init__(self, name: str, color: str):
        """
        Construct an instance of Member
        """
        self.name = name
        self.color = color
        self.balance = 0.0

    def get_name(self) -> str:
        return self.name

    def get_color(self) -> str:
        return self.color

    def get_balance(self) -> float:
        return self.balance

    def set_color(self, color: str):
        """
        Set the color of this member with a given color
        """
        self.color = color

    def set_balance(self, balance: float):
        """
        Set the balance of this member with a given balance
        """
        self.balance = balance

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name.__hash__()