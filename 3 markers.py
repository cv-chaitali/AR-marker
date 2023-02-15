import cv2
import numpy as np


calibration = np.load(r"C:/Users/Avilab/Downloads/Calib_data1.npz")

mtx= calibration["camMatrix"]
dist = calibration["distCoef"]
marker1_id = 68
marker2_id = 69
marker3_id = 70



cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    
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
            rvec1, tvec1, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker1_index], 5.0, mtx, dist)
            rvec2, tvec2, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker2_index], 5.0, mtx, dist)
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
            rvec1, tvec1, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker1_index], 5.0, mtx, dist)
            rvec2, tvec2, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker2_index], 5.0, mtx, dist)
            rvec3, tvec3, _ = cv2.aruco.estimatePoseSingleMarkers(corners[marker3_index], 5.0, mtx, dist)
    
            
    
    
            distance1 = cv2.norm(tvec1-tvec2)
            # distance2 = cv2.norm(tvec2-tvec3)
            distance3 = cv2.norm(tvec1-tvec3)
            distance2 = distance3 - distance1
            
           
            
           
            print("Distance between marker 1 and marker 2:", (round(distance1,2),0,0))
            print("Distance between marker 2 and marker 3:", (0,round(distance2,2),0))
            print("Distance between marker 1 and marker 3:", round(distance3,2))
            print("r and t values:", rvec1, tvec1)
            print("r and t values:", rvec2, tvec2)
            print("r and t values:", rvec3, tvec3)
            
            point1 = cv2.drawFrameAxes(frame, mtx, dist, rvec1, tvec1 ,  4,4)
            point2 = cv2.drawFrameAxes(frame, mtx, dist, rvec2, tvec2 ,  4,4)
            point3 = cv2.drawFrameAxes(frame, mtx, dist, rvec3, tvec3 , 4,4)




            cv2.putText(frame, "Distance between marker 1 and marker 2: {:.2f}".format(round(distance1,2),0,0), (10, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            cv2.putText(frame, "Distance between marker 1 and marker 3: {:.2f}".format(round(distance3,2)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                        
            frame_markers = cv2.aruco.drawDetectedMarkers(frame,corners,ids,(0,255,0))
            for i in range(len(ids)):
            
                id_num = str(ids[i][0])
                
                
                center = tuple(map(int, corners[i][0].mean(axis=0)))
                
                # Draw the ID number on the frame at the center of the marker
                # cv2.putText(frame_markers, id_num, center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
            
            # cv2.imshow("Frame with markers", frame_markers)
            

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
            

cap.release()
cv2.destroyAllWindows()
