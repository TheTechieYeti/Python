from flask_app import app 
from flask_app.config.mysqlconnection import MySQLConnection
from flask import session, flash
import re, pprint, datetime
from flask_app.model import user
from datetime import date

db="iSport_schema"

class Message: 
    def __init__(self,data):
        self.id = data['id']
        self.event_id = data['event_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None