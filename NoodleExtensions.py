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
class Animations():
    # this is for those who have autofill who can't remember the actual strings.
    position = "_position"
    rotation = "_rotation"
    localRotation = "_localRotation"
    scale = "_scale"
    dissolveCube = "_dissolve"
    dissolveArrow = "_dissolveArrow"
    time = "_time"
    color = "_color"

class Editor():
    
    remove = 0
    change = 1
    add = 2
    def __updateDependencies(self, dependency):
        infodatpath = self.CustomLevelPath
        infodatpath = infodatpath.split("\\")
        infodatpath.remove(infodatpath[len(infodatpath)-1])
        infodatpath.append("info.dat")
        infodatpath = "\\".join(infodatpath)

        with open(infodatpath, 'r') as getinfodat:
            infodat = json.load(getinfodat)
        with open(infodatpath, 'w') as editinfodat:
            for x in range(len(infodat["_difficultyBeatmapSets"])):
                # warning: the next few lines are ugly.
                for y in range(len(infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"])):
                    if infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_beatmapFilename"] == self.CustomLevelPath.split("\\")[len(self.CustomLevelPath.split("\\"))-1]: # if the difficulty is the same file as the one the user is using
                        if infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"].get("_requirements") == None:
                            infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"]["_requirements"] = []
                        if not dependency in infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"]["_requirements"]:
                            infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"]["_requirements"].append(dependency)
            json.dump(infodat, editinfodat)

    def __init__(self, CustomLevelPath):
        '''
        - `CustomLevelPath` The path where the `level.dat` is. (include `.dat`)
        '''
        if not os.path.exists(CustomLevelPath):
            raise FileNotFoundError("This level.dat file does not exist.")
        self.CustomLevelPath = CustomLevelPath

        # Edit info.dat to have NoodleExtensions as a req
        self.__updateDependencies("Noodle Extensions")

    def EditBlock(self, beat, pos:tuple, track=None, false=False, interactable=True):
        '''
        Edits a specific block/note (same thing)
        - `beat` The beat at which the block can be found.
        - `pos` The position of the block (tuple). (0, 0) is found left-most row, bottom layer.

        ### To edit the block
        - `track` add / change the track of a block. (ignore this to remove the track.)
        - `false` whether or not the block will affect the player's score.
        - `interactable` whether or not the saber can go through the block.

        Do note that if `interactable` is set to False, `false` will also be set to False. 
        You don't want a block that will kill the player that cannot be hit. 
        '''
        with open(self.CustomLevelPath, 'r') as editnote:
            notes = json.load(editnote)
        with open(self.CustomLevelPath, 'w') as editnote_:
            for x in range(len(notes["_notes"])):
                if notes["_notes"][x]["_time"] == beat and notes["_notes"][x]["_lineIndex"] == pos[0] and notes["_notes"][x]["_lineLayer"] == pos[1]:
                    false = False if not interactable else False if not false else True # "Do note that if `interactable` is set to False, `false` will also be set to False. You don't want a block that will kill the player that cannot be hit."
                    if track == None:
                        notes["_notes"][x]["_customData"] = {
                            "_fake" : false,
                            "_interactable" : interactable
                        }
                    else:
                        notes["_notes"][x]["_customData"] = {
                            "_fake" : false,
                            "_interactable" : interactable,
                            "_track" : track
                        }
            json.dump(notes, editnote_)
    
    def EditWall(self, beat, length, index, track=None, false=False, interactable=True):
        '''
        The exact same as EditNote except it's EditWall (edits a wall.)
        - `beat` The beat at which it starts
        - `length` The beat at which it ends
        - `index` The row on which it's on (0 is left-most)

        - `track` The track to assign to the wall. Leave empty to remove it
        - `false` whether or not the Wall will damage the player.
        - `interactable` whether or not the wall will vibrate the controllers. 
        '''
        with open(self.CustomLevelPath, 'r') as getWalls:
            walls = json.load(getWalls)
        with open(self.CustomLevelPath, 'w') as EditWalls:
            for x in range(len(walls["_obstacles"])):
                if walls["_obstalces"][x]["_time"] == beat and walls["_obstalces"][x]["_duration"] == length-beat and walls["_obstalces"][x]["_lineIndex"] == index: # if we're talking about the same wall
                    if track != None:
                        walls["_obstacles"][x]["_customData"] = {
                            "_track" : track,
                            "_fake" : false,
                            "_interactable" : interactable
                        }
                    else:
                        walls["_obstacles"][x]["_customData"] = {
                            "_fake" : false,
                            "_interactable" : interactable
                        }
                    break
            json.dump(walls, EditWalls)

    def EditEvent(self, time, EventType, track, editType:int, newData:dict=None):
        '''
        Edits a specific customEvent. 
        - `time` the time at which the event occurs.
        - `EventType` the type of the even you want to edit.
        - `track` the track of the even you want to edit
        - `editType` either Editor.remove, or Editor.change.\n
        if using `Editor.remove`, then ignore the `newData` setting.

        - `newData` The new data of the event. If using `Editor.remove` then ignore this.\n
        If not using `Editor.remove`, then insert the new data using `Animator.Animate` as it returns the data you want.
        '''
        with open(self.CustomLevelPath, 'r') as GetEvents:
            events = dict(json.load(GetEvents))
        
        if editType != 0 and newData == None: # if there's missing data and you're not removing
            raise AttributeError("Missing newData setting, as you are not removing the event.")
        with open(self.CustomLevelPath, 'w') as EditEvents:
            if editType == 0: # if wanna remvoe
                for x in range(len(events["_customData"]["_customEvents"])):
                    if events["_customData"]["_customEvents"][x]["_type"] == EventType and events["_customData"]["_customEvents"][x]["_time"] == time and events["_customData"]["_customEvents"][x]["_data"]["_track"] == track: # a long line to just check whether or not the event is the correct one to remove.
                        events["_customData"]["_customEvents"].remove(events["_customData"]["_customEvents"][x])
                        break
                json.dump(events, EditEvents)
        
            elif editType == 1: # if want to overwrite it with something else
                for x in range(len(events["_customData"]["_customEvents"])):
                    if events["_customData"]["_customEvents"][x]["_type"] == EventType and events["_customData"]["_customEvents"][x]["_time"] == time and events["_customData"]["_customEvents"][x]["_data"]["_track"] == track:
                        events["_customData"]["_customEvents"][x] = newData
                        break
            
            elif editType == 2:
                for x in range(len(events["_customData"]["_customEvents"])):
                    if events["_customData"]["_customEvents"][x]["_type"] == EventType and events["_customData"]["_customEvents"][x]["_time"] == time and events["_customData"]["_customEvents"][x]["_data"]["_track"] == track:
                        events["_customData"]["_customEvents"][x]["_data"] == newData["_data"]
                        break
class Animator():

    def __init__(self, editor:Editor):
        '''just put in the Editor object you're using.'''
        self.editor = editor # this is as to be able to access the actual level.dat file.
    
    def Animate(self, eventtype, animationType, data:list, track, start, end) -> dict:
        '''
        Animates a block and returns the Event's dictionary.
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
            self.editor.__updateDependencies("Chroma")
        with open(self.editor.CustomLevelPath, 'r') as GetCustomEvents:
            ce = json.load(GetCustomEvents)
        with open(self.editor.CustomLevelPath, 'w') as EditCustomEvents:
            if ce["_customData"].get("_customEvents") == None:
                ce["_customData"]["_customEvents"] = []
            
            for x in range(len(ce["_customData"]["_customEvents"])):
                if ce["_customData"]["_customEvents"][x]["_data"].get(animationType) != None:
                    if ce["_customData"]["_customEvents"][x]["_data"][animationType] == data and ce["_customData"]["_customEvents"][x]["_type"] == eventtype: # if that event already exists
                        json.dump(ce, EditCustomEvents)
                        return None
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

if __name__ == "__main__":
    print("""
    If you're running this file it seems you don't have a proper understanding of how to use it.
    To use it, go to https://github.com/megamaz/NoodleExtensions-python/blob/master/docs/documentation.md (the documentation) and read it.
    It explains in thorough detail how everything works.

    Just a reminder that this file is not meant to be ran but is meant to be imported. 
    In a python script, it would look like this;

    import NoodleExtensions

    Thank you for using my script!""")