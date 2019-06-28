import os
import face_recognition
import threading
import time


class RecorgNizerMani():

    def __init__(self):
        self.start_time = time.time()
        self._label = 1
        self.increment_val = 1

        self.treshold_val = 0.31
        self.file_path = "C:\Users\HP\Desktop\\425\\4250110"
        self.file_ = os.listdir(self.file_path)
        self.loaded_img_weights = {}
        self.labeled_img = {}
        self.load_filesToArray()
        self.partial_filePath_list = []

    def load_filesToArray(self):
        self.decrement_Val = len(self.file_) - ((len(self.file_)) - 1)
        for file_index in range(len(self.file_)):
            temp = self.file_path + "/" + self.file_[file_index]
            self.loaded_img_weights[self.file_[file_index]] = temp
            # self.partial_filePath_list.append(self.file_[file_index])
            # print "Loading Files To Tray  " + str(((float(self.decrement_Val)) / float(len(self.file_))) * 100)
            self.decrement_Val += 1
        self.label_resemblance()

    @staticmethod
    def face_encodings(filetopath):
        return face_recognition.face_encodings(face_recognition.load_image_file(filetopath))[0]

    def check_recorg_val(self, picked_ytbecoded_file, next_ytbencoded_tocheck_file):
        print  face_recognition.face_distance([picked_ytbecoded_file], next_ytbencoded_tocheck_file)
        if ((
                face_recognition.face_distance([picked_ytbecoded_file], next_ytbencoded_tocheck_file) < self.treshold_val)):

            # print  ("checking {} against {} results in", picked_ytbecoded_file,next_ytbencoded_tocheck_file,face_recognition.face_distance([picked_ytbecoded_file], next_ytbencoded_tocheck_file))
            return True
        else:
            return False
    def check_label_prob(self,increment_val_):
        print "calling with", increment_val_
        dummy_inc_val = increment_val_
        self.ckecklistner = 0
        while True:
            print self.ckecklistner
            # if increment_val_ ==  18:
            #     print self.loaded_img_weights
            try:
                self.bool_val = self.check_recorg_val(self.face_encodings(self.loaded_img_weights.values()[dummy_inc_val]),
                                         self.face_encodings(self.loaded_img_weights.values()[increment_val_-1]))
            except IndexError as er:
                print "Error"
            # print self.bool_val
            print self.loaded_img_weights.values()[dummy_inc_val] + " as against " + self.loaded_img_weights.values()[increment_val_-1],increment_val_
            if self.bool_val:
                print self.bool_val
                return (True,self.labeled_img[self.loaded_img_weights.keys()[self.loaded_img_weights.values().index(
                    self.loaded_img_weights.values()[increment_val_-1])]])
            elif increment_val_- 1 == 0:
                break
            else:
                increment_val_-=1
            self.ckecklistner+=1

        return (False,None)
    def label_resemblance(self):


        self.labeled_img[
            self.loaded_img_weights.keys()[self.loaded_img_weights.values().index(
                self.loaded_img_weights.values()[0])]
        ] = str(self._label)

        for img_index in range(len(self.file_)-1):
            self.label_pro = self.check_label_prob(self.increment_val)
            if self.label_pro[0]:
                print "got here",self.increment_val
                self.labeled_img[
                    self.loaded_img_weights.keys()[self.loaded_img_weights.values().index(
                        self.loaded_img_weights.values()[self.increment_val])]
                ] = str(self.label_pro[1])
                if self.increment_val < len(self.loaded_img_weights.values())-1:
                    self.increment_val +=1
                print self.loaded_img_weights.keys()[self.loaded_img_weights.values().index(
                        self.loaded_img_weights.values()[self.increment_val])]

                continue
            else:
                print "i was called"
                self._label += 1
                self.labeled_img[
                    self.loaded_img_weights.keys()[self.loaded_img_weights.values().index(
                        self.loaded_img_weights.values()[self.increment_val])]
                ] = str(self._label)
                self.increment_val += 1
        print self.labeled_img
        print "ran for {} to {}".format(self.start_time,time.gmtime())
        print("--- %s seconds ---" % (time.time() - self.start_time))

RecorgNizerMani()

# known_image = face_recognition.load_image_file("guy.jpg")
# unknown_image = face_recognition.load_image_file("image_watermarkv2IMP.png")
#
# # print known_image
# tempEncodedm= []
#
#
#
# for k, v in loaded_img_weights.items():
#
#     dist = face_recognition.face_distance([loaded_img_weights.values()[2]], v)
#     print dist,k


# biden_encoding = face_recognition.face_encodings(known_image)[0]
# unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
#
# results = face_recognition.face_distance([unknown_encoding],biden_encoding)


# print results
