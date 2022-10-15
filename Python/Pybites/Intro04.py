MESSAGE = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=MESSAGE):
    lines = message.split("\n")
    joined = "|".join(lines)
    return(joined)
    pass



split_in_columns(MESSAGE)

