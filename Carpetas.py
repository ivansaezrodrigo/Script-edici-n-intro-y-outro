import os

class Carpetas:

    def existe(ruta):
        return os.path.isdir(ruta)           
   
    def crear_carpeta(ruta):
            try:
                if (not Carpetas.existe(ruta)):
                    os.mkdir(ruta)
                    print(f'[✓] Carpeta "{ruta}" creada..')
                    return True
                else:
                    print(f'[✓] Carpeta "{ruta}" existe.')
                    return False
            except:
                print(f'[x] Fallo al crear la carpeta "{ruta}"..')

    def lista_elementos(ruta):
        elementos = os.listdir(ruta)
        return elementos
    
    

    def extension(archivo):
        return archivo.split('.')[1]

    def array_formato(array_archivos,formatos_white_list):
        archivos_no_match = []
        for archivo in array_archivos:
            if (Carpetas.extension(archivo) not in formatos_white_list):
                archivos_no_match.append(archivo)

        return archivos_no_match

    def archivo_formato_video(archivo,extensiones_video = ['avi','mov','mp4']):
        if (Carpetas.extension(archivo.lower()) in extensiones_video):
            return True
        else:
            print(f'[x] La extensión del archivo "{archivo}" no es reconocida como formato de video.')
            return False
        
    def array_formato_video(array,extensiones_video = ['avi','mov','mp4']):
        videos_no_match = Carpetas.array_formato(array,extensiones_video)
        if(len(videos_no_match) == 0):
            return True
        else:
            print(f'[x] "',videos_no_match.join(','),'" no son formatos reconocidos.')
            return False        
