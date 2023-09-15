import io

def font_to_bytes(font) -> io.BytesIO:
    """
    Convert a TrueType font file to bytes and store it in a BytesIO object.

    This function takes the path to a TrueType font file, reads all its bytes in binary mode,
    and then creates a BytesIO object from those bytes.

    :param font: The path to the TrueType font file.
    :type font: str
    :return: A BytesIO object containing the font data.
    :rtype: io.BytesIO
    """
    # Open the TTF file in binary read mode
    with open(font, 'rb') as f:
        # Read all the bytes from the file and store them in a variable
        ttf_bytes = f.read()
    # Create a BytesIO object from the TTF file bytes
    return io.BytesIO(ttf_bytes)
