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
import NoodleExtensions
editor = NoodleExtensions.Editor("Your Level.dat Path")
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
## EditEvent
This one is to either Change, remove, or overwrite an event with a new one.\
To remove an event, simply do this;
```py
editor.EditEvent(6, "_eventExample", "ExampleTrack", editor.remove)
```
if doing anything else, there is a `newData` setting which will be a dictionary of the `_data` object that will be inside the `_customEvent` item.
# Animator
The animator is what (you guessed it) will be taking care of all the animating. You NEED to have an [editor](#Editor) setup for the Animator to work. There is no skipping that step.\
Here is a quick example of setting up an Animator;
```py
import NoodleExtensions
editor = NoodleExtensions.Editor("Your Level.dat Path")

animator = NoodleExtensions.Animator(editor) # this is the line to set up an animator. Really, not that hard!
```
The animator can currently only animate tracks and path animations. `AssignPlayerToTrack` and `AssignTrackParent` are soon to come!\
It is recommended that any animation either start at 1-1.5 beats before the actual animation. This prevents the gif shown in [_position](#_position) from happening where the notes blips into position while it's moving towards the player. If that is your intended effect, then have at it.\
Animation quick guide:
- [`_position`](#_position)
- [`_rotation`](#_rotation-and-_localrotation)
## _position
[Example Script](https://github.com/megamaz/NoodleExtensions-python/blob/master/examples/1_POSITION.py)\
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
![Bounce](images/bounce.gif)

## _rotation and _localRotation
[Example Script](https://github.com/megamaz/NoodleExtensions-python/tree/master/examples/2_ROTATION.py)\
The rotation and localRotation both use the same settings: `[pitch, yaw, roll, time, easing]` (you can think of the rotation as a stick going through the block, and the block rotating from that stick)
- pitch : left / right
- yaw : top/down
- roll : front/back
- time : the time in which the animation should happen, ranging from 0-1, start-end
- easing : How the block should move during the animation. Gained from NoodleExtensions.EASINGS or [easings.net](https://easings.net).
Inline usage looks like this;
```py
. . .
animator.Animate("AnimateTrack", NoodleExtensions.Animations.rotation, [
    [0, 0, 0, 0],
    [0, 0, 180, 1, "easeInOutBack"]
], "RotationTrack", 5, 6)
```
The code above then gives us this result:\
![Rotate](images/rotate.gif)\
The main difference between `_rotation` and `_localRotation` is the fact that `_rotation` will rotate from the World position (in between the feet on the ground) whilst `_localRotation` will be rotating from the block's position. (If you're animating a track, the blocks will not be rotated from their average position but from their own)