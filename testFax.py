import os

import face_recognition

def faceEncodings(fileToPath):
    return face_recognition.face_encodings(face_recognition.load_image_file(fileToPath))[0]
loaded_img_weights = {}
known_image = face_recognition.load_image_file("guy.jpg")
unknown_image = face_recognition.load_image_file("image_watermarkv2IMP.png")
file_path = "C:/Users/HP/Desktop/image_Test_Utils"
file_ = os.listdir(file_path)
# print known_image
tempEncodedm= []
for n in range(len(file_)):
    temp = (file_path+"/"+file_[n])
    loaded_img_weights[file_[n]] = temp
print loaded_img_weights,"\n",file_

# for k, v in loaded_img_weights.items():
#
#     dist = face_recognition.face_distance([loaded_img_weights.values()[2]], v)
#     print dist,loaded_img_weights


# biden_encoding = face_recognition.face_encodings(known_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#
# results = face_recognition.face_distance([unknown_encoding],biden_encoding)



# print results

