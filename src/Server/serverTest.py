from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib import parse
from datetime import datetime as dt
import socketserver
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from DataStructures.Trip import *
from DataStructures.Event import *
from DataStructures.Member import *
from DataStructures.Cost import *
from DataStructures.CostManager import *

class Server(BaseHTTPRequestHandler):
    """
    Attributes
    ----------
    trip_list : dict
        (k, v) -> (the name of the trip, Trip() object)
    """
    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer):
        self.trip_list = {}
        super().__init__(request, client_address, server)

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == '/get_trip_list':
            self.get_trip_list()
        elif self.path == '/get_event_list':
            self.get_event_list(self.parse_path()['title'])
        elif self.path == '/get_member_list':
            self.get_member_list(self.parse_path()['title'])

    def get_trip_list(self):
        self.wfile.write(bytes("Get Trip List", 'utf-8'))
        res = {}
        for trip_name in self.trip_list:
            res[trip_name] = {}
            res[trip_name]["start_date"] = self.trip_list[trip_name].get_start_date()
            res[trip_name]["end_date"] = self.trip_list[trip_name].get_end_date()
        self.wfile.write(bytes(json.dumps(res), 'utf-8'))

    def get_event_list(self, title: str):
        self.wfile.write(bytes("Get Event List", 'utf-8'))
        res = []
        for e in self.trip_list[title].get_event_list():
            event = {
                "title": e.get_title(),
                "location": e.get_location(),
                "start_time": e.get_start().isoformat(),
                "end_time": e.get_end().isoformat(),
                "label": e.get_label(),
                "description": e.get_description()
            }
            res.append(event)
        self.wfile.write(bytes(json.dumps(res), 'utf-8'))

    def get_member_list(self, title: str):
        self.wfile.write(bytes("Members handle", 'utf-8'))
        res = []
        for m in self.trip_list[title].get_member_list():
            member = {
                "name": m.get_name(),
                "color": m.get_color()
            }
            res.append(member)
        self.wfile.write(bytes(json.dumps(res), 'utf-8'))

    def get_transaction_sheet(self):
        self.wfile.write(bytes("Get transaction sheet", 'utf-8'))

    def get_balance_sheet(self):
        self.wfile.write(bytes("Get balance sheet", 'utf-8'))

    def do_POST(self):
        self._set_headers()
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        print(data)
        print(type(data))
        self.wfile.write(bytes("POST request retrieved", 'utf-8'))

    def post_update_event(self, title: str, data: dict):
        self.wfile.write(bytes("Post update event", 'utf-8'))
        if self.trip_list[title].contains_event(data["original_ID"]):
            self.trip_list[title].delete_event("original_ID")
        self.trip_list[title].add_event(
            data["title"],
            dt.fromisoformat(data["start_time"]),
            dt.fromisoformat(data["end_time"]),
            data["label"],
            data["location"],
            data["description"]
        )

    def post_add_member(self, title: str, data: dict):
        self.wfile.write(bytes("Post add member", 'utf-8'))
        self.trip_list[title].add_member(data["name"], data["color"])

    def post_delete_member(self, title: str, data: dict):
        self.wfile.write(bytes("Post delete member", 'utf-8'))
        self.trip_list[title].delete_member(data["name"])

    def update_cost_handle(self):
        self.wfile.write(bytes("Cost updated", 'utf-8'))

    def parse_path(self) -> dict:
        return dict(parse.parse_qsl(parse.urlsplit(self.path).query))



def main():
    web_server = HTTPServer(('localhost', 8080), Server)
    print("local server started at localhost port 8080")
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    main()
