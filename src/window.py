from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

from app import App
from track_frame import TrackFrame
import utils

class Ui_MainWindow(object):
    """
    UI setup functions
    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1112, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("color: white;")

        # The main view that contains everything
        self.mainView = QtWidgets.QWidget(MainWindow)
        self.mainView.setAutoFillBackground(False)
        self.mainView.setObjectName("mainView")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainView)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Contains the side-menu and the list-view
        self.setupContentView()
        self.verticalLayout.addWidget(self.contentView)

        # Media player controls
        self.setupMediaPlayerView()
        self.verticalLayout.addWidget(self.mediaPlayerView)
        MainWindow.setCentralWidget(self.mainView)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.player = QtMultimedia.QMediaPlayer(None)
        self.playerDuration = 0

        self.ConnectEvents()

        App.init()
        self.LoadTracks()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Player"))
        self.btnChooseFolder.setText(_translate("MainWindow", "Choose Music Folder"))
        self.mediaPlayerLabelTimeStamp.setText(_translate("MainWindow", "00:00"))
        self.mediaPlayerLabelLength.setText(_translate("MainWindow", "00:00"))
    
    def setupContentView(self):
        self.contentView = QtWidgets.QFrame(self.mainView)
        self.contentView.setStyleSheet("")
        self.contentView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contentView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentView.setObjectName("contentView")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.contentView)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # The side-menu that has a list of buttons to swap between views and choose the musics folder
        self.setupSideMenu()
        self.horizontalLayout.addWidget(self.sideMenu)

        # The list-view that contains all the tracks from the chosen directory
        self.setupListView()
        self.horizontalLayout.addWidget(self.listView)

    def setupSideMenu(self):
        self.sideMenu = QtWidgets.QFrame(self.contentView)
        self.sideMenu.setMinimumSize(QtCore.QSize(300, 0))
        self.sideMenu.setStyleSheet("background-color: #2B2B2B")
        self.sideMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sideMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideMenu.setObjectName("sideMenu")

        self.btnChooseFolder = QtWidgets.QPushButton(self.sideMenu)
        self.btnChooseFolder.setGeometry(QtCore.QRect(10, 10, 281, 31))
        self.font = QtGui.QFont()
        self.font.setFamily("Yu Gothic UI Semibold")
        self.font.setPointSize(12)
        self.btnChooseFolder.setFont(self.font)
        self.btnChooseFolder.setStyleSheet("")
        self.btnChooseFolder.setObjectName("btnChooseFolder")

    def setupListView(self):
        self.listView = QtWidgets.QScrollArea(self.contentView)
        self.listView.setStyleSheet("background-color: black")
        self.listView.setWidgetResizable(True)
        self.listView.setObjectName("listView")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 808, 476))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.track_list_view_container = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.track_list_view_container.setAlignment(QtCore.Qt.AlignTop)
        self.track_list_view_container.setObjectName("track_list_view_container")
        self.track_list_view_container.setContentsMargins(15, 15, 15, 15)

        self.listView.setWidget(self.scrollAreaWidgetContents)

        lbl = QtWidgets.QLabel("Music")
        lbl.setFont(self.font)
        self.track_list_view_container.addWidget(lbl)

    def setupMediaPlayerView(self):
        self.mediaPlayerView = QtWidgets.QFrame(self.mainView)
        self.mediaPlayerView.setMinimumSize(QtCore.QSize(0, 120))
        self.mediaPlayerView.setMaximumSize(QtCore.QSize(16777215, 120))
        self.mediaPlayerView.setStyleSheet("background-color: #0B263B")
        self.mediaPlayerView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mediaPlayerView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mediaPlayerView.setObjectName("mediaPlayerView")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mediaPlayerView)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.mediaPlayer = QtWidgets.QFrame(self.mediaPlayerView)
        self.mediaPlayer.setMinimumSize(QtCore.QSize(500, 0))
        self.mediaPlayer.setMaximumSize(QtCore.QSize(500, 16777215))
        self.mediaPlayer.setStyleSheet("")
        self.mediaPlayer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mediaPlayer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mediaPlayer.setObjectName("mediaPlayer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mediaPlayer)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.mediaPlayerButtons = QtWidgets.QFrame(self.mediaPlayer)
        self.mediaPlayerButtons.setMinimumSize(QtCore.QSize(0, 78))
        self.mediaPlayerButtons.setStyleSheet("red")
        self.mediaPlayerButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mediaPlayerButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mediaPlayerButtons.setObjectName("mediaPlayerButtons")
        self.btnPlayPause = QtWidgets.QPushButton(self.mediaPlayerButtons)
        self.btnPlayPause.setGeometry(QtCore.QRect(224, 14, 50, 50))
        self.btnPlayPause.setStyleSheet("QPushButton {\n"
                "    border-style: solid;\n"
                "    border-color: white;\n"
                "    border-width: 3px;\n"
                "    border-radius: 25%;\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color: rgba(240, 240, 240, 100);\n"
                "}")
        self.btnPlayPause.setText("")
        self.btnPlayPause.setObjectName("btnPlayPause")
        self.btnShuffle = QtWidgets.QPushButton(self.mediaPlayerButtons)
        self.btnShuffle.setGeometry(QtCore.QRect(120, 18, 41, 41))
        self.btnShuffle.setStyleSheet("QPushButton {\n"
                "    border-style: solid;\n"
                "    border-color: white;\n"
                "    border-width: 3px;\n"
                "    border-radius: 20%;\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: rgba(240, 240, 240, 100);\n"
                "}")
        self.btnShuffle.setText("")
        self.btnShuffle.setObjectName("btnShuffle")
        self.btnPrev = QtWidgets.QPushButton(self.mediaPlayerButtons)
        self.btnPrev.setGeometry(QtCore.QRect(170, 18, 41, 41))
        self.btnPrev.setStyleSheet("QPushButton {\n"
                "    border-style: solid;\n"
                "    border-color: white;\n"
                "    border-width: 3px;\n"
                "    border-radius: 20%;\n"
                "}\n"
                "\n"
                "QPushButton:hover {\n"
                "    background-color: rgba(240, 240, 240, 100);\n"
                "}")
        self.btnPrev.setText("")
        self.btnPrev.setObjectName("btnPrev")
        self.btnNext = QtWidgets.QPushButton(self.mediaPlayerButtons)
        self.btnNext.setGeometry(QtCore.QRect(286, 18, 41, 41))
        self.btnNext.setStyleSheet("QPushButton {\n"
                "    border-style: solid;\n"
                "    border-color: white;\n"
                "    border-width: 3px;\n"
                "    border-radius: 20%;\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: rgba(240, 240, 240, 100);\n"
                "}")
        self.btnNext.setText("")
        self.btnNext.setObjectName("btnNext")
        self.btnLoop = QtWidgets.QPushButton(self.mediaPlayerButtons)
        self.btnLoop.setGeometry(QtCore.QRect(336, 18, 41, 41))
        self.btnLoop.setStyleSheet("QPushButton {\n"
                "    border-style: solid;\n"
                "    border-color: white;\n"
                "    border-width: 3px;\n"
                "    border-radius: 20%;\n"
                "}\n"
                "QPushButton:hover {\n"
                "    background-color: rgba(240, 240, 240, 100);\n"
                "}")
        self.btnLoop.setText("")
        self.btnLoop.setObjectName("btnLoop")
        self.verticalLayout_3.addWidget(self.mediaPlayerButtons)
        self.sliderBarContainer = QtWidgets.QFrame(self.mediaPlayer)
        self.sliderBarContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sliderBarContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sliderBarContainer.setObjectName("sliderBarContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.sliderBarContainer)
        self.horizontalLayout_3.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mediaPlayerLabelTimeStamp = QtWidgets.QLabel(self.sliderBarContainer)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        self.mediaPlayerLabelTimeStamp.setFont(font)
        self.mediaPlayerLabelTimeStamp.setStyleSheet("")
        self.mediaPlayerLabelTimeStamp.setAlignment(QtCore.Qt.AlignCenter)
        self.mediaPlayerLabelTimeStamp.setObjectName("mediaPlayerLabelTimeStamp")
        self.horizontalLayout_3.addWidget(self.mediaPlayerLabelTimeStamp)

        self.slider = QtWidgets.QSlider(self.sliderBarContainer)
        self.slider.setFixedWidth(367)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: none;
                height: 2px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
                background: white;
                margin: 2px 0;
            }

            QSlider::handle:horizontal {
                background: #0B263B;
                border: 2px solid white;
                width: 12px;
                margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
                border-radius: 7px;
                margin: -7px 0;
            }
        """)
        self.sliderIsPressed = False
        self.sliderPosition = 0
        self.horizontalLayout_3.addWidget(self.slider)

        self.mediaPlayerLabelLength = QtWidgets.QLabel(self.sliderBarContainer)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(12)
        self.mediaPlayerLabelLength.setFont(font)
        self.mediaPlayerLabelLength.setAlignment(QtCore.Qt.AlignCenter)
        self.mediaPlayerLabelLength.setObjectName("mediaPlayerLabelLength")
        self.horizontalLayout_3.addWidget(self.mediaPlayerLabelLength)
        self.verticalLayout_3.addWidget(self.sliderBarContainer)

        self.horizontalLayout_2.addWidget(self.mediaPlayer)

    def ConnectEvents(self):
        self.btnChooseFolder.clicked.connect(self.OnChooseFolder)
        self.btnPlayPause.clicked.connect(self.OnPlayPause)

        # QMediaPlayer events
        self.player.stateChanged.connect(self.OnStateChange)
        self.player.positionChanged.connect(self.OnPositionChange)
        self.player.durationChanged.connect(self.OnDurationChange)

        # QSlider events
        self.slider.sliderPressed.connect(self.OnSliderPressed)
        self.slider.sliderReleased.connect(self.OnSliderRelease)
        self.slider.sliderMoved.connect(self.OnSliderMove)       

    def LoadTracks(self):
        # Clear the track_list
        App.clear_track_list()

        # For every directory inside the settings.pkl file load in the tracks
        track_list = utils.get_tracks_from_multiple_directories(App.track_dirs)

        # Clear the track_list_view_container
        for i in reversed(range(1, self.track_list_view_container.count())):
            self.track_list_view_container.itemAt(i).widget().setParent(None)

        # This keeps track of the initial letter of the track
        initial = ""
        counter = 0
        # Add in all the tracks found inside the folder
        for track in track_list:
            track_dir = track["dirpath"]
            track_name = track["filename"]

            # If there is a new initial letter put in a label
            if initial != track_name[0].upper():
                # First add a spacer to distinguish between each group
                spacer = QtWidgets.QLabel("")
                spacer.setFixedHeight(10)
                self.track_list_view_container.addWidget(spacer)

                # Add in the label
                initial = track_name[0].upper()
                labelInitial = QtWidgets.QLabel(track_name[0].upper())
                font_size = self.font.pointSize()
                self.font.setPointSize(16)
                labelInitial.setFont(self.font)
                self.font.setPointSize(font_size)
                labelInitial.setStyleSheet("""
                    QLabel{
                        color: #3C8FCF
                    }
                """)
                self.track_list_view_container.addWidget(labelInitial)

            # Create a frame to store the information about the track
            # On every odd frame change the background-color to a different one 
            # for visibility reasons
            bg_color = "#000000"
            if counter % 2 == 1:
                bg_color = "#252525"
            print(counter)
            frame = TrackFrame(self.player, track_name, track_dir, self.font, counter, bg_color)

            self.track_list_view_container.addWidget(frame)
            counter += 1

    """
    Side menu button events
    """
    def OnChooseFolder(self):
        # Choose the folder
        folder_dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Select music folder", "")
        # Add the folder into the list of track directories
        App.add_track_dir(folder_dir)
        # Load the tracks
        self.LoadTracks()

    """
    Media player button events
    """
    def OnPlayPause(self):
        if self.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()
    
    """
    QMediaPlayer event events
    """
    def OnTrackEnd(self):
        next_track = App.get_next_track()
        media = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(next_track))
        self.player.setMedia(media)
        self.player.play()
    def OnPositionChange(self, position):
        if position == self.playerDuration and position != 0:
            self.OnTrackEnd()
        if self.sliderIsPressed:
            return
        self.slider.setValue(position)
        self.mediaPlayerLabelTimeStamp.setText(utils.convert_miliseconds(position))
    def OnDurationChange(self, duration):
        self.playerDuration = duration
        self.slider.setRange(0, duration)
        self.mediaPlayerLabelLength.setText(utils.convert_miliseconds(duration))
    def OnStateChange(self, state):
        if self.player.state() == QtMultimedia.QMediaPlayer.PlayingState:
            # Change the play/pause button icon
            pass
        else:
            # Change the play/pause button icon
            pass

    """
    QSlider event events
    """
    def OnSliderPressed(self):
        self.sliderIsPressed = True
    def OnSliderRelease(self):
        self.sliderIsPressed = False
        self.player.setPosition(self.sliderPosition)
    def OnSliderMove(self, position):
        self.sliderIsPressed = True
        self.mediaPlayerLabelTimeStamp.setText(utils.convert_miliseconds(position))
        self.sliderPosition = position