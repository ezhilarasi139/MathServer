# Ex.05 Design a Website for Server Side Processing
## Date: 10.11.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

```
math.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rectangle Area Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        label {
            font-weight: bold;
            color: #333;
        }
        input {
            padding: 8px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            text-align: center;
        }
        .error {
            color: red;
            font-size: 14px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Rectangle Area Calculator</h1>

        <!-- Form to input length and breadth -->
        <form method="POST">
            {% csrf_token %}
            <label for="length">Length (in mm):</label>
            <input type="text" id="length" name="length" value="{{ l }}">
            <label for="breadth">Breadth (in mm):</label>
            <input type="text" id="breadth" name="breadth" value="{{ b }}">
            <button type="submit">Calculate Area</button>
        </form>
        <!-- Display the result if area is calculated -->
        <div class="result">
            <h2>Result:</h2>
            <p>The area of the rectangle is: <strong>{{ area }}</strong> square millimeters (mm²).</p>
        </div>
        <!-- Display an error message if there is one -->
        {% if error %}
            <div class="error">
                <p>{{ error }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>

veiws.py

from django.shortcuts import render
def rectarea(request):  
    context = {}
    context['area'] = "0"
    context['l'] = "0"
    context['b'] = "0"
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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/', views.rectarea, name="areaofrectangle"),
    path('', views.rectarea, name="home"), 
]

```
## SERVER SIDE PROCESSING:
![alt text](<Screenshot (46).png>)


## HOMEPAGE:

![alt text](<Screenshot (47).png>)

## RESULT:
The program for performing server side processing is completed successfully.
