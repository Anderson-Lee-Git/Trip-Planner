from datetime import datetime as dt
from datetime import date as dd
import json
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from DataStructures.Event import *

def test_event_time():
    start_time = dt(2022, 8, 20, 8, 20)
    end_time = dt(2022, 9, 30, 2, 20)
    e = Event("e1", start_time, end_time, "home")
    print(e.get_id())
    t = {
        "start_time": start_time,
        "end_time": end_time
    }
    json_data = json.dumps(t, default=default)
    print(json_data)

def default(obj):
    if isinstance(obj, (dd, dt)):
        return obj.isoformat()

test_event_time()
