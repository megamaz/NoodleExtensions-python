# Python Noodle Extensions Editor (PNEE)
if you're unsure on how to use this script, this should help you out. 

## Setting-Up
if you haven't already, download the NoodleExtensions.py from the [Latest Release](https://github.com/megamaz/NoodleExtensions-python/releases) and put it inside the same folder that will contain your code.\
To start using this script, very simply just `import NoodleExtensions` and you should be good to go!

# Animating
- [Position](#Position)

### Position
Here's an [example script](https://github.com/megamaz/noodleextensions-python/examples/track/1_position) to make a note bounce down from the sky.
```py
import NoodleExtensions

editor = NoodleExtensions.Editor(r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels\ExampleLevel\EasyStandard.dat")
animator = NoodleExtensions.Animator(editor)

editor.EditBlock(3, (1, 0), "MoveTrack")

animator.Animate("AnimateTrack", "_position", [
    [0, 10, 0, 0],
    [0, 0, 0, 1, "easeOutBounce"]
], "MoveTrack", 1, 2)
```
In brief, this script above grabs a note, gives it the `MoveTrack` track, and the Animator object animates the note falling using the `easeOutBounce` [easing](https://easings.net).
That's really all there is to it. Here is a line by line explanation;
```py
import NoodleExtensions
```
This line **must** be in your project for it to work. It basically tells your script to use the `NoodleExtensions.py` you downloaded.
```py
editor = NoodleExtensions.Editor(r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber\Beat Saber_Data\CustomWIPLevels\ExampleLevel\EasyStandard.dat")
```
Although this line might seem complicated, it would look much simpler if I just removed the path to the `level.dat`: `editor = NoodleExtensions.Editor("level.dat Path")`\
This just tells your script which level you want to to edit. It also automatically adds Noodle Extensions as a requirement, so you don't need to do that.
```py
animator = NoodleExtensions.Animator(editor)
```
This line is quite simple. It tells your code that you in fact, want to animate stuff. You feed in the editor so the Animtor knows what you want to animate.\
It's the next line that looks much harder. To make it easier to read, I spread it out over multiple lines. 
```py
animator.Animate("AnimateTrack", "_position", [
    [0, 10, 0, 0],
    [0, 0, 0, 1, "easeOutBounce"]
], "MoveTrack", 1, 2)
```
The first setting is `"AnimmateTrack"` which means that this line is going to be animating a track. The next setting, `"_position"`, says that this animation type is going to be a positional animation. The next setting is a nested list (lists within lists) that will contain positional animation.\
Position statements are going to look like this; `[x, y, z, time, easing]`
- x : Left/Right
- y : Up/Down
- z : Forw/Backw
- time : the time, 0-1, where the animation should happen
- easing : all easings are gained from [easings.net](https://easings.net)
The first setting in the nested list says that at the very beginning the note should be 10 units high. The next setting says that it should go back to where it was - (0, 0, 0) with the bouncing easing. \
After the nested list, you name the track you want to animte - `MoveTrack` - when the animation should start (beats) and when it should end (beats)