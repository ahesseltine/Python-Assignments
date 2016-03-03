import json
import sqlite3
databaseconnection = sqlite3.connect('Roster_Assignment.sqlite')
databasecursor = databaseconnection.cursor()
databasecursor.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE);
CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
json_data = json.loads(open(raw_input('Enter file name: ')).read())
for varlist in json_data:
    name = varlist[0];
    title = varlist[1];    binary = varlist[2];
    databasecursor.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    databasecursor.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = databasecursor.fetchone()[0]
    databasecursor.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    databasecursor.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = databasecursor.fetchone()[0]
    databasecursor.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
         ( user_id, course_id, binary ) )
    databaseconnection.commit()