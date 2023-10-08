# All ascending scalar patterns

def notePatterns(minNote, maxNote, maxLength):
    singleNotes=[]
    ascendingNoteScales=[]
    allNotePatterns=[]
    notes = []

    # One note options
    for i in range(minNote, maxNote):
        notes = [i]
        singleNotes.append(notes)

    # Ascending scalar options
    for i in range(minNote + 1, maxNote + 1):
        notes = []
        for j in range(1, i+1):
            notes.append(j)
        if notes:
            ascendingNoteScales.append(notes)

    # All descending scalar patterns
    descendingNoteScales = [x[::-1] for x in ascendingNoteScales]

    # All descending and ascending scalar patterns
    ascendingDescendingScaleNotes = []
    for i in range(len(ascendingNoteScales)):
        combinedPattern = ascendingNoteScales[i] + descendingNoteScales[i][1:]
        ascendingDescendingScaleNotes.append(combinedPattern)

    descendingAscendingNoteScales = []
    for i in range(len(ascendingNoteScales)):
        combinedPattern = descendingNoteScales[i] + ascendingNoteScales[i][1:]
        descendingAscendingNoteScales.append(combinedPattern)

    allNotePatterns = [{"notePatternType": "scale",
                        "scaleNotePatterns": {"singleNotes": singleNotes,
                                               "ascendingScaler": ascendingNoteScales,
                                               "descendingScaler": descendingNoteScales,
                                               "ascendingDescendingScaler": ascendingDescendingScaleNotes,
                                               "descendingAscendingScaler": descendingAscendingNoteScales}}]
    return allNotePatterns


def main():
    minNote = 1
    maxNote = 9
    maxLength = 2 * (maxNote)
    print(notePatterns(minNote, maxNote, maxLength))

if __name__ == '__main__':
    main()