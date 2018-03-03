import numpy as np
import cv2
import datetime
import time
import os

earlier=datetime.datetime.now()

name_count=0

#It will keep all the recordings daywise
def TimeElasped():
	current=datetime.datetime.now()
	elasped=current-earlier
	# print str(elasped.minute)+"-"+str(elasped.second)
	# print str(elasped.total_seconds())
	seconds=60*60*24
	if(elasped.total_seconds()>(seconds)):
		global earlier
		earlier=datetime.datetime.now()
		return 1
	else:
		return 0;

#It will delete all the recordings older than a month
def DeleteMonth():
	global name_count
	if(name_count>30):
		name_count=-1
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
while(True):
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter('vid'+str(name_count)+'.avi',fourcc, 20.0, (640,480))

	while(cap.isOpened()):
	    if(TimeElasped()):
	    	DeleteMonth()
	    	break
	    ret, frame = cap.read()
	    if ret==True:
	        # frame = cv2.flip(frame,0)

	        # write the flipped frame
	        out.write(frame)

	        cv2.imshow('frame',frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	            break
	    else:
	        break

	name_count=name_count+1

	# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

