# 기준 잡기
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# 안경 이미지 로드
glasses_img = cv2.imread('pngegg.png', cv2.IMREAD_UNCHANGED)
glasses_width = glasses_img.shape[1]
glasses_height = glasses_img.shape[0]

# Face mesh 모델 로드
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# 비디오 캡쳐 시작
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    
    # 입력 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 얼굴을 찾아서 468개 랜드마크 추출
    results = face_mesh.process(image)
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]
        landmark_points = []
        for landmark in landmarks.landmark:
            x = landmark.x * image.shape[1]
            y = landmark.y * image.shape[0]
            landmark_points.append((x, y))
        
        # 눈의 중심점 좌표 계산
        left_eye_x = int((landmark_points[33][0] + landmark_points[133][0]) / 2)
        left_eye_y = int((landmark_points[33][1] + landmark_points[133][1]) / 2)
        right_eye_x = int((landmark_points[362][0] + landmark_points[263][0]) / 2)
        right_eye_y = int((landmark_points[362][1] + landmark_points[263][1]) / 2)
        
        # 눈과 안경의 상대적 크기 계산
        scale = ((right_eye_x - left_eye_x) / glasses_width) * 2.0
        
        # 안경 이미지 회전 및 크기 조정
        glasses_img_resized = cv2.resize(glasses_img, (0, 0), fx=scale, fy=scale)
        angle = -cv2.fastAtan2((right_eye_y - left_eye_y), (right_eye_x - left_eye_x))
        M = cv2.getRotationMatrix2D((glasses_img_resized.shape[1]//2, glasses_img_resized.shape[0]//2), angle, 1.0)
        glasses_img_resized_rotated = cv2.warpAffine(glasses_img_resized, M, (glasses_img_resized.shape[1], glasses_img_resized.shape[0]))
        
        # 안경 이미지를 눈 위치에 합성
        x_offset = int(left_eye_x - (glasses_img_resized_rotated.shape[1]/15)*4)
        y_offset = int(left_eye_y - (glasses_img_resized_rotated.shape[0]/15)*6)
        y1, y2 = y_offset, y_offset + glasses_img_resized_rotated.shape[0]
        x1, x2 = x_offset, x_offset + glasses_img_resized_rotated.shape[1]

        alpha_s = glasses_img_resized_rotated[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        for c in range(0, 3):
            image[y1:y2, x1:x2, c] = (alpha_s * glasses_img_resized_rotated[:, :, c] + alpha_l * image[y1:y2, x1:x2, c])

        # try_x = int(landmark_points[199][0])
        # try_y = int(landmark_points[199][1])
        # cv2.line(image,(try_x,try_y),(try_x,try_y),(0,0,255),10)
    # 출력 이미지를 화면에 표시
    cv2.imshow('MediaPipe FaceMesh', image)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 종료
cap.release()
cv2.destroyAllWindows()

