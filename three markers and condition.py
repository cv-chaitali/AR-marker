import cv2
import numpy as np
from object_loader import OBJ
import math

calibration = np.load("/Users/chaitalibhattacharyya/Desktop/쓰리다 어토메이션/cam_mat_av.npz")

mtx= calibration["camMatrix"]
dist = calibration["distCoef"]
marker1_id = 68
marker2_id = 69
marker3_id = 70
obj_path = "/Users/chaitalibhattacharyya/Desktop/쓰리다 어토메이션/cube.obj"
obj = OBJ(obj_path, swapyz=True)

# cap = cv2.VideoCapture('path/to/video/file.mp4')

# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if not ret:  # Check if frame was successfully read
#         break

model = np.array([[ 2.4, -2.4,  2.4],
       [ 2.4, -2.4, -2.4],
       [ 2.4,  2.4,  2.4],
       [ 2.4,  2.4, -2.4],
       [-2.4, -2.4,  2.4],
       [-2.4, -2.4, -2.4],
       [-2.4,  2.4,  2.4],
       [-2.4,  2.4, -2.4]])

cap = cv2.VideoCapture(1)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)


while(True):
    ret, frame = cap.read()
    
        
    # Define the rotation and translation vectors
    rvecs1 = np.array([ 2.98969011, -0.10622513,  0.20938305])
    rvecs2 = np.array([ 3.08723531, -0.08143395,  0.21018213])
    rvecs3 = np.array([ 3.23242976, -0.00787602,  2.06458464])
    tvecs1 = np.array([-63.88892557, -25.63058673,  59.75624146])
    tvecs2 = np.array([-61.04150737, -28.85400097,  67.66699227])
    tvecs3 = np.array([-57.16775894, -32.24923976,  75.33138719])
    
    # Project the 3D coordinates of each cube onto the 2D image plane
    imgpts, _ = cv2.projectPoints(model, rvecs1, tvecs1, mtx, dist)
    imgpts1, _ = cv2.projectPoints(model, rvecs2, tvecs2, mtx, dist)
    imgpts2, _ = cv2.projectPoints(model, rvecs3, tvecs3, mtx, dist)
    
    imgpts = np.int32(imgpts).reshape(-1, 2)
    
    # Draw cube faces
    frame = cv2.fillPoly(frame, [imgpts[:4]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts[4:]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts[[0,1,5,4]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts[[1,2,6,5]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts[[2,3,7,6]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts[[3,0,4,7]]], (0, 0, 255))
    
    # Draw cube edges
    for j in range(4):
        frame = cv2.line(frame, tuple(imgpts[j]), tuple(imgpts[(j+1)%4]), (0, 0, 255), thickness=2)
        frame = cv2.line(frame, tuple(imgpts[j+4]), tuple(imgpts[((j+1)%4)+4]), (0, 0, 255), thickness=2)
        frame = cv2.line(frame, tuple(imgpts[j]), tuple(imgpts[j+4]), (0, 0, 255), thickness=2)
      
    imgpts1 = np.int32(imgpts1).reshape(-1, 2)
    
    
    # Draw cube faces
    frame = cv2.fillPoly(frame, [imgpts1[:4]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts1[4:]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts1[[0,1,5,4]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts1[[1,2,6,5]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts1[[2,3,7,6]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts1[[3,0,4,7]]], (0, 0, 255))
    
    # Draw cube edges
    for j in range(4):
        frame = cv2.line(frame, tuple(imgpts1[j]), tuple(imgpts1[(j+1)%4]), (0, 0, 255), thickness=2)
        frame = cv2.line(frame, tuple(imgpts1[j+4]), tuple(imgpts1[((j+1)%4)+4]), (0, 0, 255), thickness=2)
        frame = cv2.line(frame, tuple(imgpts1[j]), tuple(imgpts1[j+4]), (0, 0, 255), thickness=2)
     
    
     
    
    imgpts2 = np.int32(imgpts2).reshape(-1, 2)
    
    
    # Draw cube faces
    frame = cv2.fillPoly(frame, [imgpts2[:4]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts2[4:]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts2[[0,1,5,4]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts2[[1,2,6,5]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts2[[2,3,7,6]]], (0, 0, 255))
    frame = cv2.fillPoly(frame, [imgpts2[[3,0,4,7]]], (0, 0, 255))
    
    # Draw cube edges
    for j in range(4):
        frame = cv2.line(frame, tuple(imgpts2[j]), tuple(imgpts2[(j+1)%4]), (0, 0, 255), thickness=2)
        frame = cv2.line(frame, tuple(imgpts2[j+4]), tuple(imgpts2[((j+1)%4)+4]), (0, 0, 255), thickness=2)
        frame = cv2.line(frame, tuple(imgpts2[j]), tuple(imgpts2[j+4]), (0, 0, 255), thickness=2)








    
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(frame, cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_1000))
    if ids is not None and len(ids) == 2:
        marker1_index = None
        marker2_index = None
        for i in range(len(ids)):
            if ids[i] == marker1_id:
                marker1_index = i
            elif ids[i] == marker2_id:
                marker2_index = i

        if marker1_index is not None and marker2_index is not None:
            rvec1, tvec1, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker1_index], 0.048, mtx, dist)
            rvec2, tvec2, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker2_index], 0.048, mtx, dist)
            distance = cv2.norm(tvec1-tvec2)
            print("Distance between marker 1 and marker 2 or 3:",round(distance,2))
            
            
            
    elif ids is not None and len(ids) >= 3:
        marker1_index = None
        marker2_index = None
        marker3_index = None
        for i in range(len(ids)):
            if ids[i] == marker1_id:
                marker1_index = i
            elif ids[i] == marker2_id:
                marker2_index = i
            elif ids[i] == marker3_id:
                marker3_index = i
        if marker1_index is not None and marker2_index is not None and marker3_index is not None:
            rvec1, tvec1, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker1_index], 0.048, mtx, dist)
            rvec2, tvec2, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker2_index], 0.048, mtx, dist)
            rvec3, tvec3, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker3_index], 0.048, mtx, dist)
    
            # r_1_mat,_ = cv2.Rodrigues(rvec1)
            # r_2_mat,_ = cv2.Rodrigues(rvec2)
            # relative_r = r_2_mat @ r_1_mat.T #matrix
            # # relative_r,_ = cv2.Rodrigues(relative_r) #vector
            # angle = math.acos((relative_r[0][0]+relative_r[1][1]+relative_r[2][2]-1)/2)
            
    
    
            distance1 = cv2.norm(tvec1-tvec2)
            # distance2 = cv2.norm(tvec2-tvec3)
            distance3 = cv2.norm(tvec1-tvec3)
            distance2 = cv2.norm(tvec2-tvec3)
            
            r_1_mat,_ = cv2.Rodrigues(rvec1)
            r_2_mat,_ = cv2.Rodrigues(rvec2)
            relative_r = r_2_mat @ r_1_mat.T #matrix
            # relative_r,_ = cv2.Rodrigues(relative_r) #vector
            angle = math.acos((relative_r[0][0]+relative_r[1][1]+relative_r[2][2]-1)/2)
            
           
            print("Distance between marker 1 and marker 2:", (round(distance1,2),0,0))
            print("Distance between marker 2 and marker 3:", (0,round(distance2,2),0))
            print("Distance between marker 1 and marker 3:", round(distance3,2))
            print("r and t values:", rvec1, tvec1)
            print("r and t values:", rvec2, tvec2)
            print("r and t values:", rvec3, tvec3)
            
            point1 = cv2.drawFrameAxes(frame, mtx, dist, rvec1, tvec1 ,  4,4)
            point2 = cv2.drawFrameAxes(frame, mtx, dist, rvec2, tvec2 ,  4,4)
            point3 = cv2.drawFrameAxes(frame, mtx, dist, rvec3, tvec3 , 4,4)
            
            frame_markers = cv2.aruco.drawDetectedMarkers(frame,corners,ids,(0,255,0))
            for i in range(len(ids)):
            
                id_num = str(ids[i][0])
                
                
                center = tuple(map(int, corners[i][0].mean(axis=0)))
                
                # Draw the ID number on the frame at the center of the marker
                # cv2.putText(frame_markers, id_num, center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            
            cv2.imshow("Frame with markers", frame_markers)



            cv2.putText(frame, "Distance between marker 1 and marker 2: {:.2f}".format(round(distance1,2),0,0), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            cv2.putText(frame, "Distance between marker 1 and marker 3: {:.2f}".format(round(distance3,2)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                   

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
