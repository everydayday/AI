# =======================================================
# ===                  To do List                      ===
# 얼굴형 안경 근거 찾기
# 사람들에게 적용해보기
# 
# =======================================================



# degOfchin : 13
# face_width : 6 
# low_width : 7
# face_length : 2
import cv2
import mediapipe as mp
import math,utils
import numpy as np
from glassmodule import apply_glasses,face_detect

FONTS =cv2.FONT_HERSHEY_COMPLEX
    

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
       face_type, face_num = face_detect(landmark_points)

    
            
    #utils.textWithBackground(image,'얼굴형 타입: ' + face_type,FONTS, 1.0, (30, 50), bgOpacity=0.9, textThickness=2)
    #utils.colorBackgroundText(image,  f'Blink', FONTS, 1.7, (200, 100), 2, utils.YELLOW, pad_x=6, pad_y=6, )

    with_glass_image = apply_glasses(image,face_num)

    print(face_type)      
       
    
    
    cv2.imshow('MediaPipe FaceMesh', with_glass_image)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()

