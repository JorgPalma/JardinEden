from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Producto, Deposito, Venta, DetalleVenta
from .forms import ProductoForm, DepositoForm, VentaForm
from .carrito import Carrito
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required 


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')
    
def Frutas(request):
    productos = Producto.objects.filter(categoria=2)
    data = {
        'productos': productos
    }
    return render(request, 'core/producto/frutas.html', data)

def Otros(request):
    productos = Producto.objects.filter(categoria=7)
    data = {
        'productos': productos
    }
    return render(request, 'core/producto/otros.html', data)

def Verduras(request):
    productos = Producto.objects.filter(categoria=1)
    data = {
        'productos': productos
    }
    return render(request, 'core/producto/verduras.html', data)

def Comidas(request):
    productos = Producto.objects.filter(categoria=3)
    data = {
        'productos': productos
    }
    return render(request, 'core/producto/comidas.html', data)

@permission_required('core.add_producto')
def proadd(request):
    data = {
        'form': ProductoForm
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
            return redirect(to="prolist")
        else:
            data["form"] = formulario

    return render(request, 'core/producto/proadd.html', data)

@permission_required('core.view_producto')
def prolist(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'core/producto/prolist.html', data)

@permission_required('core.delete_producto')
def prodel(request, id): 
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="prolist")

@permission_required('core.change_producto')
def promod(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="prolist")
        data["form"] = formulario

    return render(request, 'core/producto/promod.html', data)

@permission_required('core.view_deposito')
def bodlist(request):
    depositos = Deposito.objects.all()
    data = {
        'depositos': depositos
    }
    
    return render(request, 'core/bodega/bodlist.html', data)

@permission_required('core.add_deposito')
def bodadd(request):

    current_user = get_object_or_404(User, pk=request.user.pk)

    data = {
        'form': DepositoForm
    }

    if request.method == 'POST':
        formulario = DepositoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            deposito = formulario.save(commit=False)
            deposito.vendedor = current_user

            #Producto
            currentProducto = deposito.producto
            if currentProducto == None :
                print("UnU")
            else:
                idProducto = currentProducto.id
                stockActualP = currentProducto.stock
                asumarP = deposito.cantidadp
                totalP = stockActualP + asumarP
                producto = get_object_or_404(Producto, id=idProducto)
                producto.stock = totalP
                producto.save()

            deposito.save()
            messages.success(request, "¡Depósito realizado con éxito!")
            return redirect(to='bodlist')
        else:
            data["form"] = formulario

    return render(request, 'core/bodega/bodadd.html', data)

@permission_required('core.delete_deposito')
def boddel(request, id): 
    deposito = get_object_or_404(Deposito, id=id)
    #BorrarProducto
    currentProducto = deposito.producto
    if currentProducto == None :
        print("UnU")
    else:
        producto = deposito.producto
        currentStock = producto.stock
        arestar = deposito.cantidadp
        nuevoStock = currentStock - arestar
        producto.stock = nuevoStock
        producto.save();
        messages.success(request, "¡Depósito cancelado con éxito!")

    deposito.delete()

    return redirect(to="bodlist")


def add_cart(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.agregar(producto)
    messages.success(request, "Agregado correctamente al carrito")

    return redirect(request.META['HTTP_REFERER'])
    

def add_cart1(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.agregar(producto)
    return redirect("cart")

def delete_cart(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.eliminar(producto)
    return redirect("cart")

def less_cart(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.restar(producto)
    return redirect("cart")

def less_cart10(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.restar10(producto)
    return redirect("cart")

def add_cart10(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=id)
    carrito.sumar10(producto)
    return redirect("cart")

def clean_cart(request):   
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("cart")

def cart(request):
    return render(request, 'core/carrito.html')

@permission_required('core.add_venta')
def venadd(request):

    current_user = get_object_or_404(User, pk=request.user.pk)

    data = {
        'form': VentaForm
    }

    if request.method == 'POST':
        formulario = VentaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            venta = formulario.save(commit=False)
            venta.vendedor = current_user
            venta.total = 0
            venta.save()

            carrito = request.session.get('carrito')
            for c in carrito:
                current_producto = Producto.objects.get(id=c)
                producto = carrito[c]['producto_id']
                cantidad = carrito[c]['cantidad']
                precio = carrito[c]['precio']
                venta.total = venta.total + precio
                venta.save()
                current_producto.stock = current_producto.stock - cantidad
                current_producto.save()
                detalleventa = DetalleVenta.objects.create(
                    venta= venta,
                    producto = current_producto,
                    cantidad = cantidad,
                    subtotal = precio
                )
                detalleventa.save()
            carrito2 = Carrito(request)
            carrito2.limpiar()
            return redirect('vendetail', venta.idventa)

        else:
            data["form"] = formulario


    return render(request, 'core/venta/venadd.html', data)

@permission_required('core.view_venta')
def venlist(request):
    ventas = Venta.objects.all()
    data = {
        'ventas': ventas
    }
    
    return render(request, 'core/venta/venlist.html', data)

@login_required
def vendetail(request, id):
    venta = get_object_or_404(Venta, idventa=id)

    detalles = DetalleVenta.objects.filter(venta=venta.idventa)

    data = {
        'ventas': venta,
        'detalles': detalles
    }
    
    return render(request, 'core/venta/vendetail.html', data)