from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import *



@login_required(login_url="/accounts/login/")
def index(request):
  products = Product.objects.filter(author=request.user)
  context={
     'products' : products,
  }
  

  return render(request, "products/index.html", context )

# Create product
@login_required(login_url="/accounts/login/")
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        cover = request.FILES.get('cover')
        category_id = request.POST.get('category_id')


        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            description=description,
            cover=cover,
            author=request.user,
            category_id=category_id
        )
        product.save()
        return redirect('products:index')
    
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'products/create.html',context)

# details page
@login_required(login_url="/accounts/login/")
def product_details(request, pk):
   product = Product.objects.filter(id=pk, author=request.user).first()

   if not product:
        return HttpResponse('Product not found')

   return render(request, 'products/detail.html', {'product': product})
  


# update method
@login_required(login_url="/accounts/login/")
def update_product(request, pk):
   product = Product.objects.filter(id=pk, author=request.user).first()
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
   categories = Category.objects.all()
   context = {
       'product': product,
        'categories' : categories
    }
   return render(request, 'products/update.html', context )
       
    

# delete method
@login_required(login_url="/accounts/login/")
def delete_product(request, pk):
    product = Product.objects.filter(id=pk, author=request.user).first()

    if not product:
        return HttpResponse('Product not found')

    product.delete()
    return redirect('products:index')
