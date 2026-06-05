from django.shortcuts import render
from datetime import datetime
import zoneinfo

def relogio(request):
    agora = datetime.now(tz=zoneinfo.ZoneInfo('America/Sao_Paulo'))

    contexto = {
        'hora': agora.strftime('%H:%M:%S'),
        'data': agora.strftime('%d/%m/%Y'),
        'dia_semana': agora.strftime('%A'),
    }

    return render(request, 'mywatch/index.html', contexto)