import logging
from pydub import AudioSegment

l = logging.getLogger("pydub.converter")
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

AudioSegment.from_mp3("Mr-Scruff-DJ-Mix-from-London-Koko-Saturday-16th-february-2013-79847030.mp3")
