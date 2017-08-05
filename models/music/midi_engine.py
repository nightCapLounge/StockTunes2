
import random, copy, json
import mido as midi
import base64 as b64
import models.music.facts as facts
import io

class MidiEngine(object):
    """
        MidiEngine

        Description:
            Ingests an array of seed data and generates MIDI data
            based on that data.

            To use, simply construct with seed data and optional target field,
            then call MidiEngine::Run(). Once finished, query for the midi_file
            attribute to get the end result.

            Currently, music key defaults to C Minor.  
        
        Model Description:
            This is a random gen model.  It simply uses a single field from the seed
            data to create a harmonic map.  If the field goes up, 
            then a major chord is randomly selected.  If the field goes down 
            or is equal a minor chord is selected. 

            The primary tones of the selected chords are then selected and their exact 
            identity is randomly chosen (the octave).

            The result is written to a byte buffer instead of to disk to minimize 
            processing time.  The byte buffer pretends it is a file (a file object in python speak),
            and is used to accept midi data from the Mido library and later to write to 
            http response.

    """

    def __init__(self, seed_data, target_field="Adj Close"):
        """
            MidiEngine::__init__

            Parameters:
                seed_data:list
                    A list of dictionaries containing historical stock data
                target_field
                    The field being targeted by the MIDI Gen model. Defaults
                    to Adjusted Close.

            Returns: None

            Description:
                Constructs the MidiEngine initial state. 

        """
        self.seed_data    = seed_data
        self.target_field = target_field
        self.harmonic_map = []
        self.key          = facts.Key_C_Minor
        self.tone_map     = []
        self.midi_file    = None

    
    def Run(self):
        """
            MidiEngine::Run

            Parameters: None

            Returns: None

            Description:
                Call to generate MIDI file based on seed data.  If called already, 
                call again to regenerate seed data.  

        """
        self.GenerateHarmonicMap()
        self.GenerateToneMap()
        self.GenerateMIDI()


    def GenerateHarmonicMap(self):
        """
            MidiEngine::GenerateHarmonicMap

            Parameters: None

            Returns: None

            Description:
                This creates a harmonic map for tones to be drived from.

                1. Tonic is written to map
                2. Major and minor chords in key are given their own lists
                3. If current data point is greater than or equal to previous data point
                    then a major chord is randomly select.  If less than, a minor chord
                    is randomly selected.  Results are push map.
                4. Map is stored in instance variable.

        """
        # Start off with the root chord
        hmap = [self.key._ChordSequence[0]]

        # Divide chords into major/minor
        major = []
        minor = []
        for chord in self.key._ChordSequence:
            if issubclass(chord, facts.Minor_Chord):
                minor.append(chord)
            elif issubclass(chord, facts.Major_Chord):
                major.append(chord)

        prev = self.seed_data.pop(0)[self.target_field]
        for _ in range(0, len(self.seed_data)):
            designation = major if self.seed_data[0][self.target_field] > prev else minor
            hmap.append(random.choice(designation))
            prev = self.seed_data.pop(0)[self.target_field]

        self.harmonic_map = hmap


    def GenerateToneMap(self):
        """
            MidiEngine::GenerateToneMap

            Parameters: None

            Returns: None

            Description:
                This creates a tone map based on the harmonic map to turn into MIDI.

                1. Iterate over harmonic map and select primary triad of each chord.
                2. Push primary tone lists to tone map. 
                3. Store tone map in instance variable.

        """
        tmap = []
        
        for chord in self.harmonic_map:
            tones = copy.deepcopy(chord._ToneSequence)
            #random.shuffle(tones)
            tmap.append(tones[:3])
        
        self.tone_map = tmap
        print(tmap)


    def GenerateMIDI(self):
        """
            MidiEngine::GenerateMIDI

            Parameters: None

            Returns: None

            Description:
                This takes the tone map and translates it to midi.

                1. For each tone in tone map, replace it with a random MIDI code 
                    designation. e.g. a C can either be 24, 36, 48, etc.
                2. Create a midi file object and a track using Mido library
                3. For each chord (set of related tones), write to midi file as stack
                    of simultaneous tone.  Also turn of previously sounding chord.
                4. Write the resulting file to a byte buffer in memory. 
                5. Save the buffer in an instance variable to be queried later.

        """
        midimap = []
        for seq in self.tone_map:
            new_seq = [random.choice(facts.Tone_MIDI_Mapping[x.value]) for x in seq]
            midimap.append(new_seq)

        outfile = midi.MidiFile()
        track   = midi.MidiTrack()
        track.append(midi.Message('program_change', program=12))

        delta = 1024
        prev  = []
        for seq in midimap:
            if len(prev) > 0:
                track.append(midi.Message('note_off', note=prev[0], velocity=100, time=delta))
                for tone_index in range(1, len(prev)):
                    track.append(midi.Message('note_off', note=prev[tone_index], velocity=100, time=0))  

            for tone_index in range(0, len(seq)):
                track.append(midi.Message('note_on', note=seq[tone_index], velocity=100, time=0))
            
            prev = seq

        outfile.tracks.append(track)
        _buffer = io.BytesIO()
        outfile.save(file=_buffer)
        self.midi_file = _buffer


