from django.shortcuts import render

def rectarea(request):
    # Initial context for rendering
    context = {}
    context['area'] = "0"
    context['l'] = "0"
    context['b'] = "0"

    # Handle POST request (when the form is submitted)
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')
        print('request=', request)
        print('Length=', l)
        print('Breadth=', b)
        try:
            area = int(l) * int(b)
            context['area'] = area
            context['l'] = l
            context['b'] = b
            print('Area=', area)
        except ValueError:
            context['area'] = "Invalid input"
            context['error'] = "Please enter valid numbers for length and breadth."
    return render(request, 'mathapp/math.html', context)
