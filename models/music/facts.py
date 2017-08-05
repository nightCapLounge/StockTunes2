
"""
    fact.py

    Author:
        Nathaniel Moon
        nathaniel.c.moon@gmail.com
    
    Date:
        2 July 2016

    Description:
        A structured format of music theory in python.
        Still needs some work.

        Think of it as a music theory cheat sheet for python programs

"""


import sys, traceback
from enum import Enum

# -------------------------------------------------------------------------------------
# ---------------------------- Global Use Functions ---------------------------
# -------------------------------------------------------------------------------------

def values(enumList):
    try:
        result = [ item.value for item in enumList ]
        return result
    except ValueError as e:
        Logger.err(e, traceback.format_exc())
        gracefulExit()





# -------------------------------------------------------------------------------------
# ---------------------------- Tone Mapping ---------------------------
# -------------------------------------------------------------------------------------

class Tones(Enum):
    C_DOUBLE_FLAT = 11
    C_FLAT = 12
    C_NATURAL = 1
    C_SHARP = 2
    C_DOUBLE_SHARP = 3
    D_DOUBLE_FLAT = 1
    D_FLAT = 2
    D_NATURAL = 3
    D_SHARP = 4
    D_DOUBLE_SHARP = 5
    E_DOUBLE_FLAT = 3
    E_FLAT = 4
    E_NATURAL = 5
    E_SHARP = 6
    E_DOUBLE_SHARP = 7
    F_DOUBLE_FLAT = 4
    F_FLAT = 5
    F_NATURAL = 6
    F_SHARP = 7
    F_DOUBLE_SHARP = 8
    G_DOUBLE_FLAT = 6
    G_FLAT = 7
    G_NATURAL = 8
    G_SHARP = 9
    G_DOUBLE_SHARP = 10
    A_DOUBLE_FLAT = 8
    A_FLAT = 9
    A_NATURAL = 10
    A_SHARP = 11
    A_DOUBLE_SHARP = 12
    B_DOUBLE_FLAT = 10
    B_FLAT = 11
    B_NATURAL = 12
    B_SHARP = 1
    B_DOUBLE_SHARP = 2


    # Using this get function to numerically reference the enum
    #   effectively get it to imitate a static circularly linked list
    #   Be sure to use this when selecting an enum using a modified index

    @staticmethod
    def get(index):
        try:
            if index < 0: index = 12-abs(index)
            return Tones(((index-1) % 12) + 1)
        except ValueError as e:
            Logger.err(e, traceback.format_exc())
            





# -------------------------------------------------------------------------------------
# ---------------------------- Chord Definitions ---------------------------
# -------------------------------------------------------------------------------------

class ChordMeta(type):
    def __getitem__(cls, index):
        return cls._ToneSequence[index]


class Chord(object):

    __metaclass__ = ChordMeta

    _ToneSequence = []

    @classmethod
    def Triad(cls):
        return cls._ToneSequence[ : 3]



class Major_Chord(Chord):

    @classmethod
    def MajorSeventh(cls):
        return cl[ : 4]

    @classmethod
    def DominantSeventh(cls):
        result = cls[ : 4]
        result[3] = Tones.get(result[3].value-1)
        return result

    @classmethod
    def Ninth(cls):
        return cls[ : 5]

    @classmethod
    def AddNine(cls):
        result = cls.Triad()
        result.append(cls[4])
        return result

    @classmethod
    def Eleventh(cls):
        return cls[ : 6]

    @classmethod
    def AddEleven(cls):
        result = cls.Triad()
        result.append(cls[5])
        return result

    @classmethod
    def Thirteenth(cls):
        return cls[ : 7]

    @classmethod
    def AddThirteen(cls):
        result = cls.Triad()
        result.append(cls[6])
        return result

    @classmethod
    def SusFour(cls):
        result = cls.Triad()
        result[1] = Tones.get(result[1].value+1)
        return result

    @classmethod
    def SusSix(cls):
        result = cls.Triad()
        result[2] = Tones.get(result[2].value+2)
        return result

    @classmethod
    def SusTwo_Three(cls):
        result = cls.Triad()
        result[1] = Tones.get(result[1].value-2)
        return result


class Minor_Chord(Chord):

    @classmethod
    def MajorSeventh(cls):
        result = cls[ : 4]
        result[3] = Tones.get(result[3].value-1)
        return result

    @classmethod
    def MinorSeventh(cls):
        return cls[ : 4]


    @classmethod
    def Ninth(cls):
        return cls[ : 5]

    @classmethod
    def AddNine(cls):
        result = cls.Triad()
        result.append(cls[4])
        return result

    @classmethod
    def Eleventh(cls):
        return cls[ : 6]

    @classmethod
    def AddEleven(cls):
        result = cls.Triad()
        result.append(cls[5])
        return result

    @classmethod
    def Thirteenth(cls):
        return cls[ : 7]

    @classmethod
    def AddThirteen(cls):
        result = cls.Triad()
        result.append(cls[6])
        return result

    @classmethod
    def SusFour(cls):
        result = cls.Triad()
        result[1] = Tones.get(result[1].value+2)
        return result

    @classmethod
    def SusSix(cls):
        result = cls.Triad()
        result[2] = Tones.get(result[2].value+1)
        return result

    @classmethod
    def SusTwo_Three(cls):
        result = cls.Triad()
        result[1] = Tones.get(result[1].value-1)
        return result


class Diminished_Chord(Chord):

    @classmethod
    def Half(cls):
        return cls[ : 4]

    @classmethod
    def Fully(cls):
        result = cls[ : 4]
        result[3] = result[3]-1


class Augmented_Chord(Chord):
    pass






# -------------------------------------------------------------------------------------
# ---------------------------- Chord Identities ---------------------------
# -------------------------------------------------------------------------------------

# ---------------------- Cb ----------------------

class C_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.C_FLAT, 
                        Tones.E_FLAT, 
                        Tones.G_FLAT,
                         Tones.B_FLAT,
                         Tones.D_FLAT,
                         Tones.F_FLAT,
                         Tones.A_FLAT]

class C_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.C_FLAT,
                        Tones.E_DOUBLE_FLAT,
                        Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT,
                        Tones.D_FLAT,
                        Tones.F_FLAT,
                        Tones.A_DOUBLE_FLAT]

class C_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.C_FLAT,
                        Tones.E_DOUBLE_FLAT,
                        Tones.G_DOUBLE_FLAT,
                        Tones.B_DOUBLE_FLAT]

class C_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.C_FLAT,
                        Tones.E_FLAT,
                        Tones.G_NATURAL]



# ---------------------- C ----------------------

class C_Major(Major_Chord):
    _ToneSequence = [Tones.C_NATURAL, 
                        Tones.E_NATURAL, 
                        Tones.G_NATURAL,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_NATURAL]

class C_Minor(Minor_Chord):
    _ToneSequence = [Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_FLAT]

class C_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_FLAT]

class C_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.C_NATURAL,
                        Tones.E_NATURAL,
                        Tones.G_SHARP]



# ---------------------- C# ----------------------

class C_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.C_SHARP,
                        Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_SHARP]

class C_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_NATURAL]

class C_Sharp_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_NATURAL]

class C_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.C_SHARP,
                        Tones.E_SHARP,
                        Tones.G_DOUBLE_SHARP]


# ---------------------- Db ----------------------


class D_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.D_FLAT, 
                        Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_NATURAL, 
                        Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_FLAT]

class D_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.D_FLAT, 
                        Tones.F_FLAT,
                        Tones.A_FLAT,
                        Tones.C_FLAT, 
                        Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT]

class D_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.D_FLAT,
                        Tones.F_FLAT,
                        Tones.A_DOUBLE_FLAT,
                        Tones.C_FLAT]

class D_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.D_FLAT, 
                        Tones.F_NATURAL,
                        Tones.A_NATURAL]


# ---------------------- D ----------------------

class D_Major(Major_Chord):
    _ToneSequence = [Tones.D_NATURAL, 
                        Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_SHARP, 
                        Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_NATURAL]

class D_Minor(Minor_Chord):
    _ToneSequence = [Tones.D_NATURAL, 
                        Tones.F_NATURAL,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL, 
                        Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_FLAT]

class D_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_NATURAL]


class D_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.D_NATURAL,
                        Tones.F_SHARP,
                        Tones.A_SHARP]


# ---------------------- D# ----------------------


class D_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_SHARP,
                        Tones.C_DOUBLE_SHARP,
                        Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_SHARP]

class D_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_NATURAL]

class D_Sharp_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_SHARP]

class D_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_DOUBLE_SHARP]

# ---------------------- Eb ----------------------

class E_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.E_FLAT,
                        Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_NATURAL]

class E_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_FLAT]

class E_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT,
                        Tones.D_FLAT]

class E_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.E_FLAT,
                        Tones.G_NATURAL,
                        Tones.B_NATURAL]

# ---------------------- E ----------------------

class E_Major(Major_Chord):
    _ToneSequence = [Tones.E_NATURAL,
                        Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_SHARP]

class E_Minor(Minor_Chord):
    _ToneSequence = [Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL]

class E_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_NATURAL]

class E_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.E_NATURAL,
                        Tones.G_SHARP,
                        Tones.B_SHARP]

# ---------------------- Fb ----------------------

class E_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.E_SHARP,
                        Tones.G_DOUBLE_SHARP,
                        Tones.B_SHARP,
                        Tones.D_DOUBLE_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_SHARP,
                        Tones.C_DOUBLE_SHARP]

class E_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_SHARP,
                        Tones.C_SHARP]

class E_Sharp_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_SHARP]

class E_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.E_SHARP,
                        Tones.G_DOUBLE_SHARP,
                        Tones.B_DOUBLE_SHARP]

# ---------------------- Fb ----------------------

class F_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.F_FLAT,
                        Tones.A_FLAT,
                        Tones.C_FLAT,
                        Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT,
                        Tones.D_FLAT]

class F_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.F_FLAT,
                        Tones.A_DOUBLE_FLAT,
                        Tones.C_FLAT,
                        Tones.E_DOUBLE_FLAT,
                        Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT,
                        Tones.D_DOUBLE_FLAT]

class F_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.F_FLAT,
                        Tones.A_DOUBLE_FLAT,
                        Tones.C_DOUBLE_FLAT,
                        Tones.E_DOUBLE_FLAT]

class F_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.F_FLAT,
                        Tones.A_FLAT,
                        Tones.C_NATURAL]


# ---------------------- F ----------------------

class F_Major(Major_Chord):
    _ToneSequence = [Tones.F_NATURAL,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_NATURAL]

class F_Minor(Minor_Chord):
    _ToneSequence = [Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_FLAT]

class F_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_FLAT,
                        Tones.E_FLAT]

class F_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.F_NATURAL,
                        Tones.A_NATURAL,
                        Tones.C_SHARP]

# ---------------------- F# ----------------------

class F_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.F_SHARP,
                        Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_SHARP]

class F_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL]

class F_Sharp_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_NATURAL]


class F_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.F_SHARP,
                        Tones.A_SHARP,
                        Tones.C_DOUBLE_SHARP]


# ---------------------- Gb ----------------------

class G_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.G_FLAT,
                        Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_FLAT,
                        Tones.E_FLAT]

class G_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT,
                        Tones.D_FLAT,
                        Tones.F_FLAT,
                        Tones.A_FLAT,
                        Tones.C_FLAT,
                        Tones.E_DOUBLE_FLAT]

class G_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.G_FLAT,
                        Tones.B_DOUBLE_FLAT,
                        Tones.D_DOUBLE_FLAT,
                        Tones.F_FLAT]

class G_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.G_FLAT,
                        Tones.B_FLAT,
                        Tones.D_NATURAL]


# ---------------------- G ----------------------

class G_Major(Major_Chord):
    _ToneSequence = [Tones.G_NATURAL,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_NATURAL]

class G_Minor(Minor_Chord):
    _ToneSequence = [Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_FLAT]

class G_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_NATURAL]

class G_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.G_NATURAL,
                        Tones.B_NATURAL,
                        Tones.D_SHARP]

# ---------------------- G# ----------------------

class G_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.G_SHARP,
                        Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_SHARP]

class G_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_NATURAL]

class G_Sharp_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_SHARP]

class G_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.G_SHARP,
                        Tones.B_SHARP,
                        Tones.D_DOUBLE_SHARP]


# ---------------------- Ab ----------------------

class A_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.A_FLAT,
                        Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_NATURAL,
                        Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_NATURAL]

class A_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.A_FLAT,
                        Tones.C_FLAT,
                        Tones.E_FLAT,
                        Tones.G_FLAT,
                        Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_FLAT]

class A_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.A_FLAT,
                        Tones.C_FLAT,
                        Tones.E_DOUBLE_FLAT,
                        Tones.G_FLAT]

class A_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.A_FLAT,
                        Tones.C_NATURAL,
                        Tones.E_NATURAL]

# ---------------------- A ----------------------

class A_Major(Major_Chord):
    _ToneSequence = [Tones.A_NATURAL,
                        Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_SHARP,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_SHARP]

class A_Minor(Minor_Chord):
    _ToneSequence = [Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_NATURAL,
                        Tones.G_NATURAL,
                        Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL]

class A_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_NATURAL]

class A_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.A_NATURAL,
                        Tones.C_SHARP,
                        Tones.E_SHARP]

# ---------------------- A# ----------------------


class A_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.A_SHARP,
                        Tones.C_DOUBLE_SHARP,
                        Tones.E_SHARP,
                        Tones.G_DOUBLE_SHARP,
                        Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP]

class A_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_SHARP,
                        Tones.G_SHARP,
                        Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_SHARP]

class A_Sharp_Diminished(Diminished_Chord):
   _ToneSequence = [Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_SHARP]

class A_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.A_SHARP,
                        Tones.C_DOUBLE_SHARP,
                        Tones.E_DOUBLE_SHARP]

# ---------------------- Bb ----------------------

class B_Flat_Major(Major_Chord):
    _ToneSequence = [Tones.B_FLAT,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_NATURAL,
                        Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_NATURAL]

class B_Flat_Minor(Minor_Chord):
    _ToneSequence = [Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_NATURAL,
                        Tones.A_FLAT,
                        Tones.C_NATURAL,
                        Tones.E_FLAT,
                        Tones.G_FLAT]

class B_Flat_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.B_FLAT,
                        Tones.D_FLAT,
                        Tones.F_FLAT,
                        Tones.A_FLAT]

class B_Flat_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.B_FLAT,
                        Tones.D_NATURAL,
                        Tones.F_SHARP]


# ---------------------- B ----------------------

class B_Major(Major_Chord):
    _ToneSequence = [Tones.B_NATURAL,
                        Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_SHARP,
                        Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_SHARP]

class B_Minor(Minor_Chord):
    _ToneSequence = [Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_SHARP,
                        Tones.A_NATURAL,
                        Tones.C_SHARP,
                        Tones.E_NATURAL,
                        Tones.G_NATURAL]

class B_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.B_NATURAL,
                        Tones.D_NATURAL,
                        Tones.F_NATURAL,
                        Tones.A_NATURAL]

class B_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.B_NATURAL,
                        Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP]

# ---------------------- B# ----------------------

class B_Sharp_Major(Major_Chord):
    _ToneSequence = [Tones.B_SHARP,
                        Tones.D_DOUBLE_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_DOUBLE_SHARP,
                        Tones.C_DOUBLE_SHARP,
                        Tones.E_SHARP,
                        Tones.G_DOUBLE_SHARP]

class B_Sharp_Minor(Minor_Chord):
    _ToneSequence = [Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_DOUBLE_SHARP,
                        Tones.A_SHARP,
                        Tones.C_DOUBLE_SHARP,
                        Tones.E_SHARP,
                        Tones.G_SHARP]

class B_Sharp_Diminished(Diminished_Chord):
    _ToneSequence = [Tones.B_SHARP,
                        Tones.D_SHARP,
                        Tones.F_SHARP,
                        Tones.A_SHARP]

class B_Sharp_Augmented(Augmented_Chord):
    _ToneSequence = [Tones.B_SHARP,
                        Tones.D_DOUBLE_SHARP,
                        Tones.G_SHARP] # This should be F triple sharp but we don't account for that





# -------------------------------------------------------------------------------------
# ---------------------------- Key Definitions ---------------------------
# -------------------------------------------------------------------------------------


class KeyMeta(type):
    def __getitem__(cls, index):
        return cls._ChordSequence[index]


class Key(metaclass=KeyMeta):

    _ChordSequence = []

    @classmethod
    def Scale(cls):
        return [item[0] for item in cls._ChordSequence]

    @classmethod
    def length(cls):
        return len(cls._ChordSequence)



class Major_Key(Key):
    
    @classmethod
    def Tonic(cls):
        return Key[0]

    @classmethod
    def Dominant(cls):
        return Key[4]


class Minor_Key(Key):

    @classmethod
    def Tonic(cls):
        return super(Minor_Key, cls)[0]

    @classmethod
    def Dominant(cls):
        return Key[4]


# We have the option of expanding this to include modes here


# -------------------------------------------------------------------------------------
# ---------------------------- Key Identities ---------------------------
# -------------------------------------------------------------------------------------


# ---------------------- Cb ----------------------

class Key_C_Flat_Major(Major_Key):
    _ChordSequence = [C_Flat_Major,
                        D_Flat_Minor,
                        E_Flat_Minor,
                        F_Flat_Major,
                        G_Flat_Major,
                        A_Flat_Minor,
                        B_Flat_Diminished]


# ---------------------- C ----------------------


class Key_C_Major(Major_Key):
    _ChordSequence = [C_Major,
                        D_Minor,
                        E_Minor,
                        F_Major,
                        G_Major,
                        A_Minor,
                        B_Diminished]

class Key_C_Minor(Minor_Key):
    _ChordSequence = [C_Minor,
                        D_Diminished,
                        E_Flat_Major,
                        F_Minor,
                        G_Minor,
                        A_Flat_Major,
                        B_Flat_Major]


# ---------------------- C# ----------------------

class Key_C_Sharp_Major(Major_Key):
    _ChordSequence = [C_Sharp_Major,
                        D_Sharp_Minor,
                        E_Sharp_Minor,
                        F_Sharp_Major,
                        G_Sharp_Major,
                        A_Sharp_Minor,
                        B_Sharp_Diminished]

class Key_C_Sharp_Minor(Minor_Key):
    _ChordSequence = [C_Sharp_Minor,
                        D_Sharp_Diminished,
                        E_Major,
                        F_Sharp_Minor,
                        G_Sharp_Minor,
                        A_Major,
                        B_Major]



# ---------------------- Db ----------------------

class Key_D_Flat_Major(Major_Key):
    _ChordSequence = [D_Flat_Major,
                        E_Flat_Minor,
                        F_Minor,
                        G_Flat_Major,
                        A_Flat_Major,
                        B_Flat_Minor,
                        C_Diminished]


# ---------------------- D ----------------------

class Key_D_Major(Major_Key):
    _ChordSequence = [D_Major,
                        E_Minor,
                        F_Sharp_Minor,
                        G_Major,
                        A_Major,
                        B_Minor,
                        C_Sharp_Diminished]


class Key_D_Minor(Minor_Key):
    _ChordSequence = [D_Minor,
                        E_Diminished,
                        F_Major,
                        G_Minor,
                        A_Minor,
                        B_Flat_Major,
                        C_Major]


# ---------------------- D# ----------------------

class Key_D_Sharp_Minor(Minor_Key):
    _ChordSequence = [D_Sharp_Minor,
                        E_Sharp_Diminished,
                        F_Sharp_Major,
                        G_Sharp_Minor,
                        A_Sharp_Minor,
                        B_Major,
                        C_Sharp_Major]


# ---------------------- Eb ----------------------

class Key_E_Flat_Major(Major_Key):
    _ChordSequence = [E_Flat_Major,
                        F_Minor,
                        G_Minor,
                        A_Flat_Major,
                        B_Flat_Major,
                        C_Minor,
                        D_Diminished]


class Key_E_Flat_Minor(Minor_Key):
    _ChordSequence = [E_Flat_Minor,
                        F_Diminished,
                        G_Flat_Major,
                        A_Flat_Minor,
                        B_Flat_Minor,
                        C_Flat_Major,
                        D_Flat_Major]

# ---------------------- E ----------------------

class Key_E_Major(Major_Key):
    _ChordSequence = [E_Major,
                        F_Sharp_Minor,
                        G_Sharp_Minor,
                        A_Major,
                        B_Major,
                        C_Sharp_Minor,
                        D_Sharp_Diminished]


class Key_E_Minor(Minor_Key):
    _ChordSequence = [E_Minor,
                        F_Sharp_Diminished,
                        G_Major,
                        A_Minor,
                        B_Minor,
                        C_Major,
                        D_Major]

# ---------------------- E# ----------------------

    # Nothing to put here

# ---------------------- Fb ----------------------

    # Nothing to put here

# ---------------------- F ----------------------

class Key_F_Major(Major_Key):
    _ChordSequence = [F_Major,
                        G_Minor,
                        A_Minor,
                        B_Flat_Major,
                        C_Major,
                        D_Minor,
                        E_Diminished]


class Key_F_Minor(Minor_Key):
    _ChordSequence = [F_Minor,
                        G_Diminished,
                        A_Flat_Major,
                        B_Flat_Minor,
                        C_Minor,
                        D_Flat_Major,
                        E_Flat_Major]


# ---------------------- F# ----------------------

class Key_F_Sharp_Major(Major_Key):
    _ChordSequence = [F_Sharp_Major,
                        G_Sharp_Minor,
                        A_Sharp_Minor,
                        B_Major,
                        C_Sharp_Major,
                        D_Sharp_Minor,
                        E_Sharp_Diminished]


class Key_F_Sharp_Minor(Minor_Key):
    _ChordSequence = [F_Sharp_Minor,
                        G_Sharp_Diminished,
                        A_Major,
                        B_Minor,
                        C_Sharp_Minor,
                        D_Major,
                        E_Major]

# ---------------------- Gb ----------------------

class Key_G_Flat_Major(Major_Key):
    _ChordSequence = [G_Flat_Major,
                        A_Flat_Minor,
                        B_Flat_Minor,
                        C_Flat_Major,
                        D_Flat_Major,
                        E_Flat_Minor,
                        F_Diminished]


# ---------------------- G ----------------------

class Key_G_Major(Major_Key):
    _ChordSequence = [G_Major,
                        A_Minor,
                        B_Minor,
                        C_Major,
                        D_Major,
                        E_Minor,
                        F_Sharp_Diminished]


class Key_G_Minor(Minor_Key):
    _ChordSequence = [G_Minor,
                        A_Diminished,
                        B_Flat_Major,
                        C_Minor,
                        D_Minor,
                        E_Flat_Major,
                        F_Major]

# ---------------------- G# ----------------------

class Key_G_Sharp_Minor(Minor_Key):
    _ChordSequence = [G_Sharp_Minor,
                        A_Sharp_Diminished,
                        B_Major,
                        C_Sharp_Minor,
                        D_Sharp_Minor,
                        E_Major,
                        F_Sharp_Major]

# ---------------------- Ab ----------------------

class Key_A_Flat_Major(Major_Key):
    _ChordSequence = [A_Flat_Major,
                        B_Flat_Minor,
                        C_Minor,
                        D_Flat_Major,
                        E_Flat_Major,
                        F_Minor,
                        G_Diminished]

class Key_A_Flat_Minor(Minor_Key):
    _ChordSequence = [A_Flat_Minor,
                        B_Flat_Diminished,
                        C_Flat_Major,
                        D_Flat_Minor,
                        E_Flat_Minor,
                        F_Flat_Major,
                        G_Flat_Major]

# ---------------------- A ----------------------

class Key_A_Major(Major_Key):
    _ChordSequence = [A_Major,
                        B_Minor,
                        C_Sharp_Minor,
                        D_Major,
                        E_Major,
                        F_Sharp_Minor,
                        G_Sharp_Diminished]

class Key_A_Minor(Minor_Key):
    _ChordSequence = [A_Minor,
                        B_Diminished,
                        C_Major,
                        D_Minor,
                        E_Minor,
                        F_Major,
                        G_Major]

# ---------------------- A# ----------------------

class Key_A_Sharp_Minor(Minor_Key):
    _ChordSequence = [A_Sharp_Minor,
                        B_Sharp_Diminished,
                        C_Sharp_Major,
                        D_Sharp_Minor,
                        E_Sharp_Minor,
                        F_Sharp_Major,
                        G_Sharp_Major]

# ---------------------- Bb ----------------------

class Key_B_Flat_Major(Major_Key):
    _ChordSequence = [B_Flat_Major,
                        C_Minor,
                        D_Minor,
                        E_Flat_Major,
                        F_Major,
                        G_Minor,
                        A_Diminished]

class Key_B_Flat_Minor(Minor_Key):
    _ChordSequence = [B_Flat_Minor,
                        C_Diminished,
                        D_Flat_Major,
                        E_Flat_Minor,
                        F_Minor,
                        G_Flat_Major,
                        A_Flat_Major]

# ---------------------- B ----------------------

class Key_B_Major(Major_Key):
    _ChordSequence = [B_Major,
                        C_Sharp_Minor,
                        D_Sharp_Minor,
                        E_Major,
                        F_Sharp_Major,
                        G_Sharp_Minor,
                        A_Sharp_Diminished]

class Key_B_Minor(Minor_Key):
    _ChordSequence = [B_Minor,
                        C_Sharp_Diminished,
                        D_Major,
                        E_Minor,
                        F_Sharp_Minor,
                        G_Major,
                        A_Major]

# ---------------------- B# ----------------------

    # Nothing to put here



# -------------------------------------------------------------------------------------
# ---------------------------- Time Signatures ---------------------------
# -------------------------------------------------------------------------------------


class Time_Signature(object):
    pass

class Four_Four(object):
    pass



# -------------------------------------------------------------------------------------
# ---------------------------- Tone to MIDI Mapping ---------------------------
# -------------------------------------------------------------------------------------

class Tone_To_MIDI_Meta(type):
    def __getitem__(cls, index):
        return _Map[index]


Tone_MIDI_Mapping = [
            None,
            [24, 36, 48, 60, 72, 84, 96],       # C
            [25, 37, 49, 61, 73, 85],           # C#
            [26, 38, 50, 62, 74, 86],           # D
            [27, 39, 51, 63, 75, 87],           # D#
            [28, 40, 52, 64, 76, 88],           # E
            [29, 41, 53, 65, 77, 89],           # F
            [30, 42, 54, 66, 78, 90],           # F#
            [31, 43, 55, 67, 79, 91],           # G
            [32, 44, 56, 68, 80, 92],           # G#
            [33, 45, 57, 69, 81, 93],           # A
            [34, 46, 58, 70, 82, 94],           # A#
            [35, 47, 59, 71, 83, 95]            # B
        ]



# -------------------------------------------------------------------------------------
# ---------------------------- Voice Facts ---------------------------
# -------------------------------------------------------------------------------------


class Inst(Enum):

    Soprano = 1
    Alto = 2
    Tenor = 3
    Baritone = 4
    Bass = 5
    Violin = 6
    Viola = 7
    Cello = 8
    Double_Bass = 9
    Banjo = 10
    Guitar = 11
    Harp = 12
    Piccolo = 13
    Flute = 14
    Alto_Flute = 15
    Oboe = 16
    English_Horn = 17
    Clarinet = 18
    Bass_Clarinet = 19
    Bassoon = 20
    Contrabassoon = 21
    Saxophone = 22
    Horn = 23
    C_Trumpet = 24
    Bb_Trumpet = 25
    D_Trumpet = 26
    Eb_Trumpet = 27
    C_Cornet = 28
    Bb_Bass_Trumpet = 29
    Tenor_Trombone = 30
    Bass_Trombone = 31
    Tuba = 32
    #Baritone = 33
    Euphonium = 34
    Timpani = 35
    Xylophone = 36
    Marimba = 37
    Glockenspiel = 38
    Vibraphone = 39
    Chimes = 40
    Piano = 41
    Celesta = 42
    Harpsichord = 43
    Harmonium = 44
    Organ = 45
    Bass_Guitar = 46
    Baritone_Sax = 47
    Tenor_Sax = 48
    Alto_Sax = 49




Instruments = { 0 : [21, 108],
                Inst.Soprano : [60, 81],
                Inst.Alto : [53, 74],
                Inst.Tenor : [48, 69],
                Inst.Baritone : [43, 64],
                Inst.Bass : [42, 62],
                Inst.Violin : [55, 103],
                Inst.Viola : [48, 91],
                Inst.Cello : [36, 76],
                Inst.Double_Bass : [28, 67],
                Inst.Banjo : [],
                Inst.Guitar : [40, 88],
                Inst.Harp : [24, 103],
                Inst.Piccolo : [74, 102],
                Inst.Flute : [60, 96],
                Inst.Alto_Flute : [55, 91],
                Inst.Oboe : [58, 91],
                Inst.English_Horn : [],
                Inst.Clarinet : [50, 94],
                Inst.Bass_Clarinet : [38, 77],
                Inst.Bassoon : [34, 75],
                Inst.Contrabassoon : [22, 53],
                Inst.Saxophone : [],
                Inst.Horn : [34, 77],
                Inst.C_Trumpet : [],
                Inst.Bb_Trumpet : [55, 82],
                Inst.D_Trumpet : [],
                Inst.Eb_Trumpet : [],
                Inst.C_Cornet : [],
                Inst.Bb_Bass_Trumpet : [],
                Inst.Tenor_Trombone : [40, 72],
                Inst.Bass_Trombone : [34, 67],
                Inst.Tuba : [28, 58],
                #Inst.Baritone : [],
                Inst.Euphonium : [],
                Inst.Timpani : [40, 55],
                Inst.Xylophone : [65, 108],
                Inst.Marimba : [45, 96],
                Inst.Glockenspiel : [79, 108],
                Inst.Vibraphone : [53, 89],
                Inst.Chimes : [],
                Inst.Piano : [],
                Inst.Celesta : [60, 108],
                Inst.Harpsichord : [29, 89],
                Inst.Harmonium : [],
                Inst.Organ : [],
                Inst.Bass_Guitar: [38, 67],
                Inst.Baritone_Sax : [36, 69],
                Inst.Tenor_Sax : [44, 76],
                Inst.Alto_Sax : [49, 81] }





# -------------------------------------------------------------------------------------
# ---------------------------- Voice Facts ---------------------------
# -------------------------------------------------------------------------------------


Note_Values = [
    4,      # Whole
    2,      # Half
    1,      # Quarter   
    0.5,    # Eighth
    0.25,   # Sixteenth
    6,      # Dotted Whole
    3,      # Dotted Half
    1.5,    # Dotted Quarter
    0.75    # Dotted Eighth
]

# This can be more efficient
def getClosestNote(CurrentNoteMIDIValue, DesiredNoteName, 
                    InstrumentRange=Instruments[0]):
    closest = sys.maxint
    for val in Tone_MIDI_Mapping[DesiredNoteName.value-1]:

        if val < InstrumentRange[0] or val > InstrumentRange[1]:
            continue

        current = abs(CurrentNoteMIDIValue - closest)
        tmp = abs(CurrentNoteMIDIValue - val)
        if tmp < current:
            closest = val

    return closest



Time_Signatures = {
    "4_4"   : [4, 4],
    "3_4"   : [3, 4],
    "2_4"   : [2, 4],
    "6_8"   : [6, 8]
}




