from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cmdb.models import Phone, BorrowRecord
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


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
