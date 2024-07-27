from django.shortcuts import redirect, render
from django.views import View
from .forms import CalculatorForm
from django.contrib import messages
from .worker import add_numbers, divide_numbers, minus_numbers, multiple_numbers
# Create your views here.


class CalculatorView(View):
    def get(self, request):
        form = CalculatorForm()
        context = {
            'form':form
        }
        return render(request=request, template_name='mathematic/calculator.html', context=context)
    
    def post(self, request):
        form = CalculatorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first_number = cd.get("number1")
            second_number = cd.get("number2")
            operation = cd.get("operation")
            if operation == "z":
                multiple_numbers.delay(first_number, second_number)
            elif operation == "j":
                add_numbers.delay(first_number, second_number)
            elif operation == "t":
                divide_numbers.delay(first_number, second_number)
            elif operation == "m":
                minus_numbers.delay(first_number, second_number)
            messages.success(request, "your task successfully recieved and we will process it")
            return redirect('mathematic:index')
        else:
            messages.error(request, "something went wrong please try again")
            return redirect('mathematic:calculator')


class IndexView(View):
    def get(self, request):
        return render(request, 'mathematic/index.html')