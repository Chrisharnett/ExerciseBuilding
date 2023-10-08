from notePatternGenerator import notePatterns
from rhythmPatternGenerator import rhythmPatterns

preamble = r"""#(set-global-staff-size 14)
        """


def main():
    # TODO: Min note and max note for range. Attach to instruments
    minNote = 1
    maxNote = 9
    maxLength = 2 * (maxNote)
    notePatternDictionary = notePatterns(minNote, maxNote, maxLength)
    rhythms()

if __name__ == '__main__':
    main()


pattern = {
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
}