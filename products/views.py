
from django.http import HttpResponse
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

# details page
def product_details(request, pk):
   product = Product.objects.filter(id=pk).first()

   if not product:
        return HttpResponse('Product not found')

   return render(request, 'products/detail.html', {'product': product})
  


# update method
def update_product(request, pk):
   product = Product.objects.filter(id=pk).first()
   if not product:
    return HttpResponse("Product not found")
   
   if request.method == 'POST' :
      product.name = request.POST.get('name', product.name)
      product.price = request.POST.get('price', product.price)
      product.quantity = request.POST.get('quantity', product.quantity)
      product.description = request.POST.get('description', product.description)
      if request.FILES.get('cover', product.cover):
         product.cover = request.FILES.get('cover', product.cover)
      product.save()
      return redirect('products:index')

   context = {
       'product': product
    }
   return render(request, 'products/update.html', context )
       
    

# delete method
def delete_product(request, pk):
    product = Product.objects.filter(id=pk, author=request.user).first()

    if not product:
        return HttpResponse('Product not found')

    product.delete()
    return redirect('products:index')
