from pytube import Playlist, YouTube
import os
import sys
import moviepy.editor as moviepy_editor


__author__ = 'PARK4139 : Jung Hoon Park'

def add_sound(vidname, audname, outname, fps=60): 
    my_clip = moviepy_editor.VideoFileClip(vidname)
    audio_background = moviepy_editor.AudioFileClip(audname)
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outname,fps=fps)

def download_clip(url: str):
    yt = YouTube(url)
    path_v = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_video=True)
        .order_by("resolution")
        .desc()
        .first()
        .download(output_path="$only_video/", filename_prefix="")
    )
    path_a = (
        yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True)
        .order_by("abr")
        .desc()
        .first()
        .download(output_path="$only_sound/", filename_prefix="")
    )
    
    add_sound(path_v, path_a, f"storage/{path_v.split('/')[-1]}")


def download_clips(url: str):
    pl = Playlist(url)

    for v in pl.video_urls:
        try:
            download_clip(v)
        except:
            continue


if __name__ == '__main__': 
    # url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ'
    # url = input('다운로드하고 싶은 유튜브 url :  ')
    # url = os.getenv('YOUTUBE_VIDEO')
    url = sys.argv[1]
    
    if not os.path.isdir('./storage'):
        os.system('mkdir "storage"')

    if '&list=' not in url: 
        download_clip(url)
    else:
        download_clips(url)

    os.system('del /f /s "$only_video"')
    os.system('del /f /s "$only_sound"')