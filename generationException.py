class LengthException(Exception):
    def __str__(self):
        return "Length could not be under 5 characters"\
        " or over 64"