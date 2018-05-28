from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def index(request):
	t = get_template('regression/index.html')
	html = t.render()
	#return HttpResponse('Regression Home page')
	return HttpResponse(html)

@csrf_exempt
def linear_regression(request):
	if request.method == "POST":
		x_train = json.loads(request.POST.get('x_train', ''));
		y_train = json.loads(request.POST.get('y_train', ''));
		x_test = json.loads(request.POST.get('x_test', ''));
		if(len(x_train)==len(y_train)):
			data = {'X': x_train, 'Y': y_train};
			df = pd.DataFrame(data)
			df['XY'] = df['X']*df['Y']
			df['X2'] = df['X']*df['X']
			df['Y2'] = df['Y']*df['Y']
			X_sum = df['X'].sum()
			Y_sum = df['Y'].sum()
			XY_sum = df['XY'].sum()
			X2_sum = df['X2'].sum()
			Y2_sum = df['Y2'].sum()
			length=len(df.columns)
			intercept=((Y_sum*X2_sum)-(X_sum*XY_sum))/((length*X2_sum)-(X_sum*X_sum))
			coefficient=((length*XY_sum)-(X_sum*Y_sum))/((length*X2_sum)-(X_sum*X_sum))
			for i in range(0,len(x_test)):
				x_test[i]=coefficient*x_test[i]+intercept
			return JsonResponse({'return_flag': 'Success','x_test_result':x_test}, safe=False)
		else:
			return JsonResponse({'return_flag': 'Failure','x_test_result':'length of x_train & y_train are not same'}, safe=False)
		#print("---------------------------")
	else:
		return HttpResponse('1st page')

	
