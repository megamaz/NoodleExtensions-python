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
# Need someone to add a PATHSLINUX. I own windows and do not know where these are.
EASINGSNET = "https://easings.net"
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

class Editor():
    
    def __init__(self, CustomLevelPath):
        '''
        - `CustomLevelPath` The path where the `level.dat` is. (include `.dat`)
        '''
        if not os.path.exists(CustomLevelPath):
            raise FileNotFoundError("This level.dat file does not exist.")
        self.CustomLevelPath = CustomLevelPath

        # Edit info.dat to have NoodleExtensions as a req
        infodatpath = CustomLevelPath
        infodatpath = infodatpath.split("\\")
        infodatpath.remove(infodatpath[len(infodatpath)-1])
        infodatpath.append("info.dat")
        infodatpath = "\\".join(infodatpath)

        with open(infodatpath, 'r') as getinfodat:
            infodat = json.load(getinfodat)
        with open(infodatpath, 'w') as editinfodat:
            for x in range(len(infodat["_difficultyBeatmapSets"])):
                for y in range(len(infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"])):
                    if infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_beatmapFilename"] == CustomLevelPath.split("\\")[len(CustomLevelPath.split("\\"))-1]: # if the difficulty is the same file as the fucking one the user is using
                        if infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"].get("_requirements") == None:
                            infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"]["_requirements"] = []
                        if "Noodle Extenions" not in infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"]["_requirements"]:
                            infodat["_difficultyBeatmapSets"][x]["_difficultyBeatmaps"][y]["_customData"]["_requirements"].append("Noodle Extensions")
            json.dump(infodat, editinfodat)

    def EditBlock(self, beat, index, layer, track=None, false=False, interactable=True):
        '''
        Edits a specific block/note (same thing)
        - `beat` The beat at which the block can be found.
        - `index` the "_lineIndex" property of the block, or the X position. (0 is left-most)
        - `layer` the "_lineLayer" proeprty of the block, or the Y position. (0 is bottom)

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
                if notes["_notes"][x]["_time"] == beat and notes["_notes"][x]["_lineIndex"] == index and notes["_notes"][x]["_lineLayer"] == layer:
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


class TrackAnimator():

    def __init__(self, editor:Editor):
        '''just put in the Editor object you're using.'''
        self.editor = editor # this is as to be able to access the actual level.dat file.
    
    def position(self, pos:list, track, start, end):
        '''
        - `pos` (list) that should look something like this;
        ```
        [
            [x, y, z, time (beat), ease (optional)],
            [x, y, z, time (beat), ease (optional)],
            ...
        ]
        ``` It will be used to animate the blocks in the track.
        - x     : LEFT/RIGHT
        - y     : UP/DOWN
        - z     : FORWARDS/BACKWARDS
        - time  : The beat where the animation should start
        - ease  : easings. The speed which the note should move between animations. (can be gained from `NoodleExtensions.EASINGSNET`)

        - `track` the track you want to animate.
        - `start` the start (in beats) where the animation should start
        - `end` the end (in beats) where the animation should end.
        '''
    

        with open(self.editor.CustomLevelPath, 'r') as GetCustomEvents:
            ce = json.load(GetCustomEvents)
        with open(self.editor.CustomLevelPath, 'w') as EditCustomEvents:
            if ce["_customData"].get("_customEvents") == None:
                ce["_customData"]["_customEvents"] = []
            
            for x in range(len(ce["_customData"]["_customEvents"])):
                if ce["_customData"]["_customEvents"][x]["_time"] == start: # if that even already exists
                    return
            ce["_customData"]["_customEvents"].append(
                {
                    "_time":start,
                    "_type":"AnimateTrack",
                    "_data":{
                        "_track" : track,
                        "_duration": end-start,
                        "_position":pos
                    }
                }
            )
            json.dump(ce, EditCustomEvents)