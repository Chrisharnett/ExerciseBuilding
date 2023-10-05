from patternsDictionary import allPatterns
from routines import majorScale1
from objects import *
import csv
import pickle
import json

global exerciseId
exerciseId = 0
def createExercises(patterns, key, mode):
    exercises = []
    global exerciseId
    for index, pattern in enumerate(patterns):
        p = Pattern(index, pattern.get("patternType"), pattern.get("notePattern"), pattern.get("preamble"), pattern.get("description"),
                    pattern.get("timeSignature"), pattern.get("rhythm"), pattern.get("articulation"), pattern.get("dynamic"),
                    pattern.get("direction"))
        ex = Exercise(exerciseId, p, key=key, mode=mode)
        ex.createImage()
        e = ex.serialize()
        exercises.append(e)
        exerciseId += 1
    return exercises

def createJSON(exercises):

    fields = ["exerciseId", "patternId", "exerciseName",
              "imageFilename", "imageURL", "key",
              "mode", "rhythm", "articulation",
              "dynamic", "timeSignature", "direction",
              "description", "patternType"]

    with open('output/allExercise.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(exercises)

    jsonExercises = json.dumps(exercises)
    with open("output/exerciseJSON.json", 'w') as file:
        file.write(jsonExercises)

def main():
    p = allPatterns
    keys = ["g", "c", "d"]
    allKeys = ["g", "c", "d", "f", "a", "bf", 'e', 'ef', 'b', 'af', 'fs', 'df']
    modes = ["major"]
    allModes = ["major", "natural_minor", "harmonic_minor", "jazz_minor"]
    exercises = []
    for key in keys:
        for mode in allModes:
            e = createExercises(p, key, mode)
            for exercise in e:
                exercises.append(exercise)
    createJSON(exercises)

if __name__ == '__main__':
    main()
