from enum import Enum

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
