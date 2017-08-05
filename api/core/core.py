
from models.music.midi_engine import MidiEngine


def create_midi_file(seed_data, target_field):
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


