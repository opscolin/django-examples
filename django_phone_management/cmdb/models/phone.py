
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Phone(models.Model):
    STATUS = (
        ('空闲中', '空闲中'),
        ('被借走', '被借走'),
        ('已故障', '已故障')
    )
    brand = models.CharField(max_length=32, verbose_name='手机品牌')
    model = models.CharField(max_length=32, verbose_name='手机型号')
    serial_number = models.CharField(max_length=64, unique=True, verbose_name='手机序列号')
    create_time = models.DateTimeField(auto_now=True, verbose_name='入库时间')
    buy_time = models.DateField(null=True, blank=True, verbose_name='采购时间')
    fault_time = models.DateField(null=True, blank=True, verbose_name='故障时间')
    status = models.CharField(max_length=12, choices=STATUS, default='空闲中', verbose_name='手机状态')

    def __str__(self) -> str:
        return f'{self.model}/{self.serial_number}'
    
    class Meta:
        verbose_name = '测试手机管理'
        verbose_name_plural = verbose_name


class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='手机借用人')
    phone = models.ForeignKey(Phone, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='借用的手机')
    borrow_date = models.DateTimeField(auto_now_add=True, verbose_name='借用时间')
    return_date = models.DateTimeField(null=True, blank=True, verbose_name='归还时间')

    def __str__(self) -> str:
        return f'{self.user.get_username}/{self.phone.model}'
    
    class Meta:
        verbose_name = '手机借用/归还记录'
        verbose_name_plural = verbose_name
