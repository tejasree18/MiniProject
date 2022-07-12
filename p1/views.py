from django.shortcuts import render, redirect
import csv


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['name']
        password = request.POST['key']
        with open('C:/Users/vishn/PycharmProjects/MiniProject/p1/utils/user_db.csv', newline='') as cv:
            data = csv.reader(cv)
            next(data)
            for row in data:
                if username == row[0] and password == row[1]:
                    return redirect("selection")
            else:
                return render(request, 'login.html', {'le': "Username or Password incorrect!"})


def selection(request):
    if request.method == "GET":
        return render(request, 'selection.html')
    else:
        epcno = request.POST['epcno']
        item = request.POST['item']
        with open('C:/Users/vishn/PycharmProjects/MiniProject/p1/utils/master.csv', newline='') as cv:
            data = csv.reader(cv)
            next(data)
            for row in data:
                if epcno == row[0]:
                    if item == "1" and row[1] == "Biscuit":
                        res = row[6]
                        if res == "Sealed":
                            res1 = "sealed: \n" + str(row)
                            return render(request, 'display.html', {'res': res1})
                        elif res != "Sealed":
                            res1 = "not sealed: \n" + str(row)
                            return render(request, 'display.html', {'res1': res1})
                    elif item == "2" and row[1] == "Chocolate":
                        res = row[6]
                        if res == "Sealed":
                            res1 = "sealed: \n" + str(row)
                            return render(request, 'display.html', {'res': res1})
                        elif res != "Sealed":
                            res1 = "not sealed: \n" + str(row)
                            return render(request, 'display.html', {'res1': res1})
                    elif item == "3" and row[1] == "Chips":
                        res = row[6]
                        if res == "Sealed":
                            res1 = "sealed: \n" + str(row)
                            return render(request, 'display.html', {'res': res1})
                        elif res != "Sealed":
                            res1 = "not sealed: \n" + str(row)
                            return render(request, 'display.html', {'res1': res1})
            else:
                return render(request, 'selection.html', {'le': "EPC number or Item is invalid!"})


def display(request):
    if request.method == "GET":
        return render(request, 'display.html')
