from django.shortcuts import render
from django.views import View
from .forms import CalculatorForm
# Create your views here.


class CalculatorView(View):
    def get(self, request):
        form = CalculatorForm()
        context = {
            'form':form
        }
        return render(request=request, template_name='mathematic/calculator.html', context=context)
    
    def post(self, request):
        pass


class IndexView(View):
    def get(self, request):
        return render(request, 'mathematic/index.html')