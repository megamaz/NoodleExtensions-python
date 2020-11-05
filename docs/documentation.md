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
The animator can currently only animate tracks and path animations. `AssignPlayerToTrack` and `AssignTrackParent` are soon to come!
Animation quick guide:
- [`_position`](#_position)

## _position
