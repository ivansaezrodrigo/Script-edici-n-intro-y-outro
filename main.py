import os
from Carpetas import *
from Video import *

def existe_intro_outro():
        intro_outro = Carpetas.lista_elementos('Intro y Outro')
        flag_intro = False
        flag_outro = False


        for elemento in intro_outro:
            if elemento.lower().find('intro') == 0:
                if(Carpetas.archivo_formato_video(elemento)):
                    print(f'[✓] Intro encontrada como "{elemento}"')
                    flag_intro = True
            
            if (elemento.lower().find('outro') == 0):
                if(Carpetas.archivo_formato_video(elemento)):
                    print(f'[✓] Outro encontrada como "{elemento}"')
                    flag_outro = True
        
        if (flag_intro and flag_outro):
            return True
        else:
            if(flag_intro == False):
                print('[x] Intro no encontrada')

            if(flag_outro == False):
                print('[x] Outro no encontrada')            
            return False




Carpetas.crear_carpeta('Intro y Outro')
Carpetas.lista_elementos('Intro y Outro')

existe_intro_outro()

Carpetas.crear_carpeta('Videos editados')
   
Carpetas.crear_carpeta('Videos sin editar')

print(f'[*] Listando "Videos sin editar"..\n')
videos_sin_editar =  Carpetas.lista_elementos('Videos sin editar')

if(not Carpetas.array_formato_video(videos_sin_editar)):
    exit()


for video in videos_sin_editar:
    #print(video)
    obj = Video('./Intro y Outro/intro.mp4','./Intro y Outro/outro.mp4',f'./Videos sin editar/{video}')
    obj.render()



print('\nFin')
