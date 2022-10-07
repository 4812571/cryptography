import atheris

with atheris.instrument_imports():
  import sys

def TestOneInput(data):
    if len(data) >= 3:
        if data[0] == ord('b'):
            if data[1] == ord('u'):
                if data[2] == ord('g'):
                    raise Exception("You did it!")

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()