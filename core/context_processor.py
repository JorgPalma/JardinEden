from core.models import Categoria

def total_categorias(request):
    return {'total_categorias': Categoria.objects.all()}

def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["precio"])
    return {"total_carrito": total}