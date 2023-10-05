
import pickle
from flask import Flask, render_template, url_for, send_from_directory, redirect, jsonify
from objects import *
import patternsDictionary

application = Flask(__name__)
application.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(application.instance_path, 'flaskr.sql')
)

try:
    os.makedirs(application.instance_path)
except OSError:
    pass

application.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

currentPatternIndex = 0

def clearImageDirectory():
    try:
        fileList = os.listdir(application.config['SUBMITTED_IMG'])
        for fileName in fileList:
            filePath = os.path.join(application.config['SUBMITTED_IMG'] + fileName)
            if os.path.isfile(filePath):
                os.remove(filePath)

    except Exception as e:
        print("An error occurred.", e)


def loadPatterns():
    patternsDictionary.allPatterns()
    patterns = getPatterns()
    return patterns


def getPatterns():
    with open("static/data/melodicPatterns.bin", "rb") as file:
        patterns = pickle.load(file)
    return patterns


def loadSession():
    patternIndexNumbers = [10, 5, 14, 6, 12]
    patterns = loadPatterns()
    sessionExercises = []
    for n in patternIndexNumbers:
        ex = Exercise(n, patterns.get(list(patterns)[n]), key="g", mode="major")
        if not os.path.exists(ex.path()):
            ex.createImage()
        sessionExercises.append({"name": ex.exerciseFileName,
                                 "exercise": ex,
                                 "imageSrc": ex.exerciseFileName})
    currentSession = Routine(sessionExercises)
    return currentSession


currentPracticeSession = loadSession()


@application.route('/')
def index():
    patterns = loadPatterns()
    ex = Exercise(0, patterns.get(list(patterns)[-1]), key="g", mode="major")
    ex.createImage()
    return render_template('index.html', exercise=ex)


@application.route('/session')
def thisSession():
    global currentPatternIndex
    global currentPracticeSession
    currentPracticeSession.createSessionSequence()
    currentPatternIndex = 0
    firstExercise = currentPracticeSession.sessionExercises[currentPatternIndex].get("exercise")
    return render_template('session.html', exercise=firstExercise)


@application.route('/session/nextExercise')
def nextExercise():
    global currentPatternIndex
    global currentPracticeSession
    if currentPatternIndex >= len(currentPracticeSession.sessionSequence):
        currentPatternIndex = 0
    elif currentPatternIndex < len(currentPracticeSession.sessionSequence) - 1:
        currentPatternIndex += 1
        for exercise in currentPracticeSession.sessionExercises:
            if exercise.get("name") == currentPracticeSession.sessionSequence[currentPatternIndex]:
                return jsonify(exercise.get("exercise").serialize())
    else:
        # change this to bring you to the post session page.
        currentPatternIndex = 0
        clearImageDirectory()
        return jsonify({'error': 'Finished session'})


@application.route('/allPatterns')
def allPatterns():
    patterns = getPatterns()
    # all exercises in G Major
    allExercises = []
    for exerciseId, pattern in enumerate(patterns):
        ex = Exercise(exerciseId, patterns[pattern], key="g", mode="major")
        allExercises.append(ex)
        ex.createImage()
    return render_template('allPatterns.html', exercises=allExercises)


if __name__ == '__main__':
    application.run(debug=True, port=5001)
