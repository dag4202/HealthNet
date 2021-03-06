from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from hospital.forms import HospitalForm, DepartmentForm

@login_required
def CreateHospital(request):
    done = False
    if request.method == 'POST':
                
        hospital_form = HospitalForm(data = request.POST,prefix = 'hospital')

        if hospital_form.is_valid():

            profile = hospital_form.save(commit = True)
            done = True
        else:
            print( hospital_form.errors)
    else:
        hospital_form = HospitalForm(prefix = 'hospital')  
    return render(request,'temp.html',{'form':hospital_form , 'done': done})



def CreateDepartment(request):
    done = False
    if request.method == 'POST':
                
        department_form = DepartmentForm(data = request.POST,prefix = 'hospital')

        if department_form.is_valid():

            profile = department_form.save(commit = False)
            done = True
        else:
            print( department_form.errors)
    else:
        department_form = DepartmentForm(prefix = 'hospital')  
    return render(request,'temp.html',{'form':department_form , 'done': done})