import cv2

cam = cv2.VideoCapture(0)

while True:
    ret, image = cam.read()
    image = cv2.flip(image, 1)
    # 获取图像的宽和高
    height, width, _ = image.shape

    # 计算裁剪框的大小
    # crop_width = 1080
    # crop_height = 1080

    crop_width = 720
    crop_height = 720

    # 计算中心点
    center_x = width // 2
    center_y = height // 2

    # 计算裁剪框的坐标
    start_x = center_x - crop_width // 2
    start_y = center_y - crop_height // 2
    end_x = start_x + crop_width
    end_y = start_y + crop_height

    # 裁剪图像
    cropped_image = image[start_y:end_y, start_x:end_x]
    resized_image = cv2.resize(cropped_image, (224, 224))
    cv2.imshow('frame', resized_image)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
