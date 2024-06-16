from django.shortcuts import render
from .models import Trainer


def trainer(request):
    trainer = Trainer.objects.all()
    return render(request, 'trainer_app/trainer.html', context={"trainers": trainer})
