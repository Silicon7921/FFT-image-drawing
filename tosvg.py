'''
DO NOT PUT THE OUTPUT DIRECTLY INTO PATH.TXT
THE OUTPUT CONTAINS DATA WHICH CANNOT BE PARSED BY FOURIER.PY
YOU SHOULD PROCESS THE OUTPUT MANUALLY
'''

from typing import Iterable, List, Union
import sys, cv2
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget ,QMessageBox

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # init main window
        self.setWindowTitle("Simple SVG Generator")
        self.setGeometry(100, 100, 200, 200)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        # select file button
        self.btn_select_file = QPushButton("Input Bitmap...", self)
        self.btn_select_file.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select_file)
        # select output button
        self.btn_select_folder = QPushButton("Output Folder...", self)
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)
        # finish button
        self.btn_finish = QPushButton("Confirm", self)
        self.btn_finish.clicked.connect(self.finish)
        layout.addWidget(self.btn_finish)
        # init variables
        self.file_path = None
        self.folder_path = None
    
    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File...", "", "PNG (*.PNG);;JPG (*.JPG);;BMP (*.BMP);;All Files (*)","PNG (*.PNG)")
        if file_name:
            self.file_path = file_name
    def select_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Output Folder")
        if folder_name:
            self.folder_path = folder_name
    def finish(self):
        #check if two variable are defined
        if self.file_path==None or self.folder_path== None:
            """pass"""
            msgbox = QMessageBox()
            msgbox.setGeometry(100, 100, 200, 100)
            msgbox.setText("Undefined Input/Output")
            msgbox.setIcon(QMessageBox.Icon.Critical)
            msgbox.setWindowTitle("Error")
            msgbox.exec()
        else:
            bitmap_to_contour_svg(input_bitmap_path=self.file_path,output_svg_path=self.folder_path+"/output.svg")
            self.close()
    def closeEvent(self,event):
        sys.exit()

def length_within_points(a : Iterable, empty_value : Union[int, float] = 0) -> int:
    a = list(a)
    l_pivot, r_pivot = -1, -2
    for index, (l_val, r_val) in enumerate(zip(a[::1], a[::-1])):
        if l_val != empty_value and l_pivot == -1:
            l_pivot = index
        if r_val != empty_value and r_pivot == -2:
            r_pivot = len(a) - index
    return r_pivot - l_pivot + 1

def dump_rings_from_image(image : np.ndarray, output_path : str, plot_dict : dict = {"color" : "k", "linewidth" : 2.0}, default_height : float = 8) -> List[np.ndarray]:
    # regular operation
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 50, 150)
    
    # get ratio between width and height to adjust the final output
    valid_width = length_within_points(edge.sum(axis=0))
    valid_height = length_within_points(edge.sum(axis=1))
    true_ratio = valid_width / valid_height
    
    # get contour of the edge image
    contour_tuple = cv2.findContours(edge, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    contours = contour_tuple[0]
    rings = [np.array(c).reshape([-1, 2]) for c in contours]
    
    # adjust coordinate system to the image coordinate system
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for ring in rings:
        max_x = max(max_x, ring.max(axis=0)[0])
        max_y = max(max_y, ring.max(axis=0)[1])
        min_x = max(min_x, ring.min(axis=0)[0])
        min_y = max(min_y, ring.min(axis=0)[1])
    
    # adjust ratio
    plt.figure(figsize=[default_height * true_ratio, default_height])
    
    # generate plot
    for _, ring in enumerate(rings):
        close_ring = np.vstack((ring, ring[0]))
        xx = close_ring[..., 0]
        yy = max_y - close_ring[..., 1]
        plt.plot(xx, yy, **plot_dict)
    
    plt.axis("off")
    plt.savefig(output_path, transparent=True) # "transparent=True" REMOVES BACKGROUND, SAVE A LOT OF WORK

def bitmap_to_contour_svg(input_bitmap_path : str, output_svg_path : str):
    img = cv2.imread(input_bitmap_path)
    dump_rings_from_image(img, output_path=output_svg_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())