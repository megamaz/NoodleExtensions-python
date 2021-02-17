# PNEE Documentation
If you're having trouble understanding how to use the script, this should help you out!
# Installation
Before you start coding, you have to make sure that you have it installed.\
If it's already installed:
- `pip install --upgrade NoodleExtensions`
<!---->
If you do not have it installed;
- `pip install NoodleExtensions`
## Setup
To get started making Noodle Extension levels, you first must import it into your python file.
```py
import noodleExtensions as NE
```
It isn't *necessary* to include the `as NE`. It just makes it much simpler when coding.\
Once you've imported, it's time to create an editor.
```py

lvl = "path to your level.dat here"
editor = NE.NoodleExtensions(lvl)
```
Now your file should look like this;
```py
import noodleExtensions as NE

lvl = "path to your level.dat here"
editor = NE.NoodleExtensions(lvl)
```
## Custom Data Properties
Custom data properties can be set to [objects](#objects) and [events](#events).\
Event Properties
Property | Usage | animateTrack | assignPathAnimation | assignPlayerToTrack
--- | --- | --- | --- | ---
_position | `[x, y, z, 0-1(time), easing]` | ✅ | ✅ | ✅
_rotation | `[pitch, yaw, roll, 0-1(time), easing]` | ✅ | ✅ | ✅
_localRotation | `[pitch, yaw, roll, 0-1(time), easing]` | ✅ | ✅ | ✅
_scale | `[x, y, z, 0-1(time), easing]` | ✅ | ✅ | ❌
_color | Requires Chroma. `[R, G, B, 0-1(time), easing]` (RGB 0-1 scale) | ✅ | ✅ | ❌
_dissolve | `[amount, (0-1)time, easing]` | ✅ | ✅ | ❌
_dissolaveArrow | `[amount, (0-1)time, easing]` | ✅ | ✅ | ❌
_interactable | `[0/1, (0-1)time]` | ✅ | ✅ | ❌
_time | `[lifespan, (0-1)time, easing]` | ✅ | ✅ | ❌
_definitePosition | `[x, y, z, 0-1(time), easing]` | ❌ | ✅ | ❌
The crosses above are not due to this script's limitation but to Noodle Extensions built-in limitations. 
\
Object properties
Property | Usage | Note | Obstacle
--- | --- | --- | ---
_track | `"TrackName"` | ✅ | ✅
_animation | `{"property":[data]}` | ✅ | ✅
_fake | True/False | ✅ | ✅
_interactable | True/False | ✅ | ✅


# Objects
Objects are data containers. You will need to create a few to use this script.
- [`Note`](#note)
- [`Obstacle`](#obstacle)
### Note
A `Note` object which contains note data. The note does not have to exist inside the level.dat file. Custom data properties can be assigned normally.
```py
import noodleExtensions as NE

# just as we assign any other property on this note as property=value, you can assign custom value properties using proerty=value
NE.Note(beat=10, index=0, layer=0, type=0, cutDirection=0,
_track="ExampleTrack") # review Custom Data Properties 
```
this new `Note` object will have it's track set to `"ExampleTrack"`. If you wish to give it an individual path animation (animate it without giving it a track) Then do:
```py
import noodleExtensions as NE

# this animation will do nothing
NE.Note(beat=10, index=0, layer=0, type=0, cutDirection=0,
_animation={
    "_position":[
        [0, 0, 0, 0]
    ]
})
```
#### Arguments
- `beat` That beat at which the note can be found
- `index` The left/right position of the note. (0 if left-most)
- `layer` The heigt position of the note. (0 is bottom-most)
- `type` The type of the note. 0 = left, 1=right, 2=unused, 3=bomb.
- `cutDirection` The direction of the note. [45*value] where 8 is dot note.
- `**customData` any pieces of custom data.
### Obstacle
A `Obstacle` Object which contains wall data. The wall does not have to exist in the level.dat
```py
import noodleExtensions as NE

# just as we assign any other property on this wall as property=value, you can assign custom value properties using proerty=value
NE.Obstacle(beat=10, index=1, type=1, duration=2, width=2,
_track="ExampleTrack") # review Custom Data Properties
```
This new `Obstacle` object will have it's track set to `"ExampleTrack"`. If you wish to give it an individual path animation (animate it without giving it a track) then do:
```py
import noodleExtensions as NE

# this animation will do nothing
NE.Obstacle(beat=10, index=1, type=1, duration=2, width=2,
_animation={
    "_position":[
        [0, 0, 0, 0]
    ]
})
```
if you want to get an Obstacle that does exist in the level.dat
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"level.dat path")

w = NE.Obstacle(beat=10, index=1, type=1, duration=2, width=2)
walls = editor.getWall(w)
```
#### Arguments
- `beat` That beat at which the wall starts
- `index` The left side of the wall's left/right position.
- `width` How wide the wall is.
- `type` Wall type. 0=Crouch, 1=full height.
- `duration` How long the wall is (beats)
- `**customData` any pieces of custom data.
# Functions
- [`updateDependencies`](#updatedependencies)
- [`pushchanges`](#pushchanges)
- [`getnote`](#getnote)
- [`getwall`](#getwall)
- [`editnote`](#editnote)
- [`editwall`](#editwall)
- [`animateTrack`](#animeteTrack)
- [`assignPathAnimation`](#assignPathAnimation)
- [`assignTrackParent`](#assignTrackParent)
- [`assignPlayerToTrack`](#assignPlayerToTrack)


### updateDependencies
Adds requirements to the choosen level.dat. `Noodle Extensions` is automatically added. You will need to use this if you will be animating `_color`. It is not added automatically.\
Example Usage:
```py
import noodleExtensions as NE

lvl = "path to your level.dat here"
editor = NE.NoodleExtensions(lvl)

editor.updateDependencies("Chroma")
```
`Chroma` will automatically be added as a dependency of your level.\
Note: Even though you can add non-existant mods to this and prevent anyone from ever playing, there's literally no use to it as someone can manually edit the file and remove it.
#### Arguments
- `dependency` The requirement to add.
### pushChanges
Will push all changes to the choosen level.dat. This is a **required** step. Without it, any animations or changes you've made will literally not be put inside the level.dat and nothing will happen. Always include this at the *very end of your file!*
```py
import noodleExtensions as NE

lvl = "path to your level.dat here"
editor = NE.NoodleExtensions(lvl)

# do animator stuff here

editor.pushChanges()
```
pushChanges does not take any arguments.
### getNote
If you want to get a `Note` object that does exist in the level.dat
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"level.dat path")

n = NE.Note(beat=10, index=0, layer=0, type=0, cutDirection=0)

# This will find all notes who have matching data into a list. 
# If they do not have matching customData it will still be put in.
notes = editor.getNote(n, excludeCustomData=True)

# This will find all notes with matching data and customData into a list.
# If the customData does not match, it is ignored.
notes = editor.getNote(n)
```
This will return a list of all notes with matching data.
#### Arguments
- `note` a [`Note`](#note) object.
- `excludeCustomData` (defaults to false) Whether or not the customData needs to match when finding the note.
### getWall
If you want to get a `Obstacle` object that does exist in the level.dat
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"level.dat path")

w = NE.Obstacle(beat=10, index=1, type=1, duration=2, width=2)

# This will find all obstacles who have matching data into a list. 
# If they do not have matching customData it will still be put in.
notes = editor.getWall(w, excludeCustomData=True)

# This will find all notes with matching data and customData into a list.
# If the customData does not match, it is ignored.
notes = editor.getWall(w)
```
This will return a list of all notes with matching data.
#### Arguments
- `wall` a [`Obstacle`](#obstacle) object.
- `excludeCustomData` (defaults to false) Whether or not the customData needs to match when finding the note.

### editNote
Will edit the first note found.
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"Level.dat path")

n = NE.Note(beat=10, index=0, layer=0, type=0, cutDirection=0)

# the ** will save you some time. You could always do new = NE.note(beat=n._time...) but that's slow and inconvenient.
new = NE.Note(**n.note, _track="ExampleTrack")
NE.editNote(n, new)
```
It is heavily suggested when using `editNote` **to not change any form of default info.** (beat, index etc...). This *will* mess up your code.
#### Arguments
- `oldNote` The note's current data.
- `newNote` The note's new data. It is heavily suggested to only change customData here.
- `checkForCustomData` [optional. defaults to False] if set to true, the `oldNote` will need to have matching customData. recommended to leave to False. once edited, changing the data will be complicated.

### editWall
Will edit the first wall found.
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"Level.dat path")

w = NE.Obstacle(beat=10, index=1, type=1, duration=2, width=2)
new = w = NE.Obstacle(**w.obstacle, _track="ExampleTrack")

NE.editWall(w, new)
```
It is heavily suggested when using `editWall` **to not change any form of default info.** (beat, index etc...). This *will* mess up your code.
#### Arguments
- `oldWall` The wall's current data.
- `newWall` The wall's new data.
- `checkForCustomData` [optional. defaults to False] if set to true, the `oldWall` will need to have matching customData. recommended to leave to False. once edited, changing the data will be complicated.

### animateTrack
Animate a track.
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"Level.dat path")

editor.animateTrack(NE.AnimateTrack(beat=10, track="animateTrackExample", duration=1, 
    _position=[
        [0, 0, 0, 0],
        [0, 1, 0, 1]
    ])) # dummy animation that moves the note up
```
If you think that it doesn't look fine enough and needs some tuning, as long as this function has the same beat and track, all other properties will be overwritten with the new data. This allows you to smoothly and easily change property animations.
#### Arguments
- `beat` The beat at which the animation starts.
- `track` The track that will be animated
- `duration` How long the animation should last
- `_property` The properties you wish to animate. To know which ones are correct, refer to [event properties](#Custom-Data-Properties)

### assignPathAnimation
Assigns a path animation to the specified track. A path animation is lifespan based, and not beat based. This means that notes will be animated based off of how far they are from the player.
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"Level.dat path")

editor.assignPathAnimation(NE.AssignPathAnimation(beat=10, track="assignPathAnimationExample", duration=1, 
    _position=[
        [0, 0, 0, 0],
        [0, 1, 0, 1]
    ])) # dummy animation that moves the note up
```
If you think that it doesn't look fine enough and needs some tuning, as long as this function has the same beat and track, all other properties will be overwritten with the new data. This allows you to smoothly and easily change property animations.
#### Arguments
- `beat` The beat at which the animation starts.
- `track` The track that will be animated
- `duration` How long the animation should last
- `_property` The properties you wish to animate. To know which ones are correct, refer to [event properties](#Custom-Data-Properties)
### assignTrackParent
Assigns a track to a parent track - which will make the children track follow and be affected the same way the parent track is affected.
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"Level.dat path")

editor.assignTrackParent(NE.AssignTrackParent(beat=1, tracks=["ChildrenTrack01", "ChildrenTrack02"], parentTrack="ParentTrack"))
```
#### Arguments
- `beat` The beat at which the tracks should be assigned
- `tracks` The tracks to assign
- `parentTrack` The track that will be assigned to
### assignPlayerToTrack
Will assign the player to a track. Not all properties will affect the player. To know which properties will affect the player, review [Custom Data Properties](#custom-data-properties)
```py
import noodleExtensions as NE

editor = NE.NoodleExtensions(r"Level.dat path")

editor.assignPlayerToTrack(NE.AssignPlayerToTrack(beat=1, track="PlayerTrack"))
```
#### Arguments
- `beat` The beat at which the player will be assigned.
- `track` The track to which the playyer will be assigned.