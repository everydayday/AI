import cv2
import mediapipe as mp
import math
import numpy as np
PI = math.pi

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    results = face_mesh.process(image)
    if results.multi_face_landmarks:
       landmarks = results.multi_face_landmarks[0]
       landmark_points = []
       for landmark in landmarks.landmark:
          x = landmark.x * image.shape[1]
          y = landmark.y * image.shape[0]
          landmark_points.append((x, y))
           
       y = landmark_points[28][0]
       x = landmark_points[28][1]
       
       #######
       #    y = landmark_points[157][0]
       #    x = landmark_points[157][1]
       
       # x, x1 눈 좌표
       y = landmark_points[158][0]
       x = landmark_points[158][1]
       
       
       y1 = landmark_points[153][0]
       x1 = landmark_points[153][1]       
       
       # print("x좌표:",abs(x-x1),"y좌표:",abs(y-y1) )
       
       # test
       y2 = landmark_points[10][0]
       x2 = landmark_points[10][1]
       
       # for upper
       y3 = landmark_points[8][0]
       x3 = landmark_points[8][1]
       
       #print("x2:",x2," x3",x3)
       
       #cv2.circle(image, (int(y), int(x)), 2, (0, 255, 0), -1)
       #cv2.circle(image, (int(y1), int(x1)), 2, (0, 255, 0), -1)
       # 얼굴 끝 위치
       ####cv2.circle(image, (int(y2), int(x2-(x3-x2))), 2, (0, 255, 0), -1)
       
       # 각각 각도 계산해서 특정 각도보다 커지는 지점 있으면 출력
       
       # 각도 계산
       '''
       y1 = landmark_points[135][0]
       x1 = landmark_points[135][1]
       cv2.circle(image, (int(y1), int(x1)), 2, (0, 255, 0), -1)
       
       y2 = landmark_points[169][0]
       x2 = landmark_points[169][1]
       cv2.circle(image, (int(y2), int(x2)), 2, (0, 255, 0), -1)
       
       arr = []
       arr.append([y1,x1,y2,x2])
       #rad = math.atan2(arr[2]-arr[0],arr[3]-arr[1])
       rad = math.atan2(y2-y1,x2-x1)
       deg = (rad*180)/PI
       print(deg)
       '''
       
       
       
       ######## 아래 턱 끝각 ##########
       
       ## 아래 턱 끝각
       # 얼굴 각도 1
       y1 = landmark_points[400][0]
       x1 = landmark_points[400][1]
       #cv2.circle(image, (int(y1), int(x1)), 2, (0, 255, 0), -1)
       
       y2 = landmark_points[378][0]
       x2 = landmark_points[378][1]
       #cv2.circle(image, (int(y2), int(x2)), 2, (0, 255, 0), -1)
       
       # 얼굴 각도 2
       y3 = landmark_points[8][0]
       x3 = landmark_points[8][1]
       #cv2.circle(image, (int(y3), int(x3)), 2, (255, 0, 0), -1)
       
       y4 = landmark_points[9][0]
       x4 = landmark_points[9][1]
       #cv2.circle(image, (int(y4), int(x4)), 2, (0, 0, 255), -1)
       
       
       rad1 = math.atan2(y2-y1,x2-x1)
       deg1 = (rad1*180)/PI
       
       rad2 = math.atan2(y4-y3,x4-x3)
       deg2 = (rad2*180)/PI
       #print('deg2',deg2)
       
       #print('rad diff',rad1-rad2)
       
       rad = rad2 - rad1
       deg1 = (rad1*180)/PI
       deg2 = (rad2*180)/PI
       deg = (rad*180)/PI
       fin_deg = 90 - deg
       print(fin_deg)
       ###
       #########################
       
       
       ######## 얼굴 폭 ########
       y1 = landmark_points[123][0]
       x1 = landmark_points[123][1]
       #cv2.circle(image, (int(y1), int(x1)), 2, (0, 255, 0), -1)
       
       y2 = landmark_points[352][0]
       x2 = landmark_points[352][1]
       #cv2.circle(image, (int(y2), int(x2)), 2, (0, 255, 0), -1)
       
       ###########################
       
       
       # 하안각 폭
       ## 아래 턱 끝각
       
       y1 = landmark_points[135][0]
       x1 = landmark_points[135][1]
       #cv2.circle(image, (int(y1), int(x1)), 2, (0, 255, 0), -1)
       
       y2 = landmark_points[364][0]
       x2 = landmark_points[364][1]
       #cv2.circle(image, (int(y2), int(x2)), 2, (0, 255, 0), -1)
       
       
       ### 얼굴길이 ####
       y2 = landmark_points[10][0]
       x2 = landmark_points[10][1]
       
       # for upper
       y3 = landmark_points[8][0]
       x3 = landmark_points[8][1]
       
       #cv2.circle(image, (int(y2), int(x2)), 2, (0, 0, 255), -1)
       #cv2.circle(image, (int(y3), int(x3)), 2, (0, 0, 255), -1)
       #cv2.circle(image, (int(y2), int(x2-(x3-x2))), 2, (0, 255, 0), -1)
       
       # 턱 부분
       y4 = landmark_points[152][0]
       x4 = landmark_points[152][1]
       #cv2.circle(image, (int(y4), int(x4)), 2, (0, 255, 0), -1)
       
       
       # 얼굴 끝 위치
       
       
       
       
       # 평균과의 차이 가장 적은 퍼센티지로 수치 값 구하기
    
    
    cv2.imshow('MediaPipe FaceMesh', image)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()