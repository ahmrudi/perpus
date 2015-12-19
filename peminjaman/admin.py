from django.contrib import admin
from peminjaman import models


class TeleponAnggota(admin.StackedInline):
    model = models.Telepon
    extra = 2

class AnggotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data Anggota', {'fields':['username', 'nama', 'alamat']}),
    ]
    list_display = ('nama', 'alamat')
    inlines = [TeleponAnggota]

class PinjamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Data Pinjam', {'fields':['tanggal_pinjam', 'tanggal_kembali', 'status', 'anggota', 'data_pustaka']})
    ]
    list_display = ('anggota', 'tanggal_pinjam', 'status_peminjaman')
    list_filter = ['tanggal_pinjam', 'tanggal_kembali', 'status']
    action_filter = ['status_peminjaman']
    
admin.site.register(models.Anggota, AnggotaAdmin)
admin.site.register(models.Pengarang)
admin.site.register(models.Pinjam, PinjamAdmin)
#admin.site.register(models.Telepon)
admin.site.register(models.Pustaka)