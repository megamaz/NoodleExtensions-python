from pathlib import Path

# VScode being stupid fix
# previous_folder = Path(__file__).parent.parent
# import sys
# sys.path += [str(previous_folder)]


import json
from noodleExtensions import *
path = "ExpertPlusStandard.dat"

editor = NoodleExtensions(path)

def test_updateDependencies_singleDifficulty():
    editor.updateDependencies("Dummy Dependency")

    newFile = json.load(open("Info.dat"))
    
    assert "Dummy Dependency" in newFile["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"][0]["_customData"]["_requirements"]

def test_updateDependencies_multipleDifficulty():
    editor_MULTIPLE = NoodleExtensions("ExpertStandard.dat")
    editor_MULTIPLE.updateDependencies("Dummy Dependency for Expert")

    newFile = json.load(open("Info.dat"))

    for x in newFile["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]:
        if x["_beatmapFilename"] == "ExpertStandard.dat":
            assert "Dummy Dependency for Expert" in x["_customData"]["_requirements"]


# def test_createNote():
#     newNote = Note(1, 1, 1, 0, 8, _position=[[0, 0, 0, 0]])
#     editor.createNote(newNote)
#     amnt = 0
#     for x in editor.levelData["_notes"]:
#         if x == newNote.note:
#             amnt += 1
#     # reason for len check explaioned in createwall test.
#     assert newNote.note in editor.levelData["_notes"] and amnt == 1


# def test_createWall():
#     newWall = Obstacle(1, 1, 1, 10, 2, _position=[[0, 0, 0, 0]])
#     editor.createWall(newWall)

#     # Checking len(obstacles) due to the fact I am constantly creating the same wall with same data. To avoid animation stacking, no new walls will be created if the specified wall already exists with 100% matching data.
#     amnt = 0
#     for x in editor.levelData["_obstacles"]:
#         if x == newWall.obstacle:
#             amnt += 1
#     assert newWall.obstacle in editor.levelData["_obstacles"] and amnt == 1


def test_getNote():
    noteToFind = Note(1, 1, 1, 0, 8, _position=[[0, 0, 0, 0]])
    editor.levelData["_notes"].append(noteToFind.note)
    noteFound = editor.getNote(noteToFind)

    # They have two different places in memory although they share the same bit of data.
    # This is for STACKED NOTE SUPPORT. A new Note object is created from the dict data of the given "noteToFind". 
    # So instead of `assert noteToFind in noteFound` I need to do this because otherwise it will say thay noteToFind isn't in noteFound although they have the same data. As I said, that is due to the fact that every Note obejct inside the noteFound is a new Note object for stacked note support.
    assert noteToFind.note == noteFound[0].note
    editor.levelData["_notes"].remove(noteToFind.note)


def test_getWall():
    wallToFind = Obstacle(1, 1, 1, 10, 2, _position=[[0, 0, 0, 0]])
    editor.levelData["_obstacles"].append(wallToFind.obstacle)
    wallFound = editor.getWall(wallToFind)

    # reason for this explainedin getNote test.
    assert wallToFind.obstacle == wallFound[0].obstacle
    editor.levelData["_obstacles"].remove(wallToFind.obstacle)

def test_editNote():
    noteToFind = Note(1, 1, 1, 0, 8, _position=[[0, 0, 0, 0]])
    result = editor.editNote(noteToFind, Note(1, 1, 1, 0, 8, _track="TestTrack"))

    assert result is not None

    # since the note above was edited to have different data, it would return NONE because it couldn't be found.
    result = editor.editNote(noteToFind, Note(1, 1, 1, 0, 8, _track="TestTrack"), True)

    assert result is None

def test_editWall():
    walltoFind = Obstacle(1, 1, 1, 4, 1, _position=[[0, 0, 0, 0]])
    result = editor.editWall(walltoFind, Obstacle(1, 1, 1, 4, 1, _track="ThereIsNoTrack"))
    assert result is not None

    # since the note has been edited to have differing data, result should be none because the wall couldn't be found.
    result = editor.editWall(walltoFind, Obstacle(1, 1, 1, 4, 1, _track="ThereIsNoTrack"), True)
    assert result is None

def test_animatetrack():
    # easings can be gained from https://easings.net/
    atevent = AnimateTrack(1, "TestTrack", 1, _position=[[0, 500, 0, 0], [0, 0, 0, 1, "easeOutBounce"]])
    editor.animateTrack(atevent)
    
    assert atevent.event in editor.levelData["_customData"]["_customEvents"]

def test_pathAnim():
    pathAnim = AassignPathAnimation(1, "TestTrack", 10, _scale=[
        [1, 1, 2, 0]
        ])
    editor.assignPathAnimation(pathAnim)
    
    assert pathAnim.event in editor.levelData["_customData"]["_customEvents"]

def test_assginTrackParent():
    parentEvent = editor.assignTrackParent(AssignTrackParent(1, ["TestTrack01", "TestTrack02"], "ParentTrack"))
    
    assert parentEvent in editor.levelData["_customData"]["_customEvents"]

def testAssignPlayerToTrack():
    pToTrack = editor.assignPlayerToTrack(AssignPlayerToTrack(4, "Haha player is child"))

    assert pToTrack in editor.levelData["_customData"]["_customEvents"]
def test_pushData():
    editor.pushChanges()
    lvl = json.load(open(path))
    assert len(lvl["_notes"]) >= 1 and len(lvl["_obstacles"]) >= 1

