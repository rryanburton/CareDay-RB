from django.contrib import admin
from .models import Child, DailyReport, Diapering, Sleeping, Eating
# Register your models here.


class ChildAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'gender', 'birthday',
                    'parent_name', 'parent_email', 'parent_phone']


class DailyReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'child', 'arrival_time',
                    'departure_time', 'mood_am', 'mood_pm']


class DiaperingAdmin(admin.ModelAdmin):
    list_display = ['id', 'dailyreport_id', 'time_diaper',
                    'num_one', 'num_two', 'comments']


class SleepingAdmin(admin.ModelAdmin):
    list_display = ['id', 'dailyreport_id', 'time_slp_start', 'time_slp_end']


class EatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'dailyreport_id', 'time_eat', 'food', 'leftover']


admin.site.register(Child, ChildAdmin)
admin.site.register(DailyReport, DailyReportAdmin)
admin.site.register(Diapering, DiaperingAdmin)
admin.site.register(Sleeping, SleepingAdmin)
admin.site.register(Eating, EatingAdmin)
