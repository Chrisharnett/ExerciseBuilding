import math

preamble = r"""#(set-global-staff-size 14)
        """
# All ascending scalar patterns
def notePatterns(minNote, maxNote, maxLength):
    allNotePatterns=[]
    notes = []

    # One note options
    for i in range(minNote + 1, maxNote):
        notes = [i]
        allNotePatterns.append(notes)

    # Ascending scalar options
    for i in range(minNote, maxNote + 1):
        notes = []
        for j in range(1, i+1):
            notes.append(j)
        if notes:
            allNotePatterns.append(notes)

    # All descending scalar patterns

    # All descending and ascending scalar patterns

    return allNotePatterns



def main():
    minNote=1
    maxNote=9
    maxLength= 2 * (maxNote)
    notePatterns(minNote, maxNote, maxLength)

if __name__ == '__main__':
    main()


pattern = {
"patternType": "",
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
"patternType": "rhythm",
"notePattern": [["repeat", [1, "4"], ["r4"], [2, "4"], ["r4"]], [1, "1"]],
"preamble": preamble,
"description": "Play both notes evenly and in time.",
"timeSignature": (4, 4),
"rhythm": "quarter-note",
"articulation": [],
"dynamic": "",
"direction": "ascending"
}, {
"patternType": "rhythm",
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
"patternType": "scale",
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
"patternType": "scale",
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
"patternType": "scale",
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
"patternType": "scale",
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
"patternType": "scale",
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
"patternType": "scale",
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
"patternType": "scale",
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
"patternType": "scale",
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
}, {
    "patternType": "long_tone",
    "notePattern": [["repeat", [1, "1"]]],
    "preamble": preamble,
    "description": "Hold the note for the full value, off on 1 (-1). "
                   "\nUse a mp to mf dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "whole_note",
    "articulation": [{"articulation": "fermata",
                      "index": 0,
                      "name": "fermata"}],
    "dynamic": "",
    "direction": ""

}, {
    "patternType": "long_tone",
    "notePattern": [["repeat", [1, "f", "2."]]],
    "preamble": preamble,
    "description": "Hold the note for the full value, off on 1 (-1). "
                   "\nUse a mp to mf dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (3, 4),
    "rhythm": "dotted_half_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [1, "4"], ["r4"], ["r4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nRepeat twice and end with a good whole note."
                   "\nPlay well 5 times.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [1, "4"], [1, "4"], ["r4"],  ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold each note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nRepeat twice and end with a good whole note."
                   "\nPlay well 5 times.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [1, "4"], ["r4"], [1, "4"],  ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold each note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nRepeat twice and end with a good whole note."
                   "\nPlay well 5 times.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    # Two note patterns
    "patternType": "scale",
    "notePattern": [["repeat", [1, "2"], [2, "2"]]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound."
                    "\n Play each note evenly.",
    "timeSignature": (4, 4),
    "rhythm": "half_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "scale",
    "notePattern": [["repeat", [1, "4"], [2, "2"]]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (3, 4),
    "rhythm": "",
    "articulation": [],
    "dynamic": "",
"direction": ""
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [1, "4"], [2, "4"], ["r4"], ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", ["r4"], [1, "4"], ["r4"], [2, "4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    "patternType": "rhythm",
    "notePattern": [["repeat", [1, "4"], ["r4"], [1, "4"],  ["r4"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    # Three note scale patterns
    "patternType": "scale",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "2"]], [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    # four note scale patterns
    "patternType": "scale",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [5, "4"]],
                    [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    # five note scale patterns
    "patternType": "scale",
    "notePattern": [["repeat", [1, "4"], [2, "4"], [3, "4"], [4, "4"],
                     [5, "4"], [4, "4"], [3, "4"], [2, "4"]],
                    [1, "1"]],
    "preamble": preamble,
    "description": "Hold the note for the full value. "
                   "\nUse a comfortable dynamic. "
                   "\nStrive for a consistent, clear, in-tune, sound.",
    "timeSignature": (4, 4),
    "rhythm": "quarter_note",
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    # six note scale patterns
    "patternType": "scale",
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
    "articulation": [],
    "dynamic": "",
    "direction": ""
}, {
    # ninth scale pattern
    "patternType": "scale",
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
    "articulation": [],
    "dynamic": "",
    "direction": ""
}
