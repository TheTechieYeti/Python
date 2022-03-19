from flask_app import app 
from flask_app.config.mysqlconnection import MySQLConnection
from flask import session, flash
import re, pprint, datetime
from flask_app.model import user, message
from datetime import date, time, datetime, timedelta

db="iSport_schema"

class Event:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.information = data['information']
        self.max_members = data['max_members']
        self.start_time = data['start_time']
        self.date = data['date']
        self.start_time = data['start_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.attendees = []
        self.location = []
        self.messages = []
    def capacity(self):
        return f"{len(self.attendees)}/{self.max_members}"
    def full_capacity(self):
        yes_no = False
        if len(self.attendees) == self.max_members:
            yes_no = True
        return yes_no
    def event_today(self):
        today = date.today()
        if self.date == today:
            return True
        return False
    def event_future(self):
        today = date.today()
        if self.date >= today:
            return False
        return True
    def format_date(self):
        return self.date.strftime("%a %b %d, %Y")
    def format_time(self):
        print(type(self.start_time))
        return self.start_time.strftime("%I:%M %p")
    @classmethod
    def create_event(cls,data):
        query = """INSERT INTO events (user_id ,name, information, max_members, start_time, date)
        VALUES (%(user_id)s, %(name)s,%(information)s,%(max_members)s,%(start_time)s,%(date)s);"""
        return MySQLConnection(db).query_db(query, data)
    @classmethod
    def create_event_message(cls,data):
        query = """INSERT INTO messages (user_id, event_id, content)
        VALUES (%(user_id)s,%(event_id)s,%(content)s);"""
        return MySQLConnection(db).query_db(query,data)
    @classmethod
    def get_all_events_with_creator_attendees(cls):
        query = """SELECT * FROM events
            LEFT JOIN users AS creator on creator.id = user_id
            LEFT JOIN attendees on attendees.event_id = events.id
            LEFT JOIN users as attendee on attendees.user_id = attendee.id;"""
        results = MySQLConnection(db).query_db(query)
        all_events=[]
        count=0
        iterations = len(results)
        for i in results:
            count = count + 1   #tracks the number of iterations we do 
            creator_info = {
                "id" : i['creator.id'],
                "first_name" : i['first_name'],
                "last_name" : i['last_name'],
                "email" : i['email'],
                "password" : i['password'],
                "birthday" : i['birthday'],
                "img_path"    : i['img_path'],
                "created_at" : i['creator.created_at'],
                "updated_at" : i['creator.updated_at'],
            }
            attendee_info = {
                "id" : i['attendee.id'],
                "first_name" : i['attendee.first_name'],
                "last_name" : i['attendee.last_name'],
                "email" : i['attendee.email'],
                "password" : i['attendee.password'],
                "birthday" : i['attendee.birthday'],
                "img_path"    : i['img_path'],
                "created_at" : i['attendee.created_at'],
                "updated_at" : i['attendee.updated_at'],
            }
            if count == 1:    #triggers on first iteration only 
                this_event = cls(i)
                creator = user.User(creator_info)
                this_event.creator = creator
                this_event.attendees.append(creator)
            if i['id'] != this_event.id:   #triggers only on iteration with new event info
                all_events.append(this_event)   #Adds our super associated event
                this_event = cls(i)
                creator = user.User(creator_info)
                this_event.creator = creator
                this_event.attendees.append(creator)
            if i['attendee.id'] and i['attendee.id'] != this_event.attendees[-1].id:
                this_event.attendees.append(user.User(attendee_info))
            if count == iterations:
                all_events.pop    #removes our plain jane event
                all_events.append(this_event)  #appends our supers associated event
        return all_events
    @classmethod
    def get_event_with_creator_attendees_by_event_id(cls, data):
        query = """SELECT * FROM events
            LEFT JOIN users AS creator on creator.id = user_id
            LEFT JOIN attendees on attendees.event_id = events.id
            LEFT JOIN users as attendee on attendees.user_id = attendee.id
            LEFT JOIN messages ON messages.event_id = events.id
            LEFT JOIN users AS mc on messages.user_id = mc.id
            WHERE events.id = %(id)s;"""
        results = MySQLConnection(db).query_db(query,data)
        count=0
        iterations = len(results)
        for i in results:
            count = count + 1   #tracks the number of iterations we do 
            creator_info = {
                "id" : i['creator.id'],
                "first_name" : i['first_name'],
                "last_name" : i['last_name'],
                "email" : i['email'],
                "password" : i['password'],
                "img_path"    : i['img_path'],
                "birthday" : i['birthday'],
                "created_at" : i['creator.created_at'],
                "updated_at" : i['creator.updated_at'],
            }
            attendee_info = {
                "id" : i['attendee.id'],
                "first_name" : i['attendee.first_name'],
                "last_name" : i['attendee.last_name'],
                "email" : i['attendee.email'],
                "password" : i['attendee.password'],
                "img_path"    : i['img_path'],
                "birthday" : i['attendee.birthday'],
                "created_at" : i['attendee.created_at'],
                "updated_at" : i['attendee.updated_at'],
            }
            mc_info = {
                "id" : i['mc.id'],
                "first_name" : i['mc.first_name'],
                "last_name" : i['mc.last_name'],
                "email" : i['mc.email'],
                "password" : i['mc.password'],
                "birthday" : i['mc.birthday'],
                "created_at" : i['mc.created_at'],
                "updated_at" : i['mc.updated_at'],
            }
            message_info = {
                "id" : i['messages.id'],
                "user_id" : i['messages.user_id'],
                "event_id" : i['messages.event_id'],
                "content" : i['content'],
                "created_at" : i['messages.created_at'],
                "updated_at" : i['messages.updated_at'],
            }
            if count == 1:    #triggers on first iteration only
                pprint.pprint(i, sort_dicts=False)
                this_event = cls(i)
                creator = user.User(creator_info)
                this_event.creator = creator
                this_event.attendees.append(creator)
            if i['attendee.id'] and i['attendee.id'] != this_event.attendees[-1].id:
                this_attendee = user.User(attendee_info)
                this_event.attendees.append(this_attendee)
            if i['messages.id'] and len(this_event.messages) == 0:
                this_message = message.Message(message_info)
                this_message.creator = user.User(mc_info)
                this_event.messages.append(this_message)
            if i['messages.id'] and i['messages.id'] != this_event.messages[-1].id:
                this_message = message.Message(message_info)
                this_message.creator = user.User(mc_info)
                this_event.messages.append(this_message)
            if count == iterations:
                return this_event
    @classmethod
    def join_event(cls, data):
        query = """INSERT INTO attendees (event_id, user_id)
        VALUES(%(event_id)s,%(user_id)s)"""
        this_attendee = MySQLConnection(db).query_db(query, data)
        print(this_attendee)
        return 
    @classmethod
    def unjoin_event(cls, data):
        query = """DELETE FROM attendees 
        WHERE user_id = %(user_id)s
        AND event_id = %(event_id)s"""
        MySQLConnection(db).query_db(query,data)
    
        return 
    @staticmethod
    def validate_report(event):
        is_valid = True
        if not event['name']:
            flash("Please enter an event name")
            is_valid = False
        elif len(event['name']) < 2:
            flash("Event Name must be at least 2 characters")
            is_valid = False
        if not event['information']:
            flash("Please enter information about the event ")
            is_valid = False
        elif len(event['information']) < 3:
            flash("Event information must be at least 3 characters")
            is_valid = False
        if not event['date']:
            flash("Please pick a date")
            is_valid = False
        if not event['max_members']:
            flash("Please pick a maximum amount of participants")
            is_valid = False
        if not event['start_time']:
            flash("Please select a starting time for your event")
            is_valid = False
        
        return is_valid