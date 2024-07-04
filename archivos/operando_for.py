import pathlib

ruta_script = pathlib.Path(__file__).parent 
ruta_archivo = ruta_script / 'mio_amore.txt' 

with open(ruta_archivo,'w', encoding="UTF-8") as archivo: 
    for i in range(10):
        archivo.writelines([f"TE AMO {i} HERMOSA (ﾉ´з｀)ノ♡," "perro culazo (づ ◕‿◕ )づ彡♥ \n"])