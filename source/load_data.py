import numpy as np

def load_data(file_path):
    # names=True liest die Header-Zeile automatisch
    # encoding='utf-8-sig' hilft bei seltsamen Zeichen am Anfang der Datei
    data = np.genfromtxt(file_path, delimiter=',', names=True, 
                        filling_values=0, encoding='utf-8-sig')
    
    # Packt jede Spalte in eine Variable im Dictionary
    return {name: data[name] for name in data.dtype.names}