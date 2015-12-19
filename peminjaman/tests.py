from django.test import TestCase
from peminjaman import models
from datetime import date
from peminjaman.views import PustakaList


class AnggotaTests(TestCase):
    """Anggota model tests."""
    
    def test_str(self):
        
        anggota = models.Anggota(nama="Ahmad Rudi", alamat="Jln Cinta")
        
        self.assertEquals(str(anggota), "Ahmad Rudi")

class PustakaTests(TestCase):
    """Pustaka model tests."""
    
    def test_str(self):
        
        pustaka = models.Pustaka(judul="Pustaka 1", jenis="Fiksi")
        
        self.assertEquals(str(pustaka), "Pustaka 1")

class TeleponTests(TestCase):
    """Telepon model tests."""
    
    def test_str(self):
        
        telepon = models.Telepon(nomer="0888888")
        
        self.assertEquals(str(telepon), "0888888")

class PinjamTests(TestCase):
    """Pinjam model tests."""
    
    def test_str(self):
        
        pinjam = models.Pinjam(tanggal_pinjam = date(2015, 12, 05), tanggal_kembali=date(2015, 12, 06))
        
        self.assertEquals(pinjam.tanggal_pinjam, date(2015, 12, 05))


from django.test.client import Client
from django.test.client import RequestFactory

class PustakaListViewTests(TestCase):
    """Pustaka list view tests."""
    
    def test_pustaka_in_the_context(self):
        
        client = Client()
        response = client.get('/pustaka/')
        
        self.assertEquals(list(response.context['object_list']), [])
        
        models.Pustaka.objects.create(judul="Test Case 1")
        response = client.get('/pustaka/')
        self.assertEquals(response.context['object_list'].count(), 1)
        
        
    def test_pustaka_in_the_context_request_factory(self):
        
        factory = RequestFactory()
        request = factory.get('/pustaka/')
        
        response = PustakaList.as_view()(request)
        
        self.assertEquals(list(response.context_data['object_list']), [])
        
        models.Pustaka.objects.create(judul="Test Case 1")
        response = PustakaList.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
        