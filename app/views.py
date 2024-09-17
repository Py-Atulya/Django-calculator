from django.shortcuts import render

def index(request):
    if request.method == "POST":
        num1 = float(request.POST['first_number'])
        num2 = float(request.POST['second_number'])
        operator = request.POST['operator']

        # print(operator)
        
        if operator == '+':
            result = num1 + num2
            print(result)
            return render(request, 'index.html', {'result': result,'operator':operator})
        elif operator == '-':
            result = num1 - num2
            return render(request, 'index.html', {'result': result,'operator':operator})
        elif operator == '*':
            result = num1 * num2
            return render(request, 'index.html', {'result': result,'operator':operator})
        elif operator == '/':
            if num2 == 0:
                return render(request, 'index.html', {'error': 'Cannot divide by zero'})
            result = num1 / num2
            return render(request, 'index.html', {'result': result,'operator':operator})
        
    return render(request, 'index.html')
