# Python Noodle Extensions Editor (PNEE)
if you're unsure on how to use this script, this should help you out. 

## Setting Up
if you haven't already, download the NoodleExtensions.py from the [Latest Release](https://github.com/megamaz/NoodleExtensions-python/releases) and put it inside the same folder that will contain your code.\
To start using this script, very simply just `import NoodleExtensions` and you should be good to go!

# Usage
Quick Access (they are in order of which they must be completed.)
1. [Editor](#Editor)
1. [Animator](#Animator)
# Editor 
The editor is the key element to your script. It will be containing the actual level data. It's really simple to setup, here's an example in two lines;
```py
from noodle_extensions import Editor
editor = Editor("Your Level.dat Path")
```
It's really that simple. There's not much else to it.\
To actually use the `editor` object you created, there's a few things you can do;
## EditBlock
The edit block allows you to change the block's `_customData` property. It currently only supports `_track`, `_fake`, and `_interactable`.\
For the inline usage, you need to tell it the beat of the block and it's position relative to the bottom left corner of the 3x4 grid. 
```py
editor.EditBlock(6, (1, 0), "ExampleTrack", True, False)
```
The code above grabbed a block on beat 6 who is in the bottom middle left of the 3x4 grid, (color / direction doesn't matter), gave it the `ExampleTrack` track, made it a False block that cannot be interacted with. 
## EditWall
This is the same as EditBlock, except it's for a wall. It changes the `_customData` property of the wall, and curently only support `_track`, `_fake`, and `_interactable`.
```py
edit.EditWall(6, 6, 3, "ExampleTrack", False, True)
```
The code above edited the wall to being a normal wall, just included the the `ExampleTrack` to it. The wall is set to be real and interactable.
## removeEvent
To remove an event / property of an event. This is so that you can change it. `Animator.animate` does overwrite, but if you want to remove instead just do this.\
Sample usage;
```py
# noodle extensions import setup
. . .
editor.removeEvent(5, "AnimateTrack", "ExampleTrack", "_position")
# By example, this line right here would take an event a beat 5 who animates ExampleTrack and remove it's _position property.
```
# Animator
The animator is what (you guessed it) will be taking care of all the animating. You NEED to have an [editor](#Editor) setup for the Animator to work. There is no skipping that step.\
Here is a quick example of setting up an Animator;
```py
from noodle_extensions import Editor, Animator
editor = Editor("Your Level.dat Path")

animator = Animator(editor) # this is the line to set up an animator. Really, not that hard!
```
The animator can currently only animate tracks and path animations. `AssignPlayerToTrack` and `AssignTrackParent` are soon to come!\
It is recommended that any animation either start at 1-1.5 beats before the actual animation. This prevents the gif shown in [_position](#_position) from happening where the notes blips into position while it's moving towards the player. If that is your intended effect, then have at it.\
## Example
[Example Script](https://github.com/megamaz/NoodleExtensions-python/blob/master/examples/1_POSITION.py)\
The position setting works like this: `[x, y, z, time, easing]`. Here's a reference to each;
- x : left/right
- y : up/down
- z : forw/backw
- time : the time in which the animation should happen, ranging from 0-1, start-end
- easing : How the block should move during the animation. Gained from NoodleExtensions.EASINGS or [easings.net](https://easings.net).
Here is the in-line usage;
```py
from noodle_extensions import Editor, Animator, Animations
. . .
animator.Animate("AnimateTrack", Animations.position, [
    [0, 10, 0, 0],
    [0, 0, 0, 1, "easeOutBounce"]
], "BounceTrack", 3, 4)
```
This above gives us this result;\
![Bounce](images/bounce.gif)\

## Animation Formats
To animate everything, you're gonna need to do what you did above; provide the animation type then a list. The list is the animation type's format, or how the list is supposed to look. Here's how they're supposed to look\ 
- _position         `[left/right, up/down, forw/backw, time (beat), "easing"]`
- _rotation         `[pitch, yaw, roll, time (beat), "easing"]`
- _localRotation    `[pitch, yaw, roll, time (beat), "easing"]`
- _scale            `[left/right, up/down, forw/backw, time (beat), "easing"]`
- _dissolve         `[amount, time (beat), "easing"]`
- _dissolveArrow    `[amount, time (beat), "easing"]`
- _time             `[lifespan, time (beat), "easing"]`
- _color            `[red, green, blue, time, easing`