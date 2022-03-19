from flask_app import app
from flask import render_template, redirect, session, flash, request
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.model import user, event

@app.route('/event/new')     
def new_event():
    if 'user_id' not in session: 
        flash('You must be logged in to view this page')
        return redirect('/')
    return render_template("new_event.html", user = user.User.get_logged_in_user())

@app.route('/event/new/create', methods=['POST'])         
def create_event():
    if not event.Event.validate_report(request.form):
        return redirect ('/event/new')
    print(session['user_id'])
    data = {
        "user_id": session['user_id'],
        "name" : request.form['name'],
        "information" : request.form['information'],
        "max_members" : request.form['max_members'],
        "start_time" : request.form['start_time'],
        "date" : request.form['date'],
    }
    print(data)
    event.Event.create_event(data)
    return redirect ("/dashboard")

@app.route('/event/<int:event_id>')         
def display_event(event_id):
    if 'user_id' not in session: 
        flash('You must be logged in to view this page')
        return redirect('/')
    data = {
        "id": event_id
    }
    return render_template("event1.html", event=event.Event.get_event_with_creator_attendees_by_event_id(data), user=user.User.get_logged_in_user())

@app.route('/event/<int:event_id>/new_message', methods=["POST"])         
def new_message(event_id):
    data={
        'user_id': session['user_id'],
        'event_id': event_id,
        'content' : request.form['content']
    }
    event.Event.create_event_message(data)
    return redirect(f"/event/{event_id}")

@app.route('/event/search')         
def search_for_events():
    if 'user_id' not in session: 
        flash('You must be logged in to view this page')
        return redirect('/')
    return render_template("search.html",  user = user.User.get_logged_in_user(), events=event.Event.get_all_events_with_creator_attendees())

@app.route('//event/<int:event_id>/join/<int:user_id>')         
def join_trip(event_id, user_id):
    data = {
        "user_id" : user_id,
        "event_id" : event_id
    }
    event.Event.join_event(data)
    return redirect ("/event/search")

@app.route('//event/<int:event_id>/unjoin/<int:user_id>')         
def unjoin_trip(event_id, user_id):
    data = {
        "user_id" : user_id,
        "event_id" : event_id
    }
    event.Event.unjoin_event(data)
    return redirect ("/event/search")
