
import numpy as np
import cv2

def bilinear_interpolation(img, out_dim):
    src_h, src_w, channels = img.shape
    dst_h, dst_w = out_dim[1], out_dim[0]  #dim[0]-输出数据的行, dim[1]-输出数据的列
    scale_x = float(src_w) / dst_w
    scale_y = float(src_h) / dst_h
    # print('src_h, src_w = ', src_h, src_w)
    # print('dst_h, dst_w = ', dst_h, dst_w)

    if src_h ==dst_h and src_w ==dst_w:
        return img.copy()

    dst_img = np.zeros((dst_h, dst_w, 3),dtype = np.uint8)

    for i in range(channels):
        for dst_y in range(dst_h):
            for dst_x in  range(dst_w):

                # 几何中心对齐
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5

                # 规范边缘大小，不要超出范围
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1, src_w-1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)

                # 计算过程
                temp0 = (src_x1 - src_x) * img[src_y0,src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * img[src_y1,src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)

    return dst_img

if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    dst = bilinear_interpolation(img,(800,800))
    cv2.imshow('bilinear inter',dst)
    cv2.waitKey(0)
