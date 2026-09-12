from enum import Enum
import datetime


# Statistics will be displayed upon the dashoboard as a quick single-pane of glass summary of what is happening
# We will have our base list here as a reference for what we want to setup, pull in, and calculate later
stats = ["Total number of tasks",
  "percent in each status category",
  "Stopwatch since last update",
  "Timer until next update"
  "Number of consecutive days with(out) uploads",
  "Number of tasks uploaded today",
  "Number of tasks completed today",
  "Time until next task expiration date"
]

# Mood Chooser can be added in as a way to prioritize what needs doing. A user can have presets that affect which potential tasks are displayed
# We can have a punchcard like optional entry where someone enters numbers only in the fields that matter to them in the moment, and then it chooses a task to prioritize
moods = ["Healthy",
  "Tired",
  "Frustrated", 
  "Disappointed", 
  "Eager", 
  "Anxiety", 
  "Batteries", 
  "Curious", 
  "Sightedness", 
  "Floatiness"
]

# An epicChooser will similarly come into effect passively when other automatic fields can be taken into account
# Thoughts being to make it easier to choose tasks that are easier for some reason, including:
epicChooser = ["Time of Day",
  "Work Schedule",
  "Weekday",
  "Date",
  "Warming up",
  "Winding down"
]

# Optional lists to be defined at startup before sorting through others. These to be there mainly for speed, when we don't have too much time, but can do an easy win, or discover newly unlocked tasks
lists = ["Quick Ticks",
  "Tasks to be ground down",
  "Newly unlocked tasks that were prviously blocked"
]
# TODO: Criteria to generate each of the above list categories

# Epics will be representations of the categories that we split up tasks within
# Each can have their own backlog of tasks, as well as with Habits or Hobbies relating back to them
epics = {
  "name": "",
  "examples": [],
  "tagNum": 0
}

epicList = [
  ("Learning", ["Acquiring new skills", "Practicing old ones","Retrospecting"],0),
  ("Dreaming",["Project management", "Planning for the future", "Reminding yourself of your why"],1),
  ("Administrating", ["Signing documents","Going to appointments", "Weighing the options of decisions"],2),
  ("Careering", ["Making moves in your career path", "Getting work tasks done", "Networking with people"],3),
  ("Moonlighting", ["Getting side-projects done", "Respecting the hustle", "Hobbies and Habits"],4),
  ("Estating", ["Porkchop sandwiches", "Maintenance", "Chores"],5),
  ("Recharging", ["Following pleasurable pursuits", "Active Rest", "Hanging out with people"],6)
]

# TODO: deciding on epic object criteria, which really would be tasks, backlog, and dashboard structure


# Habits are intended for more Apollonian kinds of tasks, intending for activities that you would like to do every day, and possibly track the progress or gamify your status and/or routine
# Though, of course, you can customize this as you see fit!
habitNames = ["Piano Practices",
  "Workouts",
  "Reading",
  "Qi Gong"
  "Yoga",
  "Journaling",
  "Meditation",
  "Coding"
]
# TODO: deciding on habit object criteria, which really would be in comparison to tasks and hobbies

# Hobbies, on the other hand, are intended to be for more Dionysian tasks, things that don't happen everyday, but are lots of fun to get into, and one would prefer to log progress
hobbies = ["Cooking",
  "Restaurants",
  "Artistry",
  "Hackathons",
  "Authoring",
  "Composing"
]
# TODO: deciding on hobbies object criteria, which really would be in comparison to tasks and habits

# Old Friends are a way of keeping track of who you've spoken with, when, and are in an effort to keep in touch with. A game once told me that friendships are like plants, you have to water them.
oldFriends = {
  "name": "",
  "history": "",
  "address": "",
  "encounters": [
    {"what": "",
    "where": "",
    "when": "",
    "why": "",
    "whoelse": [""],
    "Followup": ""}
  ]
# TODO: friend dashboard to show who you haven't reached out to in a while
#       notifications to notify folks and send good vibes
}

# Friends in general can be a little different, there can be information about what needs to be understood here. Further, there are bonsai friends and cactus friends, some need lots of watering and attention, while others are fully happy doing their own thing and can be happy to see you, even better perhaps to not have had you there the whole time in between. What you're friends about can also be good to note
freindos = {
  "name": "",
  "meetCute": "",
  "friendsAbout": "", # What you find yourself being friends about
  "plant type": "",  # Bonsai, Seasonal, Cactus, Evergreen
  "whereYouLive": "",
  "contactPreference": "",
  "memeSubjects": ""
}

# Task Categories are to serve as all the fields of what a task would ideally be considering as data
# These will be stored elsewhere, but here the titles are to be used as category headers, databaseStyle
taskData = {
  "name": "",
  "description": "",
  "epic": {},
  "expirationDate": datetime,
  "stakes": "",
  "prerequisites": "",
  "relative Difficulty": {},
  "satisfaction": {},
  "status": {},
  "time and Date": datetime,
  "iD": 0
}

# Relative Difficulty is to be defined by the user, we'll have emoticons here as what I find amusing
# Feel free to change them into other aspects, changing the titles for each one here should dynamically affect the system
relativeDifficulty = {
  "icon": "",
  "description": "",
  "tagNum": 0
}

relDiffList = [
  (":-P","Stupid easy, no harder than sticking one's tongue out",0),
  (":-)","Easy to get done, can be done at most times",1),
  (":-|","Bartleby (Remember that laziness is the opponent)",2),
  (">:-/","Might need a little grit, furrow your brow!",3),
  ("B-0","Just start to sing, as you tackle the thing, that cannot be done, and you'll do it",4),
  ("8-@","That's a big boiiiii!!!!11 You're not getting this done in one go, but you can take a bite out of it",5),
  ("%-#","This should be broken up into parts, task is really a spike that needs further understanding",6)
]

# Satisfaction should also be up for the user to define, as we all get different levels from completion
# Rather than just feeling good, this category is more to define how many times one can reap rewards from the completed tasks
satisfaction = {
  "name": "",
  "description": "",
  "tagNum": 0
}

satisfactionList = [
("Once","Do the thing, and it's good for now",0),
("Countably finite","The task, once done, will give a few returns",1),
("Verrazano","The task is finite, but increments of its consumption are uncountable, as in you don't see the other side of the horizon when setting out upon it",2),
("Memory","The task keeps on giving whenever you remember it, or having done it",3),
("Rebounding","The everflowing chalice, a lotus with infinite petals",4)
]


# Status of a task is to be a criterion for seeing how far along we are with something, or if it is relative to something else, and what may be affected therewith
# Default values, like in other categories, are definitions, references, or inside jokes (with myself)
status = {
  "name": "",
  "description": "",
  "tagNum": 0
}

statusList = [
("Let's go!","This task can be picked up at any time",0),
("It's happening!","Task was started, but is not yet finished",1),
("Yah-Tah!","Yay! You did it!",2),
("Awating","Something else needs to happen first, see pre-reqs",3),
("Sedimentary","Needs breaking down into smaller parts",4),
( "Incomplete","Task is missing one or more of its classifiers",5),
( "Deprecated","Doesn't really need to be done anymore, we've got something better!",6)
]
