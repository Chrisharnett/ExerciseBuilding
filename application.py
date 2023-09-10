import random
import pickle
from flask import Flask, render_template, url_for
from objects import *
import patternsDictionary

application = Flask(__name__)
application.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')

@application.route('/')
def exercise():
    # patternType, notePattern, Preamble, Description, TimeSignature, Rhythm, Articulation, Dynamic
    patterns = getPatterns()

    patternName, pattern = random.choice(list(patterns.items()))
    ex = Exercise(pattern=pattern, key="a", mode="major", direction="")

    return render_template('index.html', exercise=ex)


@application.route('/allPatterns')
def allPatterns():

    patterns = getPatterns()
    # all exercises in G Major
    allExercises = []
    for exerciseId, pattern in enumerate(patterns):
        ex = Exercise(exerciseId, patterns[pattern], key="g", mode="major")
        allExercises.append(ex)

    return render_template('allPatterns.html', exercises=allExercises)

@application.route('/newPatternView')
def newPatternView():
    patternsDictionary.writeAllPatterns()
    patterns = getPatterns()
    lastPattern = list(patterns)[-1]
    ex = Exercise(0, patterns.get(lastPattern), key="g", mode="major")

    return render_template('newPatternView.html', exercise=ex)

def getPatterns():
    with open("static/data/melodicPatterns.bin", "rb") as file:
        patterns = pickle.load(file)
    return patterns


if __name__ == '__main__':
    application.run(debug=True, port=5001)
