from django.shortcuts import render, HttpResponse, Http404
import os
from django.http import StreamingHttpResponse, FileResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


# 文件上传功能
def upload(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")

        f = open(os.path.join("D:\\Code\\upload", myFile.name), 'wb+')

        for chunk in myFile.chunks():
            f.write(chunk)
            f.close()
            return HttpResponse("upload over!")
    else:
        return render(request, 'upload.html')


# 文件下载功能
def download1(request):
    file_path = "D:\\Code\\upload\\CKS考试.txt"
    try:
        r = StreamingHttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['content-Disposition'] = 'attachment; filename=cks考试.txt'
        return r
    except Exception:
        raise Http404("Download error")


def download2(request):
    file_path = "D:\\Code\\upload\\世达CKS v1.23.pdf"
    try:
        f = open(file_path, 'rb')
        r = FileResponse(f, as_attachment=True, filename='世达CKS v1.23.pdf')
        return r
    except Exception:
        raise Http404("Download error")