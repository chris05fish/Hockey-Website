from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from budget.models import BudgetEntry
from budget.forms import BudgetEntryForm
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='/login/')
def budget(request):
	if (request.method == "GET" and "delete" in request.GET):
		id = request.GET["delete"]
		BudgetEntry.objects.filter(id=id).delete()
		return redirect("/budget/")
	else:
		table_data = BudgetEntry.objects.filter(user=request.user)
		sumProjected = 0
		sumActual = 0
		points = 0
		max = 0
		p = ""
		pos = ""
		budgetObjects = BudgetEntry.objects.all()
		for e in BudgetEntry.objects.all():
			sumProjected += e.prediction
			sumActual += e.points
			points += e.points
			if(e.points > max):
				max = e.points
				p = e.player
				pos = e.position
		total = sumActual - sumProjected
		context = {
		"table_data": table_data,
		"total": total,
		"points": points,
		"max": max,
		"p": p,
		"pos":pos,
		"budgetObjects": budgetObjects
		}
		return render(request, 'budget/budget.html', context)

@login_required(login_url='/login/')
def add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = BudgetEntryForm(request.POST)
            if (add_form.is_valid()):
                player = add_form.cleaned_data["player"]
                position = add_form.cleaned_data["position"]
                points = add_form.cleaned_data["points"]
                prediction = add_form.cleaned_data["prediction"]
                user = User.objects.get(id=request.user.id)
                BudgetEntry(user = user, player=player, position=position, points=points, prediction=prediction).save()
                return redirect("/budget/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'budget/add.html', context)
        else:
            #Cancel
            return redirect("/budget/")
    else:
        context = {
            "form_data": BudgetEntryForm()
        }
        return render(request, 'budget/add.html', context)

@login_required(login_url='/login/')
def edit(request, id):
	if (request.method == "GET"):
		# Load Tasks Entry Form with current model data.
		budgetEntry = BudgetEntry.objects.get(id=id)
		form = BudgetEntryForm(instance=budgetEntry)
		context = { "form_data" : form }
		return render(request, 'budget/edit.html', context)
	elif (request.method == "POST"):
		# Process form submission
		if ("edit" in request.POST):
			form = BudgetEntryForm(request.POST)
			if (form.is_valid()):
				budgetEntry = form.save(commit=False)
				budgetEntry.user = request.user
				budgetEntry.id = id
				budgetEntry.save()
				return redirect("/budget/")
			else:
				context = {
				"form_data": form
				}
				return render(request, 'budget/add.html', context)
		else:
			#Cancel
			return redirect("/budget/")
