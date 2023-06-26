import random
import time
import cv2
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    VideoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):

        ret, frame = VideoCaptureObject.read()

        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name , frame)
        start_time = time.time()

        result = False
    
    return image_name
    print("PHOTO TAKEN")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(image_name):
    access_token = "sl.BfyMyLL9Fns4TmsE-84Krs0aaiCx7eGsL_hoe3QHeGSUJdtoreV_cgOKWweVMdBLUvPu-WH5oVR4YW95I1n4tdmsJ4UWf-z__s0e-LIW4s5GchTyhynyJ9QY8wQpdLKTSGRy1Ao"
    file = image_name
    file_from = file
    file_to = "/newfolder1" + (image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from , 'rb') as f:
        dbx.files_upload(f.read() , file_to , mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >=3):
            name = take_snapshot()
            upload_file(name)
main()