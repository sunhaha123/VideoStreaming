from django.shortcuts import render
# views.py
from django.shortcuts import render
from django.http import StreamingHttpResponse
# Create your views here.

# 导入刚刚写好的类
from .base_camera import Camera

def index(request):
        #此处的模板请自行创建 例如:<html><body><img src='http://your_ip:port/camera/video_feed/' >
        return render(request,'camera.html')

def gen(camera):
        """视频流生成器功能。"""
        while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def video_feed(request):
        """
        视频流路由。将其放入img标记的src属性中。
        例如：<img src='http://your_ip:port/camera/video_feed/' >
        """
        # 此处应用使用StreamingHttpResponse，而不是用HttpResponse
        return StreamingHttpResponse(gen(Camera()),
                                        content_type='multipart/x-mixed-replace; boundary=frame')
