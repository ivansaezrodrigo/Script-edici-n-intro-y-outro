import moviepy
import moviepy.editor as mp
from random import randint
import time

class Video:

    def __init__(self,intro_route,outro_route,video_route,video_title=""):
        self.video_route = video_route
        self.intro_route = intro_route
        self.outro_route = outro_route
        self.fade_out_time = 0.5 # seconds
        self.fade_in_time = 0.5 # seconds
        self.video_fps = 25
        self.video_codec = 'libx264'
        self.start_time = time.time() # take the time at the beginning to calculate the total time processing.

        self.video_title = video_title
        if video_title == "":
            self.video_title=video_route.split("/")[-1][:-4]

    def render(self):

        clip1 = mp.VideoFileClip(self.intro_route).set_start(0).audio_fadein(self.fade_in_time).audio_fadeout(1).fadein(self.fade_in_time).fadeout(self.fade_out_time)
        clip2 = mp.VideoFileClip(self.video_route).set_start(0).audio_fadein(self.fade_in_time).audio_fadeout(1).fadein(self.fade_in_time).fadeout(self.fade_out_time)
        clip3 = mp.VideoFileClip(self.outro_route).set_start(0).audio_fadein(self.fade_in_time).audio_fadeout(1).fadein(self.fade_in_time).fadeout(self.fade_out_time)

        video = mp.concatenate_videoclips([clip1,clip2,clip3])
        
        print(f'Procesando el video {self.video_title} -> {video.duration}segundos.')
        #final.subclip(0,30).write_videofile("test.mp4",fps=VIDEO_FPS, codec=VIDEO_CODEC)

        #video.subclip(0,video.duration).write_videofile(f"./Videos editados/{self.video_title}.mp4",fps=self.video_fps, codec=self.video_codec, verbose=False, logger=None)
        video.subclip(0,video.duration).write_videofile(f"./Videos editados/{self.video_title}.mp4",fps=self.video_fps, codec=self.video_codec, verbose=False )

        endTime = time.time()
        print(f" {self.video_title} - Procesing time: " +str(endTime - self.start_time))