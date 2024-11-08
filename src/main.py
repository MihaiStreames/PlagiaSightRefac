"""
    Coders: Daniel-Dfg and Luckyyyin
"""
import nltk
from sys import argv
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer
from UI_Functional.main_window import MainWindow
import os
#from time import time
#CURRENT_TIME = None
def download_additional_resources():
    resources = [
        'punkt',
        'punkt_tab',
        'words',
        'stopwords',
        'averaged_perceptron_tagger',
        'averaged_perceptron_tagger_eng'
    ]

    for resource in resources:
        try:
            nltk.data.find(f'corpora/{resource}')
        except LookupError:
            print("An additional package needs to be donwloaded (only happens once per package)")
            nltk.download(resource)


if __name__ == "__main__":
    #CURRENT_TIME = time()
    # Check whether there is already a running QApplication (e.g., if running from an IDE).
    qapp = QApplication.instance()
    if not qapp:
        qapp = QApplication(argv)

    window = MainWindow()
    window.show()
    window.raise_()
    #print(f"Startup time: {time()-CURRENT_TIME}")
    #Bonjour
    QTimer.singleShot(800, download_additional_resources)
    qapp.exec()
    temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
    for filename in os.listdir(temp_dir):
        if filename != 'README.md':
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
