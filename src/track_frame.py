from PyQt5.QtWidgets import QFrame, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent

from app import App

class TrackFrame(QFrame):
    def __init__(self, player, track_name, track_dir, font, id, bg_color="#000000"):
        super(TrackFrame, self).__init__()
        self.id = id

        self.setStyleSheet("""
            QFrame{
                background-color:"""
                + bg_color + """;
            }
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 10, 7, 10)
        label_track_name = QLabel(track_name)
        label_track_name.setFont(font)
        layout.addWidget(label_track_name, 0, Qt.AlignLeft)

        playButton = QPushButton()
        playButton.setText("Play")
        playButton.setFont(font)
        playButton.setFixedSize(50, 30)
        playButton.clicked.connect(lambda: self.OnPlayTrack(track_dir, player))
        playButton.setStyleSheet("""
            QPushButton::hover {
                background-color: rgb(125, 125, 125)
            }
        """)
        layout.addWidget(playButton)

        App.add_tracks_to_track_list([track_dir])

    def OnPlayTrack(self, track_dir, player):
        App.start_playlist_from_track(self.id)
        media = QMediaContent(QUrl.fromLocalFile(track_dir))
        player.setMedia(media)
        player.play()
