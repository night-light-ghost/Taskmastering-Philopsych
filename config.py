
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

# Dashboard needs defining of the following:
## General counts
## Mood and Epic chooser
## Lists (with described prposes and what is to be found there
## Quick Ticks
