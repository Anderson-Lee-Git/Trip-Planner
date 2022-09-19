from datetime import datetime as dt
from DataStructures.Event import Event
from DataStructures.Member import Member


class Trip:
    """
    Represent a Trip containing mutable events and immutable members

    Attributes
    ----------
    events : dict
        (k, v) = (ID of the event, Event object)
    members : dict
        (k, v) = (name of the member, Member object)
    start_date : str
        the start date in the form of YYYY-MM-DD
    end_date : str
        the end date in the form of YYYY-MM-DD
    """
    def __init__(self, start_date: str, end_date: str):
        self.events = {}
        self.members = {}
        self.start_date = start_date
        self.end_date = end_date

    def get_start_date(self) -> str:
        return self.start_date

    def get_end_date(self) -> str:
        return self.end_date

    def get_event_list(self) -> tuple:
        """
        Return an immutable list of events in this trip
        """
        return tuple(self.events.values())

    def get_member_list(self) -> tuple:
        """
        Return an immutable list of members in this trip
        """
        return tuple(self.members.values())

    def get_event(self, ID: str) -> Event:
        """
        Return the event with the given ID

        Warnings
        --------
        Make sure the ID exists in this trip using .contains_event()
        """
        return self.events[ID]

    def get_member(self, name) -> Member:
        """
        Return the member with the given name

        Warnings
        --------
        Make sure the name exists in this trip using .contains_member()
        """
        return self.members[name]

    def contains_event(self, ID: str) -> bool:
        """
        Check if the given ID is an event in this event
        """
        return ID in self.events.keys()

    def contains_member(self, name: str) -> bool:
        """
        Check if the given name is a member in this event
        """
        return name in self.members.keys()

    def add_event(self, title: str, start_time: dt, end_time: dt, label: [str], location="", description="") -> None:
        """
        Add a new event with given parameters
        If duplicate event exists in the trip, then no behavior is performed
        """
        e = Event(title, start_time, end_time, location, label, description)
        if not self.contains_event(e.get_id()):
            self.events[e.get_id()] = e

    def delete_event(self, ID: str) -> None:
        """
        Delete an event in this trip with given ID
        If no such event exists, no behavior is performed
        """
        if self.contains_event(ID):
            self.events.pop(ID)

    def add_member(self, name: str, color: str) -> None:
        """
        Add a new member to this trip
        No behavior if the name exists in this trip
        """
        if not self.contains_member(name):
            self.members[name] = Member(name, color)

    def delete_member(self, name: str) -> None:
        """
        Delete an existing member in this trip
        No behavior if the name does not exist in this trip
        """
        if self.contains_member(name):
            self.members.pop(name)
