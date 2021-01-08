# Python Noodle Extensions Editor (PNEE)
if you're unsure on how to use this script, this should help you out. 

## Setting Up
To start using this script, open up a CMD and type in `pip install NoodleExtensions`. Once that's done, open up your python project in 3.9.0 (or above) and `import noodle_extensions`\
Also see:
- [Setting up pip](https://pip.pypa.io/en/stable/installing/)
# Usage
Quick Access
1. [Formats](#Animation-Formats)
1. [Editor](#Editor)
1. [Animator](#Animator)
# Animation Formats
Before you start anything, this will be your needed formats for animating. Refer to those if you can't remember!
- _position         `[x, y, z, time, "easing"]`
- _rotation         `[pitch, yaw, roll, time, "easing"]`
- _localRotation    `[pitch, yaw, roll, time, "easing"]`
- _scale            `[left/right, up/down, forw/backw, time, "easing"]`
- _dissolve         `[amount, time, "easing"]`
- _dissolveArrow    `[amount, time, "easing"]`
- _time             `[lifespan, time, "easing"]`
- _color            `[red, green, blue, time, "easing"]`
<!--END LIST-->
For better understanding of what each unit means, here's a quick guide;
- `_position` and `_scale` uses Unity X/Y/Z coordinates. X is left/right, Y is up/down, and Z is forwards/backwards. 1 unit is equivalent to 1 left/right position on the grid.
- `_rotation` and `_localRotation` make use of Pitch/Yaw/Roll. Refer to [this image](https://www.google.com/search?q=pitch+yaw+roll&safe=strict&rlz=1C1ASUM_enUS917US917&sxsrf=ALeKk03Vg15s8ruurcCtYVepnsvPtIHugA:1609307074255&tbm=isch&source=iu&ictx=1&fir=kcvIcJ6UoVZneM%252CrwdN0Ut4Lf6FUM%252C_&vet=1&usg=AI4_-kRHTAmavXFfU6li52HkQ40nTw-JwA&sa=X&ved=2ahUKEwiT7vqDgPXtAhVhMX0KHapWD3wQ_h16BAgnEAE#imgrc=kcvIcJ6UoVZneM) to better understand what they mean.
<!--END LIST-->
Some of them use numbers that are used differently than you'd expect. Those are as follows;
- `_rotation` makes use of world axis for rotation (the position in between the feet).
- `_dissolve` and `_dissolveArrow` make use of a 0-1 float, where 0 means fully visible and 1 means invisible.
- `_time` makes use of the note's lifespan, being a 0-1 float. 0 meaning the moment where the note spawns in (with the bright flash), and 1 being the moment where the player would miss the note if they failed to hit.
- `_color` uses an RGB system. To pick the right color, refer to a [color picker](https://www.rapidtables.com/web/color/RGB_Color.html). **BE SURE TO DIVIDE THE VALUE BY 255. `_color` MAKES USE OF 0-1 AND NOT 0-255**
# Editor 
The editor is the key element to your script. It will be containing the actual level data. It's really simple to setup, here's an example in two lines;
```py
from noodle_extensions import Editor

# remember, when putting a path to a string to include an "r" behind the quotation marks! this prevent backslash bugs.
editor = Editor(r"Your Level.dat Path")
```
Editor Function Quick Access:
- [`updateDependencies`](#updateDependencies)
- [`editBlock`](#editBlock)
- [`editWall`](#editWall)
- [`getBlock`](#getBlock)
- [`getWall`](#undocumented)
- [`removeEvent`](#removeEvent)
### Parameters
- `file` the path to your level.dat file. 
To actually use the `editor` object you created, there's a few things you can do;
## updateDependencies
Update dependencies allows you to add requirements to your level.
```py
from noodle_extensions import Editor

editor = Editor(r"Your Level.dat path")

editor.updateDependencies("Noodle Extensions")
```
The result of running the line above would add `Noodle Extensions` as a requirement to the specified level.
### Parameters
- `dependency` The requirement to add to the level.
## editBlock
The edit block allows you to change the block's `_customData` property.\
For the inline usage, you need to tell it the beat of the block and it's position relative to the bottom left corner of the 3x4 grid. 
```py
from noodle_extensions import Editor

editor = Editor(r"Your level.dat path")

editor.editBlock(beat=6, pos=(1, 0), track="ExampleTrack", fake=True, interactable=False)
# editBlock(beat, (posx, posy), "track", fake, interactable)
```
The code above grabbed a block on beat 6 who is in the bottom middle left of the 3x4 grid, (color / direction doesn't matter), gave it the `ExampleTrack` track, made it a False block that cannot be interacted with. 
### Parameters
- `beat` the beat at which the note can be found.
- `pos` an (x, y) tuple of the note's position, where X is left-most (0), and Y is bottom-most (0)
- `track` the track you want to give the note.
- `fake` if the note will affect score, health etc...
- `interactable` if the note can be hit with the sabers.
<!--END LIST-->
When using `fake` and `interactable`, remember that if the note cannot be hit but will affect score and health, that's just evil and is not allowed by the script. 
## editWall
This is the same as EditBlock, except it's for a wall. It changes the `_customData` property of the wall
```py
from noodle_extensions import Editor

editor = Editor(r"Your level.dat path")

editor.editWall(beat=6, length=6, index=3, track="ExampleTrack", fake=False, interactable=True)
# editWall(beat, length, index, "track", fake, interactable)
```
The code above edited the wall to being a normal wall, just included the the `ExampleTrack` to it. The wall is set to be real and interactable.
### Parameters
- `beat` The beat at which the wall will start.
- `length` The beat at which the wall ends, substracted by the beat at which it starts.
- `track` the track to give the wall.
- `fake` whether or not the wall will affect the player's life.
- `interactable` whether or not the wall will vibrate the controllers.
## getBlock
This returns a block's `json` data.
```py
from noodle_extensions import Editor

editor = Editor(r"Your level.dat path")

note = editor.getBlock(beat=5, pos=(1, 0))

print(note)
```
OUTPUT:
```
{
    "_time": 5,
    "_lineIndex": 1,
    "_lineLayer": 0,
    "_type": 1,
    "_cutDirection": 1,
    "_customData": {
        "_track":"ExampleTrack",
        "_fake":False,
        "_interactable":True
    }
}
```
Do note that changing the variable `getBlock` was set to will NOT change the file. 
### Parameters
or, if the note doesn't exist, you will get an error.
- `beat` The beat at which the note can be found
- `pos` a tuple of the note's position (X, Y) where X is left-most 0 and Y is bottom-most 0
<!--END LIST-->
This returns a note's full data.
## getWall
This returns a wall's `json` data.
```py
from noodle_extensions import Editor

editor = Editor(r"Your Level.dat path")

wall = editor.getWall(10, 1, 3)
# this will return a wall on beat 10, middle left, who is 3 beats long.
```
OUTPUT:
```
{
    "_time": 10,
    "_lineIndex": 1,
    "_type": 0,
    "_duration": 10,
    "_width": 1,
    "_customData": {
        "_track":"ExampleTrack",
        "_fake":false,
        "_interactable":true
    }
}
```
### Parameters
- `beat` The beat at which the wall starts.
- ``
## removeEvent
To remove an event / property of an event. This is so that you can change it. `Animator.animate` does overwrite, but if you want to remove instead just do this.\
Sample usage;
```py
from noodle_extensions import Editor
from noodle_extensions import Animations

editor = Editor(r"Your level.dat path")

editor.removeEvent(beat=5, EventType="AnimateTrack", track="ExampleTrack", animationType=Animations().position)
# By example, this line right here would take an event a beat 5 who animates ExampleTrack and remove it's _position property.
```
There is no `editEvent`, mainly because there's too many ways you could change a single event - if you want to change a single instance of an event, you can overwrite that instance using `Animator.animate`
### Parameters
- `beat` the beat at which the event happens.
- `eventType` The event type that will be edited.
- `track` the track that will be edited. 
- `animationType` that property that will be removed. (leave blank to remove the entirety of the event.)
# Animator
The animator is what (you guessed it) will be taking care of all the animating. You NEED to have an [editor](#Editor) setup for the Animator to work. There is no skipping that step.\
Here is a quick example of setting up an Animator;
```py
from noodle_extensions import Editor, Animator

editor = Editor(r"Your Level.dat Path")

animator = Animator(editor) # this is the line to set up an animator. Really, not that hard!
```
The animator can currently only animate tracks and path animations.\
It is recommended that any animation either start at 1-1.5 beats before the actual animation. This prevents the gif shown in [_position](#_position) from happening where the notes blips into position while it's moving towards the player. If that is your intended effect, then have at it.\
Animator Functions Quick Acess
- [`animate`](#animate)
- [`animateBlock`](#animateBlock)
- [`animateWall`](#animateWall)
- [`editTrack`](#editTrack)
### Parameters
- `editor` The editor object you created earlier in the script. 
## animate

```py
from noodle_extensions import Editor, Animator
from noodle_extensions.constants import Animations, EventType # this is just for those who have autofill.

editor = Editor(r"Your Level.dat Path")
animator = Animator(editor)

animator.animate(eventType=EventType().AnimateTrack, animationType=Animations().position, data=[
    [0, 10, 0, 0],
    [0, 0, 0, 1, "easeOutBounce"]
], track="BounceTrack", start=3, end=4)
```
### Parameters
`animator.animate` might seem a bit scary due to the provided example.\
The given settings are in the following order;
- `type` The animation type. This is why you imported `EventType`; that's to simply do `EventType().AnimateTrack` (with the parentheses) and get the `AnimateTrack` animation type.
- `animationType` the animation property. This is why you imported `Animations`; that's to simply do `Animations().position` (with the parentheses) and get the `position` animation property.
- `data` This one might seem a bit scary. but this is where you can refer to the [Animation Formats](#Animation-Formats) to help -
    You'll bee feeding into it a list. As example, the format for `_position` is `[left/right, up/down, forw,backw, time, "easing"]`. The first three items are units (1 unit is equivalent to one editor square) in which direction it should be moving. `time` is a sort of percent (0-1 float) of when it should happen from the given start time to the given end time. (so if the start time is beat 4, and the end time is beat 6, the `time` value is set to 0.5, the animation will happen on beat 5 (0.5*4+6, or `time*(startBeat+endBeat)`)). The `easing` value can be gained from [easings.net](https://easings.net) and is how fast the note will move. (if the shown graph goes up and down, the note will move up and down to the position accordingly.)
- `track` The track that will be animated.
- `start` When the animation will start.
- `end` When the animation will end.

## animateBlock
```py
from noodle_extensions import Editor, Animator
from noodle_extensions.constants import Animations, EventType # this is just for those who have autofill.

editor = Editor(r"Your Level.dat Path")
animator = Animator(editor)

animator.animateBlock(beat=6, pos=(1, 0), animationType=Animations().position, data=[
    [0, 0, 0, 0]
]) 
# keep in mind this example animation will cause the block to act as normal.
```
Very simply, `animateBlock` animates a specific property of a block. 
### Parameters
- `beat` The beat at which the note can be found.
- `pos` the position of the note (x, y) where x is left most, starting at 0 and y is bottom, starting at 0.
- `animationType` an animatable property (`Animations().property`)
- `data` a data list of the needed data to animate the block. For proper data usage, refer to [formats](#Animation-Formats)

## animateWall
```py
from noodle_extensions import Editor, Animator
from noodle_extensions.constants import Animations

editor = Editor(r"Your Level.dat Path")
animator = Animator(editor)

animate.animateWall(beat=5, length=2, index=1, animationType=Animations().position, data=[
    [0, 0, 0, 0]
])
# keep in mind this example animation will cause the wall to act as normal.
```
Very simply, `animateWall` animates a specific property of a wall.
### Parameters
- `beat` The beat at which the wall starts.
- `length` the length of the wall, or, the amount of beats difference between start of wall to end of wall.
- `index` the X position of the wall (0 is left most.)
- `animationType` the property of the wall that will be animated.
- `data` The data that will be used to animate the wall. For proper data usage, refer to [formats](#animation-formats).
## editTrack
This allows you to use AssignTrackParent and AssignPlayerToTrack
```py
from noodle_extensions import Editor, Animator
from noodle_extensions.constants import EventType, Animations

editor = Editor(r"Your level.dat path")
animator = Animator(editor)

animator.editTrack(eventType=EventType().AssignTrackParent, beat=5, tracks="ExampleTrack1 ExampleTrack2", "ParentTrack")

# [tracks] can either be a space-seperated list of tracks or a direct list of tracks (example below)
animator.editTrack(eventType=EventType().AssignTrackParent, beat=5, tracks=["ExampleTrack1", "ExampleTrack2"], parentTrack="ParentTrack")
```
### Parameters
- `eventType` Eitehr `AssignTrackParent` or `AssignPlayerToTrack`. Anything else is not supported with edit track. If you're looking to change a track's data, use [removeTrack](#removeTrack)
- `beat` The beat at which it should happen.
- `tracks` Either a list or a space-seperated list of tracks. These tracks will be assigned to a parent track, which is defined by `parentTrack`
- `parentTrack` the track to which the `tracks` should be assigned to as parent.
<!-- END LIST -->
`AssignTrackParent` Will mean that if the parented track is animated in transform way (`_scale`, `_position`, and `_rotation` (NOT `_localRotation`)) then the children tracks will be affected in the same way relative to their own positions.
## undocumented
Well this is a bit awkward. You were trying to get to a link that was supposed to directly help you with... whatever. Instead, it seems this bit hasn't been documented yet. That's very sad.
### Currently undocumented;
All is documented! yay!
<!--END LIST-->
I am working hard on getting this all documented AND working. Keep in mind if you have any form of feedback, you can contact me on discord at `megamaz#1020`