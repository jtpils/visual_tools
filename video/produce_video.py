import cv2
import os

def video_producer_2():
    """
    opencv2 use images to make video
    """
    img_path = '/home/hexindong/ws_dl/pyProj/cubic-local/test_result/OFHZ/'
    f = os.listdir(img_path)
    f.sort()
    videoWriter = cv2.VideoWriter('/home/hexindong/Desktop/Drive0064-Man.mp4',cv2.cv.CV_FOURCC(*'PIM1'),fps=20, frameSize=(800, 600))

    for i in f:
        img = cv2.imread(img_path + i)
        cv2.imshow('testResult',img)
        videoWriter.write(img)
        print str(i)

    videoWriter.release()


def video_producer_3():
    """
    opencv3 use images to make video
    """
    img_path = '/home/ovo/data/data/Kitti/object/drive_0064/video_image/'

    f = os.listdir(img_path)
    f.sort()
    videoWriter = cv2.VideoWriter('/home/ovo/data/data/Kitti/object/drive_0064/Drive0064-Man.mp4',
                                 cv2.VideoWriter_fourcc(*'PIM1'),fps=20, frameSize=(1242, 375))

    for i in f:
        img = cv2.imread(img_path + i)
        # cv2.imshow('testResult',img)
        videoWriter.write(img)
        print str(i)

    videoWriter.release()

def video_producer(img_path, video_save_path):
    '''
    input: 
        img_path: image dictory path  :'/home/ovo/data/data/Kitti/object/drive_0064/video_image/'
        video_save_path: '/home/ovo/data/data/Kitti/object/drive_0064/Drive0064-Man.mp4'
    '''
    f = os.listdir(img_path)
    f.sort()
    videoWriter = cv2.VideoWriter(video_save_path, cv2.VideoWriter_fourcc(*'PIM1'), fps=20, frameSize=(1242, 375))
    for i in f:
        img = cv2.imread(img_path+i)
        videoWriter.write(img)
        print (str(i))
    videoWriter.release()

if __name__=='__main__':
    img_path = '/home/ovo/data/data/Kitti/object/drive_0064/video_image/'
    video_save_path = '/home/ovo/data/data/Kitti/object/drive_0064/new.mp4'
    video_producer(img_path, video_save_path)