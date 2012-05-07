from PyQt4 import QtGui, uic, QtCore
import os
from PyQt4.QtGui import QMessageBox
from processing.utils import package_slides
from windows.extract_window import ExtractWindow
from windows.load_video_window import LoadVideoWindow
from windows.match_window import MatchWindow
from windows.review_window import ReviewWindow
from windows.sync_window import SyncWindow

form_class, base_class = uic.loadUiType("ui/main_window.ui")
class MainWindow(form_class, base_class):
    # State data
    _video = None
    _slide_crop_box = None      # Crop box for slide video
    _slides = None              # Path to slides
    _video_slides = None        # Slides extracted from video
    _timings = None             # Fixed timings for video

    def __init__(self, app):
        super(base_class, self).__init__()
        self._app = app
        self.setupUi(self)
        self.btnStart.clicked.connect(self._process)

    def _process(self):
        self.btnStart.setEnabled(False)
        self._load_slide_video()
        self._load_slides()
        self._extract_frames()
        self._match_slides()
        self._review_matches()
        self._sync_with_original()
        self._package_slides()
        self.btnStart.setEnabled(True)

    def _load_slide_video(self):
        self._label_set_bold(self.lblLoadSlideVideo, True)
        load_video_win = LoadVideoWindow(self)
        load_video_win.exec_()
        self._video = load_video_win.video
        self._slide_crop_box = load_video_win.selected
        self._label_set_bold(self.lblLoadSlideVideo, False)

    def _load_slides(self):
        self._label_set_bold(self.lblLoadSlides, True)
        dirname = None
        while dirname is None:
            dirname = QtGui.QFileDialog().getExistingDirectory(self, "Open slide directory", QtCore.QDir().homePath())

        dirname = unicode(dirname)  # Convert from QString to unicode string
        image_slides = []
        num = 0
        try:
            for file in sorted(os.listdir(dirname)):
                filename, extension = os.path.splitext(file)
                if extension == ".png":
                    image_slides.append((num, os.path.join(dirname, file)))
                    num += 1
        except IOError as e:
            msgBox = QMessageBox(QMessageBox.Critical, "Error :(", "Video file could not be opened.")
            msgBox.setDetailedText(unicode(e))
            msgBox.exec_()
            return

        self._slides = image_slides
        self._label_set_bold(self.lblLoadSlides, False)

    def _extract_frames(self):
        self._label_set_bold(self.lblExtractFrames, True)
        extract_window = ExtractWindow(self, self._video, self._slide_crop_box, app=self._app)
        extract_window.exec_()
        self._video_slides = extract_window.video_slides
        self._label_set_bold(self.lblExtractFrames, False)

    def _match_slides(self):
        self._label_set_bold(self.lblMatch, True)
        match_window = MatchWindow(self, self._app, self._slides, self._video_slides)
        match_window.show()
        match_window.process()
        self._matches = match_window.matches
        self._label_set_bold(self.lblMatch, False)

    def _review_matches(self):
        self._label_set_bold(self.lblReview, True)
        review_window = ReviewWindow(self, self._slides, self._video_slides, self._matches)
        review_window.show()
        while not review_window.done:
            self._app.processEvents()
        self._matches = review_window.matches
        self._label_set_bold(self.lblReview, False)

    def _sync_with_original(self):
        self._label_set_bold(self.lblSync, True)
        sync_window = SyncWindow(self, self._app, self._video.filepath, self._matches)
        sync_window.show()
        sync_window.process()
        self._synced_slides = sync_window.timings
        self._label_set_bold(self.lblSync, False)

    def _package_slides(self):
        self._label_set_bold(self.lblSave, True)
        filename = None
        while filename is None:
            filename = QtGui.QFileDialog().getSaveFileName(self, "Save file...", QtCore.QDir().homePath(), "Zip files (*.zip)")

        package_slides(unicode(filename), self._synced_slides)
        self._label_set_bold(self.lblSave, False)

    def _label_set_bold(self, label, bold=True):
        font = label.font()
        font.setBold(bold)
        label.setFont(font)