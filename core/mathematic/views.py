from django.shortcuts import redirect, render
from django.views import View
from .forms import CalculatorForm
from django.contrib import messages
from .worker import add_numbers, divide_numbers, minus_numbers, multiple_numbers
from task.models import UserTask
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
                task = multiple_numbers.delay(first_number, second_number)
                UserTask.objects.create(
                    user = request.user,
                    task_id = task.id,
                    task_type = operation,
                    status = task.status,
                    result = task.result
                )
            elif operation == "j":
                task = add_numbers.delay(first_number, second_number)
                UserTask.objects.create(
                    user = request.user,
                    task_id = task.id,
                    task_type = operation,
                    status = task.status,
                    result = task.result
                )
            elif operation == "t":
                task = divide_numbers.delay(first_number, second_number)
                UserTask.objects.create(
                    user = request.user,
                    task_id = task.id,
                    task_type = operation,
                    status = task.status,
                    result = task.result
                )
            elif operation == "m":
                task = minus_numbers.delay(first_number, second_number)
                UserTask.objects.create(
                    user = request.user,
                    task_id = task.id,
                    task_type = operation,
                    status = task.status,
                    result = task.result
                )
            messages.success(request, "your task successfully recieved and we will process it", 'success')
            return redirect('mathematic:index')
        else:
            messages.error(request, "something went wrong please try again", 'error')
            return redirect('mathematic:calculator')


class IndexView(View):
    def get(self, request):
        return render(request, 'mathematic/index.html')