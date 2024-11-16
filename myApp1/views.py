
from django.shortcuts import render, redirect

from myApp1.models import Brand


# Create your views here.

def home(request):
    return render(request,'index.html')



def insert(request):
    return render(request,'insert.html')


def brand(request):
    return render(request,'brand.html')




def insert_data(request):
    brand= Brand.objects.get(pk=id)
    if request.method == "POST":

        brand_name = request.POST['prod_name']
        brand_price = request.POST['prod_price']
        brand_category = request.POST['prod_category']
        brand_qty = request.POST['prod_qty']
        brand_desc = request.POST['prod_desc']
        brand_img = request.FILES['prod_img']

        brand = Brand(
            brand_name=brand_name,
            brand_price=brand_price,
            brand_category=brand_category,
            brand_qty=brand_qty,
            brand_img=brand_img,
            brand_desc=brand_desc,
        )

        brand.save()
        return redirect('/')

    return render(request, 'insert.html', {'brand':brand})

