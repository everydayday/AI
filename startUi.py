import cv2
import numpy as np

# 마우스 이벤트 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global is_webcam_started

    # 마우스 왼쪽 버튼 클릭 시
    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭한 위치가 버튼 영역 내에 있는지 확인
        if (x > 10 or x < 60) and (y > 10 or y < 60):
            print('yes')
            is_webcam_started = True

# 웹캠 시작 함수
def start_webcam():
    # 웹캠을 연결합니다.
    cap = cv2.VideoCapture(0)

    while True:
        # 프레임을 읽어옵니다.
        ret, frame = cap.read()

        # 화면에 프레임을 표시합니다.
        cv2.imshow('Webcam', frame)

        # 'q'를 누르거나 is_webcam_started가 True이면 종료합니다.
        if cv2.waitKey(1) == ord('q') :
            break
        
        #if cv2.waitKey(1) == ord('q') or is_webcam_started:
        #    break

    # 사용이 끝나면 웹캠을 해제합니다.
    cap.release()
    cv2.destroyAllWindows()

# 전역 변수 초기화
is_webcam_started = False

# OpenCV 창 생성
cv2.namedWindow('Webcam')

# 마우스 이벤트 콜백 함수 등록
cv2.setMouseCallback('Webcam', mouse_callback)

# 메시지 표시
start_message = np.zeros((150, 500, 3), dtype=np.uint8)
start_message.fill(255)
cv2.putText(start_message, 'Click the Start button to begin the webcam', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 2)

# 창을 업데이트하면서 사용자 입력을 기다립니다.
while True:
    cv2.imshow('Webcam', start_message)

    # 'q'를 누르면 종료합니다.
    if cv2.waitKey(1) == ord('q'):
        break

    # is_webcam_started가 True이면 웹캠을 시작합니다.
    if is_webcam_started: 
        start_webcam()       
        break

