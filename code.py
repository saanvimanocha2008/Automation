import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "Img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False

    return image_name
    print("Snapshot Taken!")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_files(image_name):
    access_token = "sl.BF2C7TeRqlDrOKCNy567PD9e8xX_ZdB185rdGsw7r2VC7cOvMjy8L2GJC1j4psRx79WKcsVC1Y-3QwRGt49naMQThBTqZj19lM2WTEpYAXY075B1qdcHDp1n8PwtNogTaEUEzrlO"
    file = image_name
    file_from = file
    file_to = "/newFolder1"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded!")

def main():
    while(True):
        if((time.time()-start_time) >= 300):
            name = take_snapshot()
            upload_files(name)

main()