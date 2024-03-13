from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cmdb.models import Phone, BorrowRecord
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


@login_required
def borrow_phone(request, pk):
    """
    申请借用手机视图
    """
    phone = Phone.objects.get(pk=pk)

    # 新增借用记录
    pr = BorrowRecord()
    pr.user = request.user
    pr.borrow_date = timezone.now()
    pr.phone = phone
    pr.save()

    # 修改被此次借用手机状态
    phone.status = '被借走'
    phone.save()

    # 发送邮件逻辑
    subject = f'[{request.user}] 申请借用手机'
    message = f'[{request.user}] 申请借用手机 ({phone.brand} - {phone.model} - {phone.serial_number})'
    recipient_list = [settings.ADMIN_EMAIL]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
    
    messages.success(request, '手机借用成功')
    return redirect(request.GET.get('next', 'admin:index'))



@login_required
def borrow_phone_v2(request, pk):
    phone = Phone.objects.get(pk=pk)
    if request.method == 'GET':
        next_url = request.GET.get('next')
        request.session['next_url'] = next_url 
        users = User.objects.all()
        # 或者是根据特定条件筛选可以审核的人，比如测试组下的每个测试人员
        # users = User.objects.filter(group='测试组')
        return render(request, 'cmdb/borrow.html', {'phone': phone, 'users': users})
    elif request.method == 'POST':
        print('body: ', request.body, request.POST)
        user_email = request.POST.get('selected_user_email')
        print('user_email: ', user_email)
        print('request session: ', request.session)
        next_url = request.session.get('next_url') 

        # 新增借用记录
        pr = BorrowRecord()
        pr.user = request.user
        pr.borrow_date = timezone.now()
        pr.phone = phone
        pr.save()

        # 修改被此次借用手机状态
        phone.status = '被借走'
        phone.save()

        # 发送邮件逻辑
        subject = f'[{request.user}] 申请借用手机'
        message = f'[{request.user}] 申请借用手机 ({phone.brand} - {phone.model} - {phone.serial_number})'
        recipient_list = [user_email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)
        
        messages.success(request, '手机借用成功')
        if next_url:
            print('next_url: ', next_url)
            return redirect(next_url)
        else:
            return redirect('admin:index')

        
