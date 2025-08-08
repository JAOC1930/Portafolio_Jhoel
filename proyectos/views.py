from django.shortcuts import render, redirect   
from .models import Proyecto, Contacto
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    proyectos = Proyecto.objects.all().order_by('-fecha_inicio')
    return render(request, 'index.html', {'proyectos': proyectos})

# views.py
def detalle_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

@require_POST
def procesar_contacto(request):
    try:
        contacto = Contacto(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            celular=request.POST.get('celular'),
            mensaje=request.POST.get('mensaje')
        )
        contacto.save()
        return JsonResponse({'success': True, 'message': 'Mensaje enviado correctamente'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=400)