from django.shortcuts import render, redirect

from products.models import Product



def index(request):
  products = Product.objects.all()
  context={
     'products' : products
  }
  

  return render(request, "products/index.html", context )


def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        cover = request.FILES.get('cover')

        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            description=description,
            cover=cover
        )
        product.save()
        return redirect('products:index')
    return render(request, 'products/create.html')


def delete_product(request, pk):
   product = Product.objects.get(id=pk)
   product.delete()
   return redirect('products:index')