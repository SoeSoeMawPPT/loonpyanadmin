from django.shortcuts import render


class ProductView():
    def list(request):
        return render(request,'inventory/productlist.html')

    def create(request):
        return render(request,'inventory/productcreate.html')