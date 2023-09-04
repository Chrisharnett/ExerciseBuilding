from flask import Flask, render_template, url_for
from objects import *
import csv

application = Flask(__name__)
application.config['SUBMITTED_IMG'] = os.path.join('static', 'img', '')


@application.route('/')
def exercise():
    patterns = getPatterns()
    ex = Exercise(pattern=patterns[0], key="a", mode="major")

    return render_template('index.html', exerciseImage=ex.getImage(), exerciseName=ex.getName().replace("_", " "),
                           exerciseDescrtiption=ex.getDescription(), exerciseDescription=ex.getDescription())

# Use a dictionary to create/store patterns
def getPatterns():
    preamble = r"""#(set-global-staff-size 14)
            """
    timeSignature = (4, 4)

    patterns = {
        "name": "Two_Bar_Tied_Dotted_Half_Notes_Long_Tone",
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (3, 4),
        "notePattern": [[1, "2.~"], [1, "2."]],
        "preamble": preamble
    }, {
        "name": "Whole_Note_Long_Tone",
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": timeSignature,
        "notePattern": [["repeat", [1, "1"]]],
        "preamble": preamble
    }, {
        "name": "Three_Note_Scale",
        "description": "Hold each note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound."
                       "\nRepeat as many times as possible.",
        "timeSignature": timeSignature,
        "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [2, "4"]],
                        [1, "1"]],
        "preamble": preamble
    }

    fields = ["name", "description", "timeSignature", "notePattern", "preamble"]

    with open("static/data/melodicPatterns.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in patterns:
            writer.writerow(row)

    return patterns


if __name__ == '__main__':
    application.run(debug=True, port=5001)
