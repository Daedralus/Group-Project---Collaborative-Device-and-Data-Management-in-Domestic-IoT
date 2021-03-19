
# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2

from imutils import paths
import os

from picamera import PiCamera

#TODO
#remove args parser
#

#example usage
#this would be the default door usage thread
"""
import Recog, KeyPad, DoorLock, DataBase
r = Recog()
k = KeyPad()
d = DataBase.open()
r.start()
try: 
	while(True):
		if KeyPad.entered():
			pinUser = KeyPad.getLastUserName()
			if pinUser in r.detect():
				DoorLock.Open()
				d.log(pinUser,time(),True)
			else:
				d.log(pinUser,time(),False)
		k.update() #after a certain amount of ticks set entered() to false
		#r.update()
except:
	r.stop()
	d.close()
	print("Error occured\n")
	
	
"""


class Recog():
	def __init__():
		#
		#python encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog
		#python pi_face_recognition.py --cascade haarcascade_frontalface_default.xml
		
		#the parser might cause conflicts as ive merged the two files
		
		# construct the argument parser and parse the arguments
		ap = argparse.ArgumentParser()
		ap.add_argument("-c", "--cascade", required=True,
			help = "path to where the face cascade resides")
		ap.add_argument("-e", "--encodings", required=True,
			help="path to serialized db of facial encodings")
		args = vars(ap.parse_args())
		
		# load the known faces and embeddings along with OpenCV's Haar
		self.data = pickle.loads(open(args["encodings"], "rb").read())
		self.detector = cv2.CascadeClassifier(args["cascade"])
		
		#set vs to None
		self.vs= None
		
		# construct the argument parser and parse the arguments
		ap = argparse.ArgumentParser()
		ap.add_argument("-i", "--dataset", required=True,
			help="path to input directory of faces + images")
		ap.add_argument("-e", "--encodings", required=True,
			help="path to serialized db of facial encodings")
		ap.add_argument("-d", "--detection-method", type=str, default="cnn",
			help="face detection model to use: either `hog` or `cnn`")
		args = vars(ap.parse_args())


		
		# grab the paths to the input images in our dataset
		self.imagePaths = list(paths.list_images(args["dataset"]))
		
		#extra
		self.e = args["encodings"]
		self.method = args["detection_method"])

		# initialize the list of known encodings and known names
		self.knownEncodings = []
		self.knownNames = []
			

	def takePhoto():
		#initialize camera
		camera = PiCamera()
		
		#take photo
		camera.start_preview(alpha=0)
		camera.capture('/home/pi/Desktop/LatestImage.jpg')
		camera.stop_preview()
		
		
	def start():
		self.vs = VideoStream(src=0).start()
	def stop():
		self.vs.stop()
		self.vs = None
	def encode():
		if self.vs is None:
			# loop over the image paths
			for (i, imagePath) in enumerate(self.imagePaths):
				# extract the person name from the image path
				print("[INFO] processing image {}/{}".format(i + 1,
					len(self.imagePaths)))
				name = imagePath.split(os.path.sep)[-2]

				# load the input image and convert it from RGB (OpenCV ordering)
				# to dlib ordering (RGB)
				image = cv2.imread(imagePath)
				rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

				# detect the (x, y)-coordinates of the bounding boxes
				# corresponding to each face in the input image
				boxes = face_recognition.face_locations(rgb,
					model=self.method

				# compute the facial embedding for the face
				encodings = face_recognition.face_encodings(rgb, boxes)

				# loop over the encodings
				for encoding in encodings:
					# add each encoding + name to our set of known names and
					# encodings
					self.knownEncodings.append(encoding)
					self.knownNames.append(name)
			# dump the facial encodings + names to disk
			data = {"encodings": knownEncodings, "names": knownNames}
			f = open(self.e, "wb")
			f.write(pickle.dumps(data))
			f.close()
			
			#update properties
			self.data = pickle.loads(open(args["encodings"], "rb").read())
			self.detector = cv2.CascadeClassifier(args["cascade"])
			
			self.imagePaths = list(paths.list_images(args["dataset"]))
		else:
			print("To encode the new faces you must first stop the detection of the faces")
		
		
	def detect():
		if self.vs is None:
			print ("Please start the Recog Object before trying to detect faces\n")
			return []
		else:
			# grab the frame from the threaded video stream and resize it
			# to 500px (to speedup processing)
			frame = self.vs.read()
			frame = imutils.resize(frame, width=500)
			
			# convert the input frame from (1) BGR to grayscale (for face
			# detection) and (2) from BGR to RGB (for face recognition)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

			# detect faces in the grayscale frame
			rects = self.detector.detectMultiScale(gray, scaleFactor=1.1, 
				minNeighbors=5, minSize=(30, 30),
				flags=cv2.CASCADE_SCALE_IMAGE)

			# OpenCV returns bounding box coordinates in (x, y, w, h) order
			# but we need them in (top, right, bottom, left) order, so we
			# need to do a bit of reordering
			boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

			# compute the facial embeddings for each face bounding box
			encodings = face_recognition.face_encodings(rgb, boxes)
			names = []

			# loop over the facial embeddings
			for encoding in encodings:
				# attempt to match each face in the input image to our known
				# encodings
				matches = face_recognition.compare_faces(self.data["encodings"],
					encoding)
				name = "No match"

				# check to see if we have found a match
				if True in matches:
					# find the indexes of all matched faces then initialize a
					# dictionary to count the total number of times each face
					# was matched
					matchedIdxs = [i for (i, b) in enumerate(matches) if b]
					counts = {}

					# loop over the matched indexes and maintain a count for
					# each recognized face face
					for i in matchedIdxs:
						name = self.data["names"][i]
						counts[name] = counts.get(name, 0) + 1

					# determine the recognized face with the largest number
					# of votes (note: in the event of an unlikely tie Python
					# will select first entry in the dictionary)
					name = max(counts, key=counts.get)
				
				# update the list of names
				names.append(name)
			return names

		