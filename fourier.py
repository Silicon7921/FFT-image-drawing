import re
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QFileDialog

def select_file():
    
    class MainWindow(QWidget):
        def __init__(self):  
            super().__init__()   
            self.initUI()
        def initUI(self):
            pass
        
        def closeEvent(self, event) -> None:
            event.ignore() #dumb solution
        
        filepath, _=QFileDialog.getOpenFileName(None, "Select correct path file...", "", "TXT (*.TXT)","TXT (*.TXT)")
        """ for debug
        if filepath:
            print(filepath)
        else:
            print("void filepath") """
    
    if MainWindow.filepath:    
        return MainWindow.filepath
    else:
        raise ValueError("null file path")


def read_file(filepath):
    try:
        with open(filepath, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("path file not exist.")
        return None
    except Exception as e:
        print(f"Unknown Error: {e}")
        return None

def is_valid_char(c):
    valid_chars = set("MmHhLlQWERTYUIOPKJGFDSAZXCVBNqwertyuiopkjgfdsazxcvbn")
    return c in valid_chars

def parse_path(path):
    path_len = len(path)
    l_list = []
    i = 0
    while i < path_len:
        if is_valid_char(path[i]):
            j = i
            i += 1
            while i < path_len and not is_valid_char(path[i]):
                i += 1
            if i != j:
                s = path[j:i].strip()
                a = s[0]
                b = s[1:]
                if a in "HhVv":
                    l_list.append([a, float(b)])
                elif a in "LlMm":
                    a = a.replace("M", "L").replace("m", "l")
                    b_list = [float(bb) for bb in re.split(r'(?<=\d)-', b) if bb]
                    assert len(b_list) == 2
                    l_list.append([a, *b_list])
                elif a in "Cc":
                    b_list = [float(bb) for bb in re.split(r'(?<=\d)-', b) if bb]
                    assert len(b_list) == 6
                    l_list.append([a, *b_list])
                elif a in "Ss":
                    b_list = [float(bb) for bb in re.split(r'(?<=\d)-', b) if bb]
                    assert len(b_list) == 4
                    l_list.append([a, *b_list])
                else:
                    print("Unknown character：", s)
        else:
            print("error:", path[i])
            i += 1
    return l_list

def generate_point_list(l_list):
    point_list = []
    for line in l_list[:-1]:
        a = line[0]
        if a == "L":
            point_list.append((line[1], line[2]))
        elif a == "l":
            point_list.append((point_list[-1][0] + line[1], point_list[-1][1] + line[2]))
        elif a == "h":
            point_list.append((point_list[-1][0] + line[1], point_list[-1][1]))
        elif a == "v":
            point_list.append((point_list[-1][0], point_list[-1][1] + line[1]))
        elif a == "V":
            point_list.append((point_list[-1][0], line[1]))
        elif a == "c":
            point_list.append((point_list[-1][0] + line[5], point_list[-1][1] + line[6]))
        elif a == "s":
            point_list.append((point_list[-1][0] + line[3], point_list[-1][1] + line[4]))
        else:
            print(point_list[-1], line)
    return point_list

def compute_fourier_data(point_list):
    y = [complex(p[0] - 270, p[1] - 213.5) for p in point_list]
    y_matrix = np.array(point_list)
    y_len = len(y)
    yy = np.fft.fft(y)

    plt.plot(y_matrix[:, 0], y_matrix[:, 1])
    
    fourier_data = []
    for i, v in enumerate(yy[:y_len]):
        c = -2 * np.pi * i / y_len
        fourier_data.append([-v.real / y_len, c, np.pi / 2])
        fourier_data.append([-v.imag / y_len, c, 0])
    fourier_data.sort(key=lambda x: abs(x[0]), reverse=True)
    return fourier_data

def process_data(filepath):
    path = read_file(filepath)
    if path is None:
        return
    
    l_list = parse_path(path)
    point_list = generate_point_list(l_list)
    return compute_fourier_data(point_list)