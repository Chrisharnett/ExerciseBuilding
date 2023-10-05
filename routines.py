exercises = [{"index": 1,
              "count": 0}]
round = 0
ROUNDMAX = 4

def exerciseSelector(exercises):
    pass

preamble = r"""#(set-global-staff-size 14)
                """

testPattern = [{
    # ninth scale pattern
    "patternType": "ninth_scale_pattern",
    "notePattern": [["repeat", [8, "4"], [7, "4"], [6, "4"], [5, "4"],
                     [4, "4"], [3, "4"], [2, "4"], [1, "4"],
                     [-1, "4"], [1, "4"], [2, "4"], [3, "4"],
                     [4, "4"], [5, "4"], [6, "4"], [7, "4"]],
                    [1, "1"]],
    "preamble": preamble,
    "description": "Quick finger movement for a clean sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending, ascending"
}]


majorScale1 = {
    "patternType": "long_tone",
    "notePattern": [["repeat", [1, "1"]]],
    "preamble": preamble,
    "description": "Hold the note for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
},{
    "patternType": "long_tone",
    "notePattern": [["repeat", [2, "1"]]],
    "preamble": preamble,
    "description": "Hold the note for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "one_bar_rhythm",
    "notePattern": [["repeat", [1, "4"], ["r4"], [2, "4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Play both notes evenly and in time.",
    "timeSignature": (4, 4),
    "rhythm": "quarter-note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending"
}, {
    "patternType": "one_bar_rhythm",
    "notePattern": [["repeat", [2, "4"], ["r4"], [1, "4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Play the notes evenly and precisely.",
    "timeSignature": (4, 4),
    "rhythm": "quarter-note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending"
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Quick, precise finger movement.",
    "timeSignature": (4, 4),
    "rhythm": "quarter-note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending"
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [3, "4"], [2, "4"], [1, "4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Play all notes with the same tone.",
    "timeSignature": (4, 4),
    "rhythm": "quarter-note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending, ascending"
},{
    "patternType": "long_tone",
    "notePattern": [["repeat", [3, "1"]]],
    "preamble": preamble,
    "description": "Hold the note with a strong sound for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "interval",
    "notePattern": [["repeat", ["r4"], [1, "4"], [3, "4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Quick and precise finger movement.",
    "timeSignature": (4, 4),
    "rhythm": "quarter-note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending"
}, {
    "patternType": "long_tone",
    "notePattern": [["repeat", [4, "1"]]],
    "preamble": preamble,
    "description": "Hold the note with a strong sound for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
}, {# five note scale patterns
    "patternType": "five_note_scale",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                     [5, "2"], ["r2"]]],
    "preamble": preamble,
    "description": "Play all notes evenly. Look ahead to the next note.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending"
},{
    "patternType": "long_tone",
    "notePattern": [["repeat", [5, "1"]]],
    "preamble": preamble,
    "description": "Hold the note with a strong sound for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "five_note_scale",
    "notePattern": [["repeat", [5, "4"], [4, "4"], [3, "4"], [2, "4"],
                     [1, "2"], ["r2"]]],
    "preamble": preamble,
    "description": "Play all notes evenly. Look ahead to the next note.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending"
}, {
    "patternType": "arpeggio",
    "notePattern": [["repeat", [1, "4"], [3, "4"], [5, "4"], ["r4"],
                     [1, "2"], ["r2"]]],
    "preamble": preamble,
    "description": "This is an arpeggio. Notice how it skips notes..",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending"
},{
    "patternType": "long_tone",
    "notePattern": [["repeat", [6, "1"]]],
    "preamble": preamble,
    "description": "Hold the note with a strong sound for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
},{
    "patternType": "five_note_scale_pattern",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                     [5, "4"], [4, "4"], [3, "4"], [2, "4"]],
                    [1, "1"]],
    "preamble": preamble,
    "description": "Play each note evenly. Repeat as many times as you can!",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending, descending"
},{
    # five note scale patterns
    "patternType": "five_note_scale_pattern",
    "notePattern": [["repeat", [5, "4"], [4, "4"], [3, "4"], [2, "4"],
                     [1, "4"], [2, "4"], [3, "4"], [4, "4"]],
                    [5, "1"]],
    "preamble": preamble,
    "description": "Play strictly in time with the metronome.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending, ascending"
},{
    "patternType": "long_tone",
    "notePattern": [["repeat", [7, "1"]]],
    "preamble": preamble,
    "description": "Hold the note with a strong sound for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
},{
    "patternType": "Scale_pattern",
    "notePattern": [["repeat", [8, "4"], [7, "4"], [6, "4"], [5, "4"],
                     [4, "4"], [3, "4"], [2, "4"], [1, "4"]]],
    "preamble": preamble,
    "description": "Play strictly in time with the metronome.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending"
},{
    "patternType": "Scale_pattern",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                     [5, "4"], [6, "4"], [7, "4"], [8, "4"]]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending"
},{
    "patternType": "long_tone",
    "notePattern": [["repeat", [8, "1"]]],
    "preamble": preamble,
    "description": "Hold the note with a strong sound for as long as you can. Make sure it has a clean ending!",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                     "index": 0,
                     "name": "fermata"}],
    "dynamic": "",
    "direction": ""
},{
    # ninth scale pattern
    "patternType": "ninth_scale_pattern",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                     [5, "4"], [6, "4"], [7, "4"], [8, "4"],
                     [9, "4"], [8, "4"], [7, "4"], [6, "4"],
                     [5, "4"], [4, "4"], [3, "4"], [2, "4"]],
                    [1, "1"]],
    "preamble": preamble,
    "description": "Adding the ninth helps the scale fit the metre.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending, descending"
}, {
    "patternType": "arpeggio",
    "notePattern": [["repeat", [5, "4"], [3, "4"], [1, "4"], ["r4"],
                     [1, "2"], ["r2"]]],
    "preamble": preamble,
    "description": "This is an arpeggio. Notice how it skips notes..",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending"
},{
    # ninth scale pattern
    "patternType": "ninth_scale_pattern",
    "notePattern": [["repeat", [8, "4"], [7, "4"], [6, "4"], [5, "4"],
                     [4, "4"], [3, "4"], [2, "4"], [1, "4"],
                     [-1, "4"], [1, "4"], [2, "4"], [3, "4"],
                     [4, "4"], [5, "4"], [6, "4"], [7, "4"]],
                    [8, "1"]],
    "preamble": preamble,
    "description": "Quick finger movement for a clean sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending, ascending"
}, {
    "patternType": "arpeggio",
    "notePattern": [["repeat", [1, "4"], [3, "4"], [5, "4"], [3, "4"],
                     [1, "2"], ["r2"]]],
    "preamble": preamble,
    "description": "Repeat as many times as possible before the last note.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "ascending, descending"
}, {
    "patternType": "arpeggio",
    "notePattern": [["repeat", [5, "4"], [3, "4"], [1, "4"], [3, "4"],
                     [5, "2"], ["r2"]]],
    "preamble": preamble,
    "description": "Repeat as many times as possible before the last note.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": "descending, ascending"
}