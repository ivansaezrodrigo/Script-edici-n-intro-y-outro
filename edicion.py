import moviepy
import moviepy.editor as mp
from random import randint
import time
import sys

title_font = 'Arial'
fade_in_time = 0.5 # seconds
fade_out_time = 0.5 # seconds

video_fps = 25

video_codec = 'libx264'

video_title = 'Prueba Script'

start_time = time.time() # take the time at the beginning to calculate the total time processing.

bg_music_files = ['Leaving the city']

number_of_clips = 0

clip1 = mp.VideoFileClip('./Intro y Outro/intro.mp4').set_start(0).audio_fadein(fade_in_time).audio_fadeout(1).fadein(fade_in_time).fadeout(fade_out_time)
clip2 = mp.VideoFileClip('./Videos sin editar/Sincronización.mp4').set_start(0).audio_fadein(fade_in_time).audio_fadeout(1).fadein(fade_in_time).fadeout(fade_out_time)
clip3 = mp.VideoFileClip('./Intro y Outro/outro.mp4').set_start(0).audio_fadein(fade_in_time).audio_fadeout(1).fadein(fade_in_time).fadeout(fade_out_time)

video = mp.concatenate_videoclips([clip1,clip2,clip3])

music_length = 0
bg_music_clips = []

#title = mp.TextClip(video_title, font= title_font, color='white', fontsize=40,align='West')
#title_col = title.on_color(size=(video.w ,title.h+10),
#                 color=(0,0,0), pos=(6,'center'), col_opacity=0.3)
#title_mov = title_col.set_pos( lambda t: (max(video.w/30,int(video.w-0.5*video.w*t)),
#                                  max(5*video.h/6,int(100*t))) )

#logo = (mp.ImageClip("logo.png")
#          .set_duration(video.duration)
#          .resize(height=70) # if you need to resize...
#          .margin(right=10, bottom=10, opacity=0)
#          .set_pos(("right","bottom")))

#final = mp.CompositeVideoClip([video,title_mov])
#final = mp.CompositeVideoClip([video,title_mov,logo])
print(video.duration)
#final.subclip(0,30).write_videofile("test.mp4",fps=VIDEO_FPS, codec=VIDEO_CODEC)

#video.subclip(0,video.duration).write_videofile(video_title+".mp4",fps=video_fps, codec=video_codec, verbose=False, logger=None)
video.subclip(0,video.duration).write_videofile(video_title+".mp4",fps=video_fps, codec=video_codec, verbose=False)

endTime = time.time()
print("Procesing time: " +str(endTime - start_time))