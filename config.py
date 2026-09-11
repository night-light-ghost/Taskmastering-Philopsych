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
epics = ["Learning",
  "Dreaming",
  "Administrating",
  "Careering",
  "Moonlighting",
  "Estating",
  "Recharging"
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
    "what": "",
    "where": "",
    "when": "",
    "why": "",
    "whoelse": [""],
    "Followup": ""
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
taskData = [
  "Name",
  "Description",
  "Epic",
  "Expiration Date",
  "Stakes",
  "Prerequisites",
  "Relative Difficulty",
  "Satisfaction",
  "Status",
  "Time and Date",
  "ID"
]

# Relative Difficulty is to be defined by the user, we'll have emoticons here as what I find amusing
# Feel free to change them into other aspects, changing the titles for each one here should dynamically affect the system
relativeDifficulty = [":-P",
  ":-)",
  ":-|",
  ">:-/",
  "B-0",
  "8-@",
  "%-#"
]

# Satisfaction should also be up for the user to define, as we all get different levels from completion
# Rather than just feeling good, this category is more to define how many times one can reap rewards from the completed tasks
satisfaction = ["Once",
  "Countably Finite",
  "Verrazano",
  "Memory",
  "Rebounding"
]

# Status of a task is to be a criterion for seeing how far along we are with something, or if it is relative to something else, and what may be affected therewith
# Default values, like in other categories, are definitions, references, or inside jokes (with myself)
status = ["Let's go!",
  "It's happening!",
  "Yah-Tah!",
  "Awating",
  "Sedimentary",
  "Incomplete",
  "Deprecated"
]

