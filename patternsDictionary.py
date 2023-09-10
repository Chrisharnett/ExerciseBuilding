import pickle
from objects import Pattern

FILENAME = "static/data/melodicPatterns.bin"

def writePatterns(allPatterns):
    file = open(FILENAME, "wb")
    pickle.dump(allPatterns, file)
    file.close()
def writeAllPatterns():
    preamble = r"""#(set-global-staff-size 14)
            """
    patterns = {
        # oneNotePatterns
        "patternType": "long_tone",
        "notePattern": [["repeat", [1, "1"]]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "whole_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "long_tone",
        "notePattern": [["repeat", [1, "2."]]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (3, 4),
        "rhythm": "dotted_half_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "one_note_rhythm",
        "notePattern": [["repeat", [1, "4"], ["r4"], ["r4"], ["r4"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "one_note_rhythm",
        "notePattern": [["repeat", [1, "4"], [1, "4"], ["r4"],  ["r4"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "one_note_rhythm",
        "notePattern": [["repeat", [1, "4"], ["r4"], [1, "4"],  ["r4"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        # Two note patterns
        "patternType": "two_note_scale_pattern",
        "notePattern": [["repeat", [1, "2"], [2, "2"]]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "half_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "two_note_scale_pattern",
        "notePattern": [["repeat", [1, "4"], [2, "2"]]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (3, 4),
        "rhythm": "",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "rhythm",
        "notePattern": [["repeat", [1, "4"], [2, "4"], ["r4"], ["r4"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "rhythm",
        "notePattern": [["repeat", ["r4"], [1, "4"], ["r4"], [2, "4"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        "patternType": "rhythm",
        "notePattern": [["repeat", [1, "4"], ["r4"], [1, "4"],  ["r4"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        # Three note scale patterns
        "patternType": "three_note_scale_pattern",
        "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "2"]], [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        # four note scale patterns
        "patternType": "four_note_scale_pattern",
        "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [5, "4"]],
                        [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        # five note scale patterns
        "patternType": "five_note_scale_pattern",
        "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                         [5, "4"], [4, "4"], [3, "4"], [2, "4"]],
                        [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        # six note scale patterns
        "patternType": "six_note_scale_pattern",
        "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                         [5, "4"], [6, "4"], [5, "4"], [4, "4"],
                         [3, "4"], [2, "4"], [1, "4"], ["r4"]],
                        [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }, {
        # ninth scale pattern
        "patternType": "ninth_scale_pattern",
        "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                         [5, "4"], [6, "4"], [7, "4"], [8, "4"],
                         [9, "4"], [8, "4"], [7, "4"], [6, "4"],
                         [5, "4"], [4, "4"], [3, "4"], [2, "4"]],
                        [1, "1"]],
        "preamble": preamble,
        "description": "Hold the note for the full value. "
                       "\nUse a comfortable dynamic. "
                       "\nStrive for a consistent, clear, in-tune, sound.",
        "timeSignature": (4, 4),
        "rhythm": "quarter_note",
        "articulation": "",
        "dynamic": ""
    }

    allPatterns = {}

    for i, pattern in enumerate(patterns, 1):
        p = Pattern(i, pattern.get('patternType'), pattern.get('notePattern'), pattern.get('preamble'),
                    pattern.get('description'), pattern.get('timeSignature'),
                    pattern.get('rhythm'), pattern.get('articulation'), pattern.get('dynamic'))
        allPatterns[p] = p

    writePatterns(allPatterns)
