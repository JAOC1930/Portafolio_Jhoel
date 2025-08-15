from django.db import models
from django.urls import reverse
from django.utils import timezone

class Proyecto(models.Model):
    # Información básica
    titulo = models.CharField(max_length=200, verbose_name="Título del proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    
    # Empresa

    empresa = models.CharField(max_length=100, blank=True, null=True, verbose_name="Empresa")

    # Multimedia
    imagen = models.URLField(blank=True, null=True, verbose_name="Imagen principal")
    video_url = models.URLField(blank=True, null=True, verbose_name="Enlace a video")
    
    # Fechas importantes
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_fin = models.DateField(blank=True, null=True, verbose_name="Fecha de finalización")
    
    # Estado (calculado automáticamente)
    ESTADO_PROYECTO = [
        ('EN_PROGRESO', 'En progreso'),
        ('COMPLETADO', 'Completado'),
        ('PAUSADO', 'Pausado'),
        ('PLANEADO', 'Planeado'),
    ]
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_PROYECTO,
        default='EN_PROGRESO',
        editable=False
    )
    
    # Enlaces útiles
    url_demo = models.URLField(blank=True, null=True, verbose_name="URL de demostración")
    url_repositorio = models.URLField(blank=True, null=True, verbose_name="URL de repositorio")
    
    # Tecnologías (texto simple para empezar)
    tecnologias = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Tecnologías utilizadas",
        help_text="Separar con comas"
    )

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        # Actualizar estado automáticamente según las fechas
        if self.fecha_fin:
            self.estado = 'COMPLETADO'
        elif self.fecha_inicio > timezone.now().date():
            self.estado = 'PLANEADO'
        else:
            self.estado = 'EN_PROGRESO'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detalle_proyecto', args=[str(self.id)])

    @property
    def duracion(self):
        """Calcula la duración del proyecto en meses/días"""
        if not self.fecha_inicio:
            return "No definido"
        
        if self.fecha_fin:
            delta = self.fecha_fin - self.fecha_inicio
        else:
            delta = timezone.now().date() - self.fecha_inicio
        
        meses = delta.days // 30
        dias = delta.days % 30
        
        if meses > 0:
            return f"{meses} mes(es) y {dias} día(s)"
        return f"{dias} día(s)"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Email")
    celular = models.CharField(max_length=15, verbose_name="Celular")  # Cambiado a CharField
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_contacto = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de contacto")

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ['-fecha_contacto']  # Ordenar por fecha descendente

    def __str__(self):
        return f"Contacto de {self.nombre} ({self.email})"