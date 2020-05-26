
from django.shortcuts import render,HttpResponse
from . import forms
from . import models
# Create your views here.

def showform(request):
    form = forms.TestForm()
    return render(request,'showForm.html',locals())

def testBug(request):
    return render(request,'app01/testBug.html')

def testForm(request):
    if request.method == "POST":
        form = forms.TestModelFormUses(request.POST)
        form.is_valid()
        form.save()
        return HttpResponse("发送POST数据成功")
    return render(request,'app01/testform.html')

def testForm_instance(request):
    '''
    测试modelform的save方法
    :param request:
    :return:
    '''
    print('testforminstance')

    obj = models.Userinfo.objects.first()
    print(obj)
    form = forms.TestModelFormUses(instance=obj)
    if request.method == "POST":
        form = forms.TestModelFormUses(request.POST)
        form.is_valid()
        #如果不传入instance参数 将会直接创建
        #如果传入instance参数
        form.save()
        return HttpResponse("发送POST数据成功")
    return render(request,'app01/testform.html',locals())

def testextends(requests):
    return render(requests,'app01/testextendsson.html')

def test_uploadfile_form(request):
    '''
    测试form Filefield字段的使用
    :param request:
    :return:
    '''
    print('test_uploadfile_form')


    if request.method == "POST":
        form = forms.TestFileFieldForm(request.POST,request.FILES)
        form.is_valid()
        print(form.cleaned_data)
        print(request.FILES)
        selfpic = form.cleaned_data['selfpic']
        print(selfpic)
        print(selfpic.content_type)
        return HttpResponse("发送POST数据成功")
    form = forms.TestFileFieldForm()
    return render(request,'app01/testform.html',locals())




