# IF YOU ARE LOOKING TO MAKE A NOODLE EXTENSIONS LEVEL
please whatever you do DO NOT USE THIS. This is *bad*. A few more notes before you leave though;
- This requires that you have some python experience.
- This is bad.
- If you have python experience, I heavily suggest you use [this](https://github.com/megamaz/python-noodleExtensions-demojs) instead. It is a copy of the demo.js in python, which is much better than this.
- If you'd rather use this, I have a few other things to say:
  - dont
  - If you *really* wanna use this, then I assume you have python experience. Enough to understand how the script works.
  - Since it's absolute trash, I will not be giving out any more support.
  - I will be finishing the [Wiki](https://github.com/megamaz/Python-Noodle-Extensions-Editor/wiki). However, if something does not make sense, do not count on me to help you with it.
  - Good luck.
# Python Noodle Extensions Editor (PNEE)
Current Version: 2.1.0\
Check your installed version by doing `pip show NoodleExtensions`. If you are not on 2.1.0, do `pip install --ugprade NoodleExtensions`.<br/>
<br/>

![PNEE](./assets/PNEE.png)
## my to-do list
If you want to know what's currently on my to-do list, you can go [here](https://trello.com/b/yA5qQTs7)! Pull requests, feedback, issues, and more are appreciated. If you'd like to contact me, you can do so on discord at `megamaz#1020`
## What is it?
This is a Python Noodle Extensions Editor for Beat Saber levels. Manually editing a JSON file over a long period of time can get really annoying, so this should speed up the process!\
### Links
- [Wiki](https://github.com/megamaz/Python-Noodle-Extensions-Editor/wiki)
- ~~Discord~~
## Sample
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"level.datpath")

# assign to a new track
dropNote = NE.Note(5, 1, 0, 0, 8)
editor.editNote(dropNote, NE.Note(5, 1, 0, 0, 8, _track="FallDownTrack"))

FallDownTrack = NE.AnimateTrack(2, "FallDownTrack", 2, _position=[
  [0, 100, 0, 0], # be in the sky before it appears
  [0, 0, 0, 0.75, "easeOutBounce"], # fall down in front of player and finish animation just in time for the player to hit it
])
editor.animateTrack(FallDownTrack)

# push events to the level.dat so it can be ready to play
editor.pushChanges()
```
# Pull Request
To make a pull request, please test your code either using [pytest](https://docs.pytest.org/en/stable/) or your python testing env. of your choice.\
I will not be accepting any form of pull request if the test files have not been modified to fit your modifications.
1. Fork this project
2. Edit code 
3. *Test* your code
4. If check 3 is done, move on to step 5
5. Make the pull request
## Current Issues:
- using editNote/editWall multiple times on the same notes/blocks will clear the current `_customData`

#### Currently testing features (checked features have been tested and are working)
* [X] updateDependencies
* [X] pushChanges
* [X] getNote
* [X] getWall
* [X] editNote
* [X] editWall
* [X] animateTrack
* [X] assignPathAnimation
* [X] assignTrackParent
* [X] assignPlayerToTrack
