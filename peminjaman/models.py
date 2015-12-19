from django.db import models
from django.contrib.auth.models import User
import datetime

class Pengarang(models.Model):
    nama = models.CharField(max_length=75)
    
    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Pengarang"
        verbose_name_plural = "Data Pengarang"


class Anggota(models.Model):
    username = models.ForeignKey(User)
    nama = models.CharField(max_length=75)
    alamat = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Anggota"
        verbose_name_plural = "Data Anggota"


class Telepon(models.Model):
    nomer = models.CharField(max_length=15)
    anggota_id = models.ForeignKey(Anggota)
    
    def __str__(self):
        return self.nomer
    
    class Meta:
        verbose_name = "Telepon"
        verbose_name_plural = "Data Telepon"


class Pustaka(models.Model):
    judul = models.CharField(max_length=75)
    jenis = models.CharField(max_length=75)
    penerbit = models.CharField(max_length=75)
    tahun = models.CharField(max_length=4)
    data_pengarang = models.ManyToManyField(Pengarang)

    def __str__(self):
        return self.judul
    
    class Meta:
        verbose_name = "Pustaka"
        verbose_name_plural = "Data Pustaka"


class Pinjam(models.Model):
    STATUS = (
        (0, "Belum Kembali"),
        (1, "Sudah Kembali"),
    )
    anggota = models.ForeignKey(Anggota, verbose_name="Peminjam")
    data_pustaka = models.ManyToManyField(Pustaka)
    tanggal_pinjam = models.DateField()
    tanggal_kembali = models.DateField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.anggota.nama
    
    def status_peminjaman(self):
        if self.status == 0:
            isTelat, telat = self.telat()
            if isTelat:
                return "Belum kembali (%d hari)"%(telat.days)
            else:
                return "Belum kembali"
        else:
            return "Sudah Kembali (%s)"%(str(self.tanggal_kembali))

    
    def telat(self):
        batas = datetime.timedelta(7)
        akhir = self.tanggal_pinjam + batas
        jarak = self.tanggal_kembali - akhir
        if self.tanggal_kembali > akhir:
            return True, jarak
        else:
            return False, jarak
    
    class Meta:
        verbose_name = "Pinjam"
        verbose_name_plural = "Data Pinjam"