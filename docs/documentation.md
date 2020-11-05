# Python Noodle Extensions Editor (PNEE)
if you're unsure on how to use this script, this should help you out. 

## Setting-Up
if you haven't already, download the NoodleExtensions.py from the [Latest Release](https://github.com/megamaz/NoodleExtensions-python/releases) and put it inside the same folder that will contain your code.\
To start using this script, very simply just `import NoodleExtensions` and you should be good to go!

# Usage
Quick Access (they are in order of which they must be completed.)
1. [Editor](#Editor)
1. [Animator](#Animator)
## Editor 
The editor is the key element to your script. It will be containing the actual level data. It's really simple to setup, here's an example in two lines;
```py
import NoodleExtensions
editor = NoodleExtensions.Editor("Your Level.dat Path")
```
It's really that simple. There's not much else to it. 

## Animator
The animator is what (you guessed it) will be taking care of all the animating. You NEED to have an [editor](#Editor) setup for the Animator to work. There is no skipping that step.\
Here is a quick example of setting up an Animator;
```py
import NoodleExtensions
editor = NoodleExtensions.Editor("Your Level.dat Path")

animator = NoodleExtensions.Animator(editor) # this is the line to set up an animator. Really, not that hard!
```
The animator can currently only animate tracks and path animations. `AssignPlayerToTrack` and `AssignTrackParent` are soon to come!\
It is recommended that any animation either start at 1-1.5 beats before the actual animation. This prevents the gif shown in [_position](#_position) from happening where the notes blips into position while it's moving towards the player. If that is your intended effect, than have at it.
Animation quick guide:
- [`_position`](#_position)
- [`_rotation`](#_rotation)
## _position
The position setting works like this: `[x, y, z, time, easing]`. Here's a reference to each;
- x : left/right
- y : up/down
- z : forw/backw
- time : the time in which the animation should happen, ranging from 0-1, start-end
- easing : How the block should move during the animation. Gained from NoodleExtensions.EASINGS or [easings.net](https://easings.net).
Here is the in-line usage;
```py
. . .
animator.Animate("AnimateTrack", NoodleExtensions.Animations.position, [
    [0, 10, 0, 0],
    [0, 0, 0, 1, "easeOutBounce"]
], "BounceTrack", 3, 4)
```
This above gives us this result;\
![Bounce](images/bounce.gif)\

## _rotation