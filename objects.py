import math

import abjad
import os

class Pattern:
    def __init__(self, patternId, patternType, notePattern, preamble, description="",
                 timesSignature=(4, 4), rhythm="", articulation="", dynamic=""):
        self.__patternId = patternId
        self.__patternType = patternType
        self.__notePattern = notePattern
        self.__preamble = preamble
        self.__description = description
        self.__rhythm = rhythm
        self.__articulation = articulation
        self.__dynamic = dynamic
        self.__timeSignature = timesSignature

    @property
    def getPatternId(self):
        return self.__patternId

    @property
    def getPatternType(self):
        return self.__patternType

    @property
    def getNotePattern(self):
        return self.__notePattern

    @property
    def getPreamble(self):
        return self.__preamble

    @property
    def getDescription(self):
        return self.__description

    @property
    def getRhythm(self):
        return self.__rhythm

    @property
    def getArticulation(self):
        return self.__articulation

    @property
    def getDynamic(self):
        return self.__dynamic

    @property
    def getTimeSignature(self):
        return self.__timeSignature

    def __str__(self):
        name = str(self.__patternId) + "_"
        if self.__rhythm != "":
            name += self.__rhythm + "_"
        name += self.__patternType
        return name


class Exercise(Pattern):
    def __init__(self, exerciseId, pattern, key="g", mode="major", direction=""):
        super().__init__(pattern.getPatternId, pattern.getPatternType, pattern.getNotePattern,
                         pattern.getPreamble, pattern.getDescription,
                         pattern.getTimeSignature, pattern.getRhythm, pattern.getArticulation,
                         pattern.getDynamic)
        self.__exerciseId = exerciseId
        self.__key = key
        self.__mode = mode
        self.__direction = direction
        self.__score = self.buildScore()
        self.__image = self.imageURL()

    @property
    def getKey(self):
        return self.__key

    @property
    def getMode(self):
        return self.__mode

    @property
    def getImage(self):
        return self.__image

    @property
    def getDirection(self):
        return self.__direction

    def __str__(self):
        name = self.__key + "_" + self.__mode + "_"
        if self.getRhythm != "":
            name += self.getRhythm + "_"
        name += self.getPatternType + "_"
        if self.getDirection != "":
            name += self.getDirection + "_"
        if self.getArticulation != "":
            name += self.getArticulation + "_"
        if self.getDynamic != "":
            name += self.getDynamic
        return name

    def buildScore(self):
        container = abjad.Container("")
        scaleNotes = self.getScaleNotes()

        for note in self.getNotePattern:
            if isinstance(note[0], int):
                container.append(self.numberToNote(scaleNotes, note))
            elif note[0] == "r":
                container.append(note)
            elif note[0] == "repeat":
                notes = ""
                for n in note[1:]:
                    if isinstance(n[0], int):
                        notes += self.numberToNote(scaleNotes, n)
                    else:
                        notes += n[0]
                c = abjad.Container(notes)
                r = abjad.Repeat()
                abjad.attach(r, c)
                container.append(c)
        attachHere = ""
        if len(container) >= 1:
            attachHere = container[0][0]
        # elif len(container) > 1:
        #     attachHere = container[0][0]
        if attachHere != "":
            keySignature = abjad.KeySignature(
                abjad.NamedPitchClass(self.__key), abjad.Mode(self.__mode))
            abjad.attach(keySignature, attachHere)
            timeSignature = abjad.TimeSignature(self.getTimeSignature)
            abjad.attach(timeSignature, attachHere)
            if not abjad.get.indicators(container[-1], abjad.Repeat):
                bar_line = abjad.BarLine("|.")
                abjad.attach(bar_line, container[-1])

        voice = abjad.Voice([container], name="Exercise_Voice")
        staff = abjad.Staff([voice], name="Exercise_Staff")
        score = abjad.Score([staff], name="Score")
        return score

    def getScaleNotes(self):
        scale = Scale(self.__key + "'", self.__mode)
        scaleNotes = scale.makeScale()
        return scaleNotes

    def numberToNote(self, scaleNotes, note):
        noteNumber = (note[0] % 7)
        noteOctave = math.floor(note[0]/8)
        pitch = scaleNotes[noteNumber - 1]
        if 0 < noteOctave:
            octave = abjad.NamedInterval(("+P" + (str(7 + noteOctave))))
            pitch += octave
        pitchName = pitch.get_name()
        n = pitchName + note[1] + " "

        return n

    def imageURL(self):
        preambleBlock = abjad.Block("context", items=[self.getPreamble])
        lilypond_file = abjad.LilyPondFile([preambleBlock, self.__score])
        namePath = os.path.join("static/img/" + str(self.__exerciseId) + str(self))
        abjad.persist.as_png(lilypond_file, namePath + ".png",
                             flags="-dcrop", resolution=300)
        path = namePath + ".cropped.png"

        return path


class Instrument:
    def __init__(self, name, lowNote="bes", highNote="f''"):
        self.__name = name
        self.__lowNote = lowNote
        self.__highNote = highNote

class Scale:
    def __init__(self, tonic, mode):
        self.__tonic = tonic
        self.__mode = mode

    def getPitches(self):
        pitchSets = {
            "major": [0, 2, 4, 5, 7, 9, 11]
        }

        return pitchSets

    def makeScale(self):
        pitches = []
        tonic = abjad.NamedPitch(self.__tonic)
        for scalePitch in self.getPitches()[self.__mode]:
            pitch = tonic + scalePitch
            pitches.append(pitch)
        return pitches

