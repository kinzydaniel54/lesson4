import random

moods = ["happy", "sad", "tired", "excited", "angry", "relaxed"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


times = ["morning", "afternoon", "evening"]

for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day} {time} you were {mood}")