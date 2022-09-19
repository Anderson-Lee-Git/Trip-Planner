from datetime import datetime as dt

class Event:
    """
    Represent a Event instance

    Attributes
    ----------
    title : str
        The title of this event
    start_time : datetime.datetime
        The start time of this event
    end_time : datetime.datetime
        The end time of this event
    location : str
        The location of this event
    label : tuple
        A tuple of labels in this event
    description : str
        The description of this event
    """
    def __init__(self, title: str, start_time: dt, end_time: dt, location: str, label=[], description=""):
        """
        Construct a new Event with given parameters
        """
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.label = label
        self.description = description

    def get_id(self):
        return self.title + self.start_time.isoformat()

    # Check representation exposure
    def get_start(self) -> dt:
        return self.start_time

    def get_end(self) -> dt:
        return self.end_time

    def get_label(self) -> [str]:
        return self.label

    def get_description(self) -> str:
        return self.description

    def get_title(self) -> str:
        return self.title

    def get_location(self) -> str:
        return self.location

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def __hash__(self):
        return self.get_id().__hash__()
