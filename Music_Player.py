from GUI_source import *
class MusicPlayer():
    def __init__(self, music_loc):
        # Sets up mediaplayer with audio file specified by music_loc
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile(music_loc))

    def play_BGM(self):
        # Volume ranges from 0 to 1 and is proportion of base volume
        # Fades audio in and out
        self.player.setLoops(BGM_LOOPS)
        self.audio_output.setVolume(BGM_VOL)
        self.player.play()