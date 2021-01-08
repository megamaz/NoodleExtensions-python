# Python Noodle Extensions Editor (PNEE)
*pronounced /nē/ (Ni)*
```
PPPPPPPPPPPPPPPPP   NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
P::::::::::::::::P  N:::::::N       N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
P::::::PPPPPP:::::P N::::::::N      N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
PP:::::P     P:::::PN:::::::::N     N::::::NEE::::::EEEEEEEEE::::EEE::::::EEEEEEEEE::::E
  P::::P     P:::::PN::::::::::N    N::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
  P::::P     P:::::PN:::::::::::N   N::::::N  E:::::E               E:::::E             
  P::::PPPPPP:::::P N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   
  P:::::::::::::PP  N::::::N N::::N N::::::N  E:::::::::::::::E     E:::::::::::::::E   
  P::::PPPPPPPPP    N::::::N  N::::N:::::::N  E:::::::::::::::E     E:::::::::::::::E   
  P::::P            N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE   
  P::::P            N::::::N    N::::::::::N  E:::::E               E:::::E             
  P::::P            N::::::N     N:::::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
PP::::::PP          N::::::N      N::::::::NEE::::::EEEEEEEE:::::EEE::::::EEEEEEEE:::::E
P::::::::P          N::::::N       N:::::::NE::::::::::::::::::::EE::::::::::::::::::::E
P::::::::P          N::::::N        N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
PPPPPPPPPP          NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
```
## my to-do list
If you want to know what's currently on my to-do list, you can go [here](https://trello.com/b/yA5qQTs7)! Pull requests, feedback, issues, and more are appreciated. If you'd like to contact me, you can do so on discord at `megamaz#1020`
## What is it?
This is a Python Noodle Extensions Editor for Beat Saber levels. Manually editing a JSON file over a long period of time can get really annoying, so this should speed up the process!

## How do I use it?
The docs can be found [Here!](https://github.com/megamaz/NoodleExtensions-python/blob/master/docs/documentation.md)\
As of installation, you can simply `pip install NoodleExtensions` and you'll be ready to `import noodle_extensions` inside your project.\
No credits are required! Suprisingly a few people have asked me about that. this is just meant to be helpful and if you'd like to give credit that's fine.

## Extra notes:
- Made entirely in python
- Pull requests are appreciated, but follow the [pull requests](#pull-request) steps
# Samples

## Simple (blank) animation
```py
from noodle_extensions import Editor, Animator
from noodle_extensions.constants import EventType, Animations

editor = Editor("YourLevel.datPath")
animator = Animator(editor)

# Animations can go here.
# Basic position animation (that does nothing)
animator.animate(EventType().AnimateTrack, Animations().position, [[0, 0]], "DummyTrack", 0, 3)
```
# Pull Request
To make a pull request, please test your code either using [pytest](https://docs.pytest.org/en/stable/) or your python testing env. of your choice.\
I will not be accepting any form of pull request if the test files have not been modified to fit your modifications.
1. Fork this project
2. Edit code 
3. *Test* your code
4. If check 3 is done, move on to step 5
5. Make the pull request
  a. Give it a meaningful title. 
  b. Give it a meaningful description.
  c. I'll review it when I have time. I'm a busy man
## Current Issues:
None (Contact me at `megamaz#1020` if you run into any issues)
#### Currently testing features (checked features have been tested and are working)
* [ ] Editor.updateDependencies
* [X] Editor.editBlock
* [X] Editor.editWall
* [X] Editor.getBlock
* [X] Editor.getWall
* [X] Editor.removeEvent
* [X] Animator.animate
* [X] Animator.animateBlock
* [X] Animator.animateWall
* [X] Animator.editTrack
