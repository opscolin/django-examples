from django.contrib import admin, messages
from cmdb.models import BorrowRecord, Phone
from django.http import HttpResponseRedirect
from django.urls import reverse


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'serial_number', 'fault_time', 'create_time', 'status', 'fault_time')
    list_filter = ('brand', 'status')
    search_fields = ('status', 'model', 'serial_number')
    actions = ['apply_for_borrow', 'apply_v2']
    def apply_for_borrow(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(request, '抱歉，每次只能申请一台手机', level=messages.ERROR)
        else:
            if queryset[0].status != '空闲中':
                self.message_user(request, '抱歉，不能选择已故障或者被借走的手机', level=messages.ERROR)
            else:
                obj = queryset[0]
                next_url = '/admin/cmdb/phone/'
                base_url = reverse('cmdb:borrow-phone', kwargs={'pk': obj.id})
                borrow_url = f'{base_url}?next={next_url}'
                return HttpResponseRedirect(borrow_url)
    apply_for_borrow.short_description = '申请借用'

    def apply_v2(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(request, '抱歉，每次只能申请一台手机', level=messages.ERROR)
        else:
            if queryset[0].status != '空闲中':
                self.message_user(request, '抱歉，不能选择已故障或者被借走的手机', level=messages.ERROR)
            else:
                obj = queryset[0]
                next_url = '/admin/cmdb/phone/'
                base_url = reverse('cmdb:borrow-phone-v2', kwargs={'pk': obj.id})
                borrow_url = f'{base_url}?next={next_url}'
                return HttpResponseRedirect(borrow_url)
    apply_v2.short_description = '申请借用V2'


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('phone', 'user', 'borrow_date', 'return_date')
        
# Register your models here.
admin.site.register(Phone, PhoneAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)