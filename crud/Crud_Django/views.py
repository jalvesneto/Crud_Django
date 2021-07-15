from crud.forms import LembreteForm
from Crud_Django.models import Lembrete
from django.shortcuts import redirect, render

def index(request):
    lembretes = {}
    lembretes['db'] = Lembrete.objects.all()
    return render(request, 'home.html', lembretes)

def addform(request):
    lembrete = {}
    lembrete['db'] = LembreteForm()
    if request.method == "POST":
        formLemb = LembreteForm(request.POST)
        if formLemb.is_valid():
            formLemb.save()
            return redirect('index')
    return render(request, 'add.html', lembrete)

def editar(request, pk):
    lemb = {}
    lemb['dbs'] = Lembrete.objects.get(pk=pk)
    if request.method == 'POST':
        form = LembreteForm(request.POST or None, instance=lemb['dbs'])
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        lemb['db'] = LembreteForm(instance=lemb['dbs'])
    return render(request, 'add.html', lemb)

def deletar(request, pk):
    lemb = Lembrete.objects.get(pk=pk)
    lemb.delete()
    return redirect('index')

