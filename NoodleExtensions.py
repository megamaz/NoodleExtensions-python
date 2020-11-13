# PPPPPPPPPPPPPPPPP   NNNNNNNN        NNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
# P::::::::::::::::P  N:::::::N       N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# P::::::PPPPPP:::::P N::::::::N      N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# PP:::::P     P:::::PN:::::::::N     N::::::NEE::::::EEEEEEEEE::::EEE::::::EEEEEEEEE::::E
#   P::::P     P:::::PN::::::::::N    N::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
#   P::::P     P:::::PN:::::::::::N   N::::::N  E:::::E               E:::::E
#   P::::PPPPPP:::::P N:::::::N::::N  N::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE
#   P:::::::::::::PP  N::::::N N::::N N::::::N  E:::::::::::::::E     E:::::::::::::::E
#   P::::PPPPPPPPP    N::::::N  N::::N:::::::N  E:::::::::::::::E     E:::::::::::::::E
#   P::::P            N::::::N   N:::::::::::N  E::::::EEEEEEEEEE     E::::::EEEEEEEEEE
#   P::::P            N::::::N    N::::::::::N  E:::::E               E:::::E
#   P::::P            N::::::N     N:::::::::N  E:::::E       EEEEEE  E:::::E       EEEEEE
# PP::::::PP          N::::::N      N::::::::NEE::::::EEEEEEEE:::::EEE::::::EEEEEEEE:::::E
# P::::::::P          N::::::N       N:::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# P::::::::P          N::::::N        N::::::NE::::::::::::::::::::EE::::::::::::::::::::E
# PPPPPPPPPP          NNNNNNNN         NNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
#
# Python Noodle Extensions Editor. (Great name, I know.) I can't do ASCII, so I used http://patorjk.com/software/taag/#p=testall&h=0&v=0&f=Alpha&t=PNEE "Doh" (Pronounced the same as Knee, /nē/)
# This code is awful. Please improve it.

import json, os
from pathlib import Path
from enum import Enum


PATHSWINDOWS = { # A list of internal Beat Saber download paths.
    "Steam":r"C:\Program Files (x86)\Steam\steamapps\common\Beat Saber",
    "Oculus":r"C:\OculusApps\Software\hyperbolic-magnematism-beat-saber"
}
PATHSLINUX = {
    "Steam":r"~/.steam/steam/SteamApps/common/Beat Saber",
    "Oculus":r"unknown" # I need someone to add an oculus download path (if exists) for Linux
}
EASINGSNET = "https://easings.net"
ANIMATORTYPES = [
    "_position",
    "_rotation",
    "_localRotation",
    "_scale",
    "_dissolve",
    "_dissolveArrow",
    "_time",
    "_color"
]
ANIMATORFORMATS = {
     "_position":       '[left/right, up/down, forw/backw, time (beat), "easing"]',
     "_rotation":       '[pitch, yaw, roll, time (beat), "easing"]',
"_localRotation":       '[pitch, yaw, roll, time (beat), "easing"]',
        "_scale":       '[left/right, up/down, forw/backw, time (beat), "easing"]',
     "_dissolve":       '[amount, time (beat), "easing"]',
"_dissolveArrow":       '[amount, time (beat), "easing"]',
         "_time":       '[lifespan, time (beat), "easing"]',
        "_color":       '[red, green, blue, time, easing]'
}
EVENTTYPES = [
    "AnimateTrack",
    "AssignPathAnimation"
]
EVENTTYPESTRACK = [
    "AssignTrackParent",
    "AssignPlayerToTrack"
]
EASINGS = [
    "easeInsine",
    "easeOutSine",
    "easeInOutSine",
    "easeInCubic",
    "easeOutCubic",
    "easeInOutCubic",
    "easeInQuint",
    "easeOutQuint",
    "easeInOutQuint",
    "easeInCirc",
    "easeOutCirc",
    "easeInOutCirc",
    "easeInElastic",
    "easeOutElastic",
    "easeInOutElastic",
    "easeInQuad",
    "easeOutQuad",
    "easeInOutQuad",
    "easeInQuart",
    "easeOutQuart",
    "easeInOutQuart",
    "easeInExpo",
    "easeOutExpo",
    "easeInOutExpo",
    "easeInBack",
    "easeOutBack",
    "easeInOutBack",
    "easeInBounce",
    "easeOutBounce",
    "easeInOutBounce"
]

class Constants:
    class Animations(Enum):
        position         = "_position"
        rotation         = "_rotation"
        localRotation    = "_localRotation"
        scale            = "_scale"
        dissolveCube     = "_dissolve"
        dissolveArrow    = "_dissolveArrow"
        time             = "_time"
        color            = "_color"
    class AnimationTypes(Enum):
        AnimateTrack        = "AnimateTrack"
        AssignPathAnimation = "AssignPathAnimation"
        AssignTrackParent   = "AssignTrackParent"
        AssignPlayerToTrack = "AssignPlayerToTrack"
    class EditorEvent(Enum):
        remove  = 0
        change  = 1
        add     = 2

class Editor:

    def updateDependencies(self, dependency:str):
        '''Update Dependencies adds a `_requirements` item. Do note it doesn't check if you have it installed nor does it check whether or not that dependency is real.\n
        However, it does check whether or not it's already in the list. 
        - `dependency` the string item you want to add to the `_requirements`
        '''
        infodatpath = self.customLevelPath
        infodatpath = infodatpath.split("\\")
        infodatpath.remove(infodatpath[len(infodatpath)-1])
        infodatpath.append("info.dat")
        infodatpath = "\\".join(infodatpath)

        with open(infodatpath, 'r') as getinfodat:
            infodat = json.load(getinfodat)
        with open(infodatpath, 'w') as editinfodat:
            for x in range(len(infodat["_difficultyBeatmapSets"])):
                # warning: the next few lines are ugly.
                for _difficultyBeatmaps in infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"]:
                    if _difficultyBeatmaps["_beatmapFilename"] == self.customLevelPath.split("\\")[len(self.customLevelPath.split("\\"))-1]: # if the difficulty is the same file as the one the user is using
                        if _difficultyBeatmaps["_customData"].get("_requirements") == None:
                            _difficultyBeatmaps["_customData"]["_requirements"] = []
                        if not dependency in _difficultyBeatmaps["_customData"]["_requirements"]:
                            _difficultyBeatmaps["_customData"]["_requirements"].append(dependency)
            json.dump(infodat, editinfodat)

    def __init__(self, customLevelPath):
        '''
        - `customLevelPath` The path where the `level.dat` is. (include `.dat`)
        '''
        if not os.path.exists(customLevelPath):
            raise FileNotFoundError("This level.dat file does not exist.")
        self.customLevelPath = customLevelPath

        # Edit info.dat to have NoodleExtensions as a req
        self.updateDependencies("Noodle Extensions")

    def editBlock(self, beat, pos:tuple, track=None, false=False, interactable=True):
        '''Edits a specific block/note (same thing)
        - `beat` The beat at which the block can be found.
        - `pos` The position of the block (tuple). (0, 0) is found left-most row, bottom layer.

        ### To edit the block
        - `track` add / change the track of a block. (ignore this to remove the track.)
        - `false` whether or not the block will affect the player's score.
        - `interactable` whether or not the saber can go through the block.

        Do note that if `interactable` is set to False, `false` will also be set to False.
        You don't want a block that will kill the player that cannot be hit.
        '''
        with open(self.customLevelPath, 'r') as editnote:
            notes = json.load(editnote)
        with open(self.customLevelPath, 'w') as editnote_:
            for note in notes["_notes"]:
                if note["_time"] == beat and note["_lineIndex"] == pos[0] and note["_lineLayer"] == pos[1]:
                    false = False if not interactable else False if not false else True # "Do note that if `interactable` is set to False, `false` will also be set to False. You don't want a block that will kill the player that cannot be hit."
                    if track == None:
                        note["_customData"] = {
                            "_fake" : false,
                            "_interactable" : interactable
                        }
                    else:
                        note["_customData"] = {
                            "_fake" : false,
                            "_interactable" : interactable,
                            "_track" : track
                        }
            json.dump(notes, editnote_)

    def editWall(self, beat, length, index, track=None, false=False, interactable=True):
        '''The exact same as EditNote except it's EditWall (edits a wall.)
        - `beat` The beat at which it starts
        - `length` The beat at which it ends
        - `index` The row on which it's on (0 is left-most)

        - `track` The track to assign to the wall. Leave empty to remove it
        - `false` whether or not the Wall will damage the player.
        - `interactable` whether or not the wall will vibrate the controllers.
        '''
        with open(self.customLevelPath, 'r') as getWalls:
            walls = json.load(getWalls)
        with open(self.customLevelPath, 'w') as EditWalls:
            for obst in walls["_obstacles"]:
                if obst["_time"] == beat and obst["_duration"] == length-beat and obst["_lineIndex"] == index: # if we're talking about the same wall
                    if track != None:
                        obst["_customData"] = {
                            "_track" : track,
                            "_fake" : false,
                            "_interactable" : interactable
                        }
                    else:
                        obst["_customData"] = {
                            "_fake" : false,
                            "_interactable" : interactable
                        }
                    break
            json.dump(walls, EditWalls)

    def editEvent(self, time, EventType, track, editType:int, newData:dict=None):
        '''Edits a specific customEvent.
        - `time` the time at which the event occurs.
        - `EventType` the type of the even you want to edit.
        - `track` the track of the even you want to edit
        - `editType` either Constants.EditorEvent.remove, or Constants.EditorEvent.change.\n
        if using `Constants.EditorEvent.remove`, then ignore the `newData` setting.

        - `newData` The new data of the event. If using `Constants.EditorEvent.remove` then ignore this.\n
        If not using `Constants.EditorEvent.remove`, then insert the new data using `Animator.animate` as it returns the data you want.
        '''
        with open(self.customLevelPath, 'r') as fd_get_events:
            events:dict = json.load(fd_get_events)

        if editType != Constants.EditorEvent.remove and newData is None: # if there's missing data and you're not removing
            raise AttributeError("Missing newData setting, as you are not removing the event.")

        with open(self.customLevelPath, 'w') as fd_edit_events:
            customEvents = events["_customData"]["_customEvents"]
            if editType == Constants.EditorEvent.remove:
                for x in range(len(customEvents)):
                    if customEvents[x]["_type"] == EventType and customEvents[x]["_time"] == time and customEvents[x]["_data"]["_track"] == track: # a long line to just check whether or not the event is the correct one to remove.
                        customEvents.remove(customEvents[x])
                        break
                json.dump(events, fd_edit_events)

            elif editType == Constants.EditorEvent.change:
                for x in range(len(customEvents)):
                    if customEvents[x]["_type"] == EventType and customEvents[x]["_time"] == time and customEvents[x]["_data"]["_track"] == track:
                        customEvents[x] = newData
                        break

            elif editType == Constants.EditorEvent.add:
                for x in range(len(customEvents)):
                    if customEvents[x]["_type"] == EventType and customEvents[x]["_time"] == time and customEvents[x]["_data"]["_track"] == track:
                        customEvents[x]["_data"] == newData["_data"] # FIXME wtf
                        break
class Animator:

    def __init__(self, editor:Editor):
        '''just put in the Editor object you're using.'''
        if editor is None:
            raise ValueError("editor cannot be None")

        self.editor = editor # this is as to be able to access the actual level.dat file.

    def animate(self, eventtype, animationType, data:list, track, start, end) -> dict:
        '''Animates a block and returns the Event's dictionary.
        This doesn't support `AssignTrackParent` and `AssignPlayerToTrack`.\n
        Instead, use `Animator.editTrack`

        - `data` (list) that should look something like this;
        - `eventtype` what kind of animation is this (NoodleExtensions.EVENTTYPES)
        - `animationType` how the note should be animated. (NoodleExtensions.ANIMATIONTYPES)

        It will be used to animate the blocks in the track.
        - First few data points. (Gained from NoodleExtensions.TRACKANIMATIONFORMATS)
        - time  : The beat where the animation should start
        - ease  : easings. The speed which the note should move between animations. (can be gained from `NoodleExtensions.EASINGSNET`)

        - `track` the track you want to animate.
        - `start` the start (in beats) where the animation should start
        - `end` the end (in beats) where the animation should end.
        '''

        if animationType not in ANIMATORTYPES:
            raise IndexError(f"The provided animation type {animationType} is not valid.")

        if eventtype not in EVENTTYPES:
            raise IndexError(f"The provided event type {eventtype} is not valid")


        if animationType == "_color":
            # add chroma as a requirement if using _color
            self.editor.updateDependencies("Chroma")
        with open(self.editor.customLevelPath, 'r') as GetCustomEvents:
            ce = json.load(GetCustomEvents)
        with open(self.editor.customLevelPath, 'w') as EditCustomEvents:
            if ce["_customData"].get("_customEvents") == None:
                ce["_customData"]["_customEvents"] = []

            for event in ce["_customData"]["_customEvents"]:
                if event["_data"].get(animationType) is not None:
                    if event["_data"][animationType] == data and event["_type"] == eventtype: # if that event already exists
                        json.dump(ce, EditCustomEvents)
                        return

            ce["_customData"]["_customEvents"].append(
                {
                    "_time":start,
                    "_type":eventtype,
                    "_data":{
                        "_track" : track,
                        "_duration": end-start,
                        animationType:data
                    }
                }
            )
            json.dump(ce, EditCustomEvents)
            return  {
                    "_time":start,
                    "_type":eventtype,
                    "_data":{
                        "_track" : track,
                        "_duration": end-start,
                        animationType:data
                    }
                }
    def editTrack(self, eventType, time, tracks, parentTrack:str=None) -> dict:
        '''Edit Track allows you to either do `AssignTrackParent` or `AssignPlayerToTrack` and returns the event
        - `eventType` Either `AssignTrackParent` or `AssignPlayerToTrack`
        - `time` The time (in beats) at which the event should happen
        - `tracks` either a list of all the tracks you want to edit or a single track.
        - `parentTrack` the track you want all of the `tracks` to be parented to. Only needed if using  `AssignTrackParent`
        '''

        tracks = tracks.split() if type(tracks) != list else tracks # Makes tracks a list if it is a string
        if eventType == "AssignTrackParent" and parentTrack is None:
            raise ValueError("Received AssignTrackParent but no parentTrack")
        
        if eventType == "AssignTrackParent":
            event = {
                "_time":time,
                "_type":eventType,
                "_data":{
                    "_childrenTracks":tracks,
                    "_parentTrack":parentTrack
                }
            }            
            with open(self.editor.customLevelPath, 'r') as getEvents:
                events = json.load(getEvents)

            with open(self.editor.customLevelPath, 'w') as editEvents:
                for customs in events["_customEvents"]:
                    if customs == event: # if the event already exists
                        return
                events["_customEvents"].append(event)
                json.dump(events, editEvents)
            return event
        
        elif eventType == "AssignPlayerToTrack":
            event = {
                "_time":time,
                "_type":eventType,
                "_data":{
                    "_track":tracks[0]
                }
            }

            with open(self.editor.customLevelPath, 'r') as getEvents:
                events = json.load(getEvents)
            
            with open(self.editor.customLevelPath, 'w') as editEvents:
                for customs in events["_customEvents"]:
                    if customs == event:
                        return
                events["_customEvents"].append(event)
                json.dump(events, editEvents)


if __name__ == "__main__":
    print("""
If you're running this file it seems you don't have a proper understanding of how to use it.
To use it, go to https://github.com/megamaz/NoodleExtensions-python/blob/master/docs/documentation.md (the documentation) and read it.
It explains in thorough detail how everything works.

Just a reminder that this file is not meant to be ran but is meant to be imported.
In a python script, it would look like this;

import NoodleExtensions

If you're unsure on how to use Python, then I suggest you take a look at the docs, or do a full course somewhere. I'm personally partially self-taught, and taught from my father.
docs            -   https://docs.python.org/
full course     -   https://www.youtube.com/watch?v=rfscVS0vtbw


Thank you for using my script!

""")