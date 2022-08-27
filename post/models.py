from django.db import models
# Create your models here.

VALYUTA_CHOICES = (
    ('azn','AZN'),
    ('usd','USD'),
    ('eur','EUR'),
    ('try','TRY'),
    ('rub','RUB'),
)

DELIVERY_CHOICES = (
    ('exw','EXW'),
    ('fca','FCA'),
    ('fob','FOB'),
    ('cif','CIF'),
)

ENDIRIM_CHOICES = (
    ('var','VAR'),
    ('yoxdur','YOXDUR'),
)

PAYMENT_CHOICES = (
    ('öncədən ödəniş','ÖNCƏDƏN ÖDƏNİŞ'),
    ('konsiqnasiya','KONSİQNASİYA'),
)

TRANSPORT_CHOICES= (
    ('avtomobil','AVTOMOBİL'),
    ('dəmir yolu','DƏMİR YOLU'),
    ('dəniz','DƏNİZ'),
    ('hava','HAVA'),
)


class Product(models.Model):
    product = models.TextField(verbose_name="Məhsul", null=True,blank=True,max_length=30)
    
    def __str__(self):
        return self.product
    
class Form(models.Model):
    # product = models.ManyToManyField(Product)
    product = models.ForeignKey(Product, related_name='mehsul', verbose_name='Məhsul',on_delete=models.CASCADE,null=True)
    
    request_number = models.CharField( max_length=10, verbose_name="Sorğu nömrəsi", null=True, blank=True)
    user_id = models.CharField(max_length=10,verbose_name='Müştəri İD', null=True, blank=True)
    datetime = models.DateTimeField(verbose_name="Təklifin qüvvədə olduğu müddət", null=True, blank=True)
    valyuta = models.CharField(max_length=10,choices=VALYUTA_CHOICES,default='azn',verbose_name="Valyuta", null=True, blank=True)    
    miqdar = models.CharField(max_length=10 ,verbose_name="Miqdar", null=True, blank=True)
    price = models.CharField(max_length=10 ,verbose_name="Vahidin qiyməti", null=True, blank=True)
    edv_degree = models.CharField(max_length=10 ,verbose_name="ƏDV drərəcəsi", null=True, blank=True)
    edv_price = models.CharField(max_length=10 ,verbose_name="ƏDV məbləği", null=True, blank=True)
    payment_terms = models.TextField( max_length=14,verbose_name="Ödəniş şərti",choices=PAYMENT_CHOICES,default="konsiqnasiya",null=True, blank=True)
    bank_account = models.CharField(max_length=10 ,verbose_name="Bank hesabı", null=True, blank=True)
    discount = models.CharField(max_length=10, default="var", choices=ENDIRIM_CHOICES,verbose_name="Endirim", null=True, blank=True)
    delivery_condition = models.TextField(max_length=4, default="fca",choices=DELIVERY_CHOICES,verbose_name="Çatdırılma şərti", null=True, blank=True)
    country = models.TextField(verbose_name="Ölkə", null=True, blank=True)    
    city = models.TextField(verbose_name="Şəhər", null=True, blank=True)
    location = models.TextField(verbose_name="Ünvan", null=True, blank=True)
    zipcode = models.CharField(max_length=10,verbose_name="Zip kod", null=True, blank=True)
    delivery_date = models.DateTimeField(verbose_name="Çatdırılma tarixi", null=True, blank=True)
    delivery_cost = models.CharField( max_length=10, verbose_name="Çatdırılma xərci", null=True, blank=True)
    type_transport = models.CharField( max_length=10,default="avtomobil",choices=TRANSPORT_CHOICES, verbose_name="Çatdırılma xərci", null=True, blank=True)
    
    status = models.BooleanField(default=False,verbose_name="Qaralama")
    tesdiq = models.BooleanField(default=False,verbose_name="Təsdiq gözlənilir")

    
    
    def __str__(self):
        return self.user_id
    
    
