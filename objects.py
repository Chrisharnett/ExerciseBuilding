import abjad
import os

class Exercise:
    def __init__(self, pattern, key="g", mode="major"):
        self.__pattern = pattern
        self.__key = key
        self.__mode = mode
        self.__score = self.buildScore()

    def buildScore(self):
        container = abjad.Container("")
        match self.__mode:
            case "major":
                scale = Scale(self.__key + "'", self.__mode)
                scaleNotes = scale.makeScale()
                for note in self.__pattern.get("notePattern"):
                    if isinstance(note[0], int):
                        container.append(self.containerize(scaleNotes, note))
                    elif note[0] == "repeat":
                        notes = ""
                        for n in note[1:]:
                            notes += self.containerize(scaleNotes, n)
                        c = abjad.Container(notes)
                        r = abjad.Repeat()
                        abjad.attach(r, c)
                        container.append(c)
            case _:
                return "Scale building error"

        bar_line = abjad.BarLine("|.")
        abjad.attach(bar_line, container[-1])
        voice = abjad.Voice([container], name="Exercise_Voice")
        staff = abjad.Staff([voice], name="Exercise_Staff")
        score = abjad.Score([staff], name="Score")

        time_signature = abjad.TimeSignature(self.__pattern.get("timeSignature"))
        abjad.attach(time_signature, container[0], context="Score")

        return score

    def containerize(self, scaleNotes, note):
        pitch = scaleNotes[note[0] - 1]
        n = pitch.get_name() + note[1] + " "
        return n

    def getImage(self):
        preambleBlock = abjad.Block("context", items=[self.__pattern.get("preamble")])
        lilypond_file = abjad.LilyPondFile([preambleBlock, self.__score])

        abjad.persist.as_png(lilypond_file, os.path.join("static/img/" + self.__pattern.get("name") + ".png"),
                             flags="-dcrop", resolution=300)

        return os.path.join("static/img/" + self.__pattern.get("name") + ".cropped.png")

    def getName(self):
        return self.__pattern.get("name")

    def getDescription(self):
        return self.__pattern.get("description")

class Instrument:
    def __init__(self, name, lowNote="bes", highNote="f''"):
        self.__name = name
        self.__lowNote = lowNote
        self.__highNote = highNote

class Scale:
    def __init__(self, tonic, mode):
        self.__tonic = tonic
        self.__mode = mode

    def getIntervals(self):
        match self.__mode:
            case "major":
                intervals = "M2 M2 m2 M2 M2 M2 m2".split()
                intervals = [abjad.NamedInterval(_) for _ in intervals]
            case _:
                intervals = "not found"
        return intervals

    def makeScale(self):
        pitches = []
        pitch = abjad.NamedPitch(self.__tonic)
        pitches.append(pitch)
        for interval in self.getIntervals():
            pitch = pitch + interval
            pitches.append(pitch)
        return pitches

