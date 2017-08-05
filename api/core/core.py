
from models.music.midi_engine import MidiEngine


def create_midi_file(seed_data, target_field):
    """
        create_midi_file

        Parameters:
            seed_data:array
                An array of dicts containing historical stock data
            target_field:string
                The field in the historical data being used for generating
                music

        Returns:
            A dictionary with errors and the resulting "midi file" (actually a byte buffer)

        Description:
            Takes in seed data and a target field, and requests a midi file from the MidiEngine

    """
    result = {
        "errors" : [],
        "file": None
    }
    me = MidiEngine(seed_data, target_field)
    me.Run()
    if me.midi_file is None:
        result["errors"].append("MIDI generation was unsuccessful")
    else:
        result["file"] = me.midi_file

    return result


