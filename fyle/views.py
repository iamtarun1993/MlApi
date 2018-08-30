from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
# Create your views here.


def index(request):
	t = get_template('fyle/index.html')
	html = t.render()
	#return HttpResponse('Regression Home page')
	return HttpResponse(html)

@csrf_exempt
def branch_details(request,branch_ifsc):
	url_new=os.getcwd()+"/static/files/banks.csv";
	#print(url_new)
	data_csv_frame = pd.read_csv(url_new);

	ifsc_code=branch_ifsc

	if (len(ifsc_code)==11):
		ifsc_code=ifsc_code.upper();
		bank_full_data=data_csv_frame[data_csv_frame["ifsc"] == ifsc_code];
		if (len(bank_full_data)==1):
			bank_full_data_final =  pd.DataFrame(bank_full_data);
			bank_full_data=bank_full_data.to_json(orient='records')
			return JsonResponse({'Response': 'Success','Brach_Details':json.loads(bank_full_data)}, safe=False)
		else:
			return JsonResponse({'Response': 'Data not found','Brach_Details':[]}, safe=False)
	else:
		return JsonResponse({'Response': 'IFSC not valid','Brach_Details':[]}, safe=False)

@csrf_exempt
def bank_list(request,bank_name,bank_city):
	#print("A")
	bank_name=bank_name.upper();
	bank_city=bank_city.upper();
	url_new=os.getcwd()+"/static/files/banks.csv";
	data_csv_frame = pd.read_csv(url_new);

	bank_full_data=data_csv_frame[(data_csv_frame["bank_name"] == bank_name) & (data_csv_frame["city"] == bank_city)];
	bank_full_data_final =  pd.DataFrame(bank_full_data);
	print("Total Bank Found : " + str(len(bank_full_data)));
	#print(bank_full_data_final)
	if (len(bank_full_data)==0):
		return JsonResponse({'Response': 'No Data Found','Bank_List':[]}, safe=False)
	else:
		'''bank_details=[];
		for i in range(0,len(bank_full_data)):
			#print(bank_full_data.iloc[i]['ifsc'],bank_full_data.iloc[i]['branch'])
			bank_details = bank_details+[{'IFSC CODE': bank_full_data.iloc[i]['ifsc'] ,'BANK NAME': bank_full_data.iloc[i]['bank_name'],'BRANCH': bank_full_data.iloc[i]['branch'],'CITY': bank_full_data.iloc[i]['city'], 'DISTRICT': bank_full_data.iloc[i]['district'], 'STATE': bank_full_data.iloc[i]['state'], 'ADDRESS' : bank_full_data.iloc[i]['address']}];
		bank_details =  pd.DataFrame(bank_details);'''
		print(bank_full_data);
		bank_list=bank_full_data.to_json(orient='records')
		return JsonResponse({'Response': 'Success','Bank_List':json.loads(bank_list)}, safe=False)
	#return JsonResponse({'Response': 'IFSC not valid','Brach_Details':[]}, safe=False)