# Musings

I'd want to be able to come back to tasks here.
Like a set running backlog, with the ability to get upcoming tasks into the most minimal steps
think like "re-rolling item stats" that you can just hop in and do

# Dashboard

A dashboard that lists out the current backlog.


We want a site to view the current task lists. While a live site would be awesome, we can start with a compiled and generated site active when turned on. There should a few general counts: numbers of tasks created, percent in each status category (which can possibly link to said list of tasks), stopwatch since last update, timer until next update, number of consecutive days without uploads, number of tasks uploaded today, number of consecutive days with uploads, numer of tasks completed today, and time until next task expiration date. 

Before we get to lists, we can have a mood or epic chooser. I'm thinking I can have a current mood modifier that reflects how capable I'm feeling in the moment. It could include things like relative healthiness, tiredness, frustrations, disappointment, eagerness, anxieties, batteries, closure, sightedness, and floatiness. Maybe weighing them out on a scale, determining if there are any tasks listed that should be prioritised. Secondly, an epic chooser can passively include things like reflecting time of day, work schedule, weekday (sunday scaries), date, and time (warming up and winding down). Actively we can change it according to what we'd want accomplished in the moment. Toggling options such as where we are, vacation vs workday (weekends count as vacation).

Below the general count, which serves as an overall summary, we can have a set of lists. Each list should have a default loadout of fields displayed, with an option of displaying more, or removing some, potentially live and updatable. Also, each list, its options, and header menu should be about a screen size. We can start by having that be automatically 1080p, and then later adjusting to scale

Summary:

* No active tasks - "Fast Track" (Quick Ticks?)
  * I could have it not list any particular tasks as "active"
  * Maybe default prioritization is the fastest/smallest tasks available
  * Or, alternatively, have a "tasks grinding" section to make smaller, and more divisible tasks
* Epic level divisions
  * How about Learning, Dreaming, Administrating, Careering, Moonlighting, Estating, Recharging
  * Each one can have their own backlog 
* Habits and Hobbies track differently
  * Habits can be Apollonian, while Hobbies can be Dionysian
  * Would want to record consistency in terms of Habits
    * Piano practices
    * Workouts
    * Reading
    * Qi Gong
    * Yoga
    * Art!
  * Would want to record curios in terms of Hobbies
    * What cooking steps worked really well
    * Which restaurants slapped the hardest
    * What's created in your artistry
* Old Friends - more of a jounal
  * Entries for last time you saw somebody
    * What we got up to
    * Where we met
    * When it happened
    * If there's something to follow up with them about
  * Dashboard can say who's been falling behind
    * That you haven't reached to in a while
    * Notifications to notify folks and send good vibes
  * Friend entry definitions
    * Where they live
    * Preferred messaging service
    * Things in common (memables)

## General counts

There can be a customizable config in terms of categorical names, or set habits that folks would want to maintain.

## Mood and Epic chooser

## Lists

Below is to be a sections of lists, hitherto describing their purposes and what to be found there

### Quick Ticks

These tasks are to be picked up idly, as things that can be one to build up confidence. Some call them "Easy Wins" or "Reference wins".

**Criteria:**

* Only tasks in first two Relative difficulty categories
* Optional chores toggleable, showing dependent on where you are in the pointillist estate
* These could be sorted according to a prioritization:
  * Stakes (if and only if exclamation points were added)
  * Satisfaction value (Highest to lowest)
  * Name (Alphabetically)
  * Pre-reqs (specifically lack thereof)
  * Status (already in progress, then let's go)
  * Expiration Date

### Backlogs of each epic

### Habits and Hobbies

### Old Friends

### Vacations

# Tasking

## Tasks you already wanna get onto

* bookmarks and dotfiles managed in github

## first-tasks.csv

**Tasks format:**
Following a structure that would hopefully be able to be translated easily into a database table we have the following to start:

| Name | Description | Epic | Expiration date | Stakes | Prerequisites | Relative difficulty | Satisfaction | Status | Time and Date \[0\] | ID \[1\] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| De-rusting machete | Grind off the rust from machete so you can oil it up | Estating | EoD March 19th 2026 | Apologizing to Nicole for not having gotten around to it yet | [1] Ferreteria Aceite | :-) | Verrazano | let's go |
| Ferreteria Aceite | Ask about oils in the hardware store to prevent machete rust | Estating | None | Always having to deal with rusty machetes | Bike Check | :-) | once | yah-TAH |

\[0\] Time and Date will be added automagically by python code during task entry
\[1\] Later something like "id" may be added as well, automagically when uploading to a database 
\[2\] Note that the pre-reqs used the name of the other task


Breakdown of terms:

* Name
  * The name of the task
  * Should be kept short
    * Minimum length could be one word
    * Maximum length could be "Verbing the Adjective Noun"
* Description
  * This based off of agile methodologies "As a user, I should be able to \_\_\_\_\_"
  * Should give a general idea of what is to be done
* Epic
  * A present-tense verb, like the kind that could be a gerund
  * Current list including, but not limited to: 
    * Learning
      * Examples: { Acquiring new skills, Practicing old ones, and Retrospecting }
    * Dreaming
      * Examples: { Project management, Planning for the future, Reminding yourself of your why }
    * Administrating
      * Examples: { Signing documents, Going to appointments, Weighing the options of decisions }
    * Careering
      * Examples: { Making moves in your career path, Getting work tasks done, Networking with people }
    * Moonlighting
      * Examples: { Getting side-projects done, respecting the hustle, Hobbies and Habits }
    * Estating
      * Examples: { Porkchop sandwiches, Maintenance, Chores }
    * Recharging
      * Examples: { Following pleasurable pursuits, Active Rest, Hanging out with people }
* Expiration Date
  * When you should have it done by (within context/reason)
  * 24h:Time on Month Day(th), year
* Stakes
  * How important the task is, represented by two things:
    * Firstly an amount of exclamation points, if applicable !!!
    * Then what you'll need to do if the task expires
* Pre-requirements (pre-reqs for short)
  * If a task is dependent upon another task, then it should be listed here by name
  * If there are No pre-requirements (a.k.a. is labeled as None), then this could be used to sort
* Relative Difficulty
  * Here I should probably use T-Shirt sizes, but I made up my own scale of emoticons:
    * :-P <-- Stupid easy, no harder than sticking one's tongue out
    * :-) <-- Easy to get done, can be done at most times
    * :-| <-- Bartleby (Remember that laziness is the opponent)
    * >:-\ <-- Might need a little grit, furrow your brow!
    * B-O <-- Just start to sing, as you tackle the thing, that cannot be done, and you'll do it
    * 8-@ <-- That's a big boiiiii!!!!11 You're not getting this done in one go, but you can take a bite out of it
    * %-# <-- This should be broken up into parts, task is really a spike that needs further understanding
* Satisfaction
  * This is how much you'll be getting out of the task
  * What's important here is to highlight if it is a one-and-done, or if it will rebound
  * So far we have the following options:
    * Once <-- Do the thing, and it's good for now 
      * This usually meant for short term gains
      * Really, fewer time spent on these will maximize output
      * Examples include, but are not limited to: { Making a single serving of food, administrative tasks like signing documents, repeated chores like dishes, laundry, and trash }
    * Countably Finite <-- The task, once done, will give a few returns
      * This can be things you need to do, as well as things you like to do, and things that once done, last a little while
      * Thinking like a (RH)multiplier, these are linear rather than constants, and usually give more than their initial task took out of you
      * Examples include, but are not limited to: { Getting a new 5 gallon water jug, Cooking a large amount of food, Getting Groceries }
    * Verrazano <-- The task is finite, but increments of its consumption are uncountable, as in you don't see the other side of the horizon when setting out upon it
      * These usually give more than they take from you, and for a longer amount of time
      * Honestly, one can practice trying to see the long game here, to determine the incrementations or causes and effects of otherwise invisible or intangible concepts
      * Examples include, but are not limited to: { Getting large quantity items like supplements, spices, or toiletries, Buying new reusable products like clothes or sheets, Learning a life-hack }
    * Memory <-- The task keeps on giving whenever you remember it, or having done it
      * This can fall into one of the last two categories, but is noticed for staying with you
      * These are awesome, and can probably just be remembered after the fact, as a kind of "gratitude of memory meditation"
      * Examples include, but are not limited to: { Reading (or listening to) a book, Sharing a nice experience with somebody, Being entertained by art }
    * Rebounding <-- The everflowing chalice, a lotus with infinite petals
      * These go beyond. Ram Dass in "Be Here Now" described not leaving your treasures in time or Samsara, for time ruins all things.
      * Examples include, but are not limited to: { Teaching something to someone else, Terraforming, Logging your habits and looking back on your accomplishments }
* Status
  * This should be a simple one-word description of where the task is, or what it needs
  * We can sort tasks with this, though honestly, it could also definitely separate them into various tables
  * Current values include, but are not limited to:
    * let's go <-- This task can be picked up at any time
    * happening <-- Task was started, but is not yet finished
    * Yah-TAH <-- Yay! You did it!
    * awaiting <-- Something else needs to happen first, see pre-reqs
    * sedimentary <-- Needs breaking down into smaller parts
    * incomplete <-- Task is missing one or more of its classifiers
    * deprecated <-- Doesn't really need to be done anymore, we've got something better!
* Time and Date
  * Autogenerated by python code at time of task entry
  * This could be used for sorting purposes, as well as notifications
* ID
  * This will be more for machine purposes than human ones
  * Right now all I can think of is for notifications of the system (i.e. powers of ten tasks)

# Python coding to do

## Uploader

This will be the code that uploads the current task list into a database, flushing out the list's contents. Ideally this could be set off, though would also happen automatically at end of day. A summary of what tasks are added could be sent to me, even and especially if it was empty. If empty for several days, a count of how many days should be listed. Also this could add an id field for tasks when adding them to the database.

## Single task entry

This will be code that adds a single task to the list. I would like to have at least two ways to do it, both on the command line through a single term at a time interface, and eventually online, by email. Both ways should allow for the option to leave a section blank. The CLI method should display a summary before appending it to the current file, with an extra warning if there is improper formatting or a missing section. Time and date of entry can be generated and added.

## Batch task entry

This code should take a text file, an email, or maybe a text (dreams!) and parse through it, adding all mentioned tasks into the current list, or online database. If done from a text file on the command line, a similar summary as for CLI method should be done. For the case of email or text, it can go straight to the online database, however a confirmation email or text reply should be sent with the summary, even though no changes can be directly made. When adding to the database, an ID field can be added.

## Task editor

I don't think a command line task editor will be needed. We can just edit csv files with vim or basic code. For live editing though, see Dashboard section.

## Data trends

More just listing an unknown here, but expressing a desire. Not fully sure what I'll get from the data science book, but hoping that something comes up as a result of reading it that we can learn from analyzing the data trends


# Absent minded findings?

* Thoughts to journal around
* Personas to explore
  * Your "excited little boy" and how he can help
    * He stays awake and pays attention (all-nighters, vidja games, movies, sleepovers)
    * Get him interested in work tasks (or at least whatever the fuck worked this morning lol)
    * Does he have a name? What Andy Watson & Cole de Mole considered your excited puppy mind
  * Your "spooky side" and how she provides courage

