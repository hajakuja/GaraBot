import os
import settings
def open_data_file(mode):
    if os.path.exists(settings.DATA_PATH):
        return open(settings.DATA_PATH, mode)
    else:
        return None
# def make_data_file():
#     if not os.path.exists(settings.DATA_PATH):
#         os.mkdir(settings.DATA_DIR)  
    