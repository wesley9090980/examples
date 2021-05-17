
import os
from PIL import Image
import numpy as np


def geturls():
    # res=requests.get(website,headers=headers)
    # htmls=res.content
   for dir in os.listdir("d:/getdkimg/img"):
       imghandle("img/"+dir)

def imghandle(path):
    a = np.array(Image.open(path).convert("L")).astype('float')
    depth = 10.                    #预设深度为10，取值范围(0-100)
    grad = np.gradient(a)          #取图像灰度的梯度值
    grad_x,grad_y = grad           #分别取x轴、y轴的梯度值
    grad_x = grad_x*depth/100.     #根据深度调整 x，y轴的梯度值
    grad_y = grad_y*depth/100.

    A = np.sqrt(grad_x**2+grad_y**2+1.)
    uni_x = grad_x/A 
    uni_y = grad_y/A 
    uni_z = 1./A 

    vec_el = np.pi/2.2                 #光源的俯视角度，弧度值
    vec_ez = np.pi/4                   #光源的方位角度，弧度值
    dx = np.cos(vec_el)*np.cos(vec_ez) #光影对x轴的影响
    dy = np.cos(vec_el)*np.sin(vec_ez) #光影对y轴的影响
    dz = np.sin(vec_el)                #光影对z轴的影响

    e = 255*(dx*uni_x + dy*uni_y + dz*uni_z)  #光源归一化
    e = e.clip(0,255)

    im = Image.fromarray(e.astype('uint8'))   #重构图像
    im.save(path)


if __name__ == '__main__':
    geturls()