import io

def font_to_bytes(font) -> io.BytesIO:
    # Abre el archivo TTF en modo lectura binaria
    with open(font, 'rb') as f:
        # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    # Crea un objeto BytesIO a partir de los bytes del archivo TTF
    return io.BytesIO(ttf_bytes)