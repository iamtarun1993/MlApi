
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from datetime import timedelta
import pandas as pd
import urllib.request
import zipfile
import os
import json
from django.http import JsonResponse

def index(request):
    t = get_template('home/index.html')
    html = t.render()
    return HttpResponse(html)

def zerodha_index(request):
	t1 = get_template('home/zerodha_index.html')
	html1 = t1.render()
	# data_csv_frame = pd.read_csv(url);
	return HttpResponse(html1)

def zerodha_main(request):
	url_new=os.getcwd();
	print(url_new)
	csv_file = [f for f in os.listdir(url_new) if f.endswith('.CSV')]

	return HttpResponse(csv_file)


def test(request):
	print("============== Start ===============");
	today = datetime.datetime.now()
	print(today);
	file_date_avail(today);
	print("============== End ===============")
	return HttpResponse("Stock Data Updated");

def file_date_avail(newday):

	filename='EQ'+str(newday.day).zfill(2)+str(newday.month).zfill(2)+str(newday.strftime("%y"))
	url = 'https://www.bseindia.com/download/BhavCopy/Equity/'+filename+'_CSV.ZIP'
	print(url);
	try:
		ret = urllib.request.urlopen(url)
		if (ret.code == 200):
			print("File Found for "+str(newday.strftime('%d/%m/%Y')));
			print("+++++++++++++++++++++++")
			dir_name = os.getcwd()
			print(dir_name);
			print("+++++++++++++++++++++++")
			test = os.listdir(dir_name)
			for item in test:
				if item.endswith(".CSV"):
					os.remove(os.path.join(dir_name, item))
		print("---come file find end -----")
		download_zip(filename,url);
	except urllib.request.HTTPError as err:
		print("error")
		print("No file found for "+str(newday.strftime('%d/%m/%Y')));
		newday=newday-timedelta(1);
		file_date_avail(newday);
	print("--------------------------")
		

def download_zip(filename,url):
	print ("Downloading zip file from BSE..")
	urllib.request.urlretrieve(url, filename+".zip");
	unzip_file_zip(filename)
	print ("Downloading zip file from BSE completed")

def unzip_file_zip(filename):
	zip_ref = zipfile.ZipFile(filename+'.zip', 'r')
	zip_ref.extractall();
	zip_ref.close();
	dir_name = os.getcwd()
	test = os.listdir(dir_name)
	for item in test:
		if item.endswith(".zip"):
			os.remove(os.path.join(dir_name, item))
	#csv_data_read(filename)

def csv_data_top(request):
	url_new=os.getcwd();
	print(url_new)
	csv_file = [f for f in os.listdir(url_new) if f.endswith('.CSV')]
	print(len(csv_file))
	if (len(csv_file)==1):
		url=csv_file[0]
		data_csv_frame = pd.read_csv(url);
		data_csv_frame.drop(['TDCLOINDI','NET_TURNOV','NO_OF_SHRS','NO_TRADES','PREVCLOSE','SC_GROUP','SC_TYPE','LAST'], axis = 1, inplace = True)
		data_csv_frame['CHANGE_PER'] = ((data_csv_frame.CLOSE - data_csv_frame.OPEN)/data_csv_frame.OPEN)*100;
		top_10_profit_stock=data_csv_frame.nlargest(10, 'CHANGE_PER');
		top_10_profit_stock.drop(['OPEN','CLOSE','LOW','HIGH'], axis = 1, inplace = True)
	top_10_profit_stock=top_10_profit_stock.to_json(orient='records');
	return HttpResponse(top_10_profit_stock, content_type='application/json')

def csv_data_bottom(request):
	url_new=os.getcwd();
	print(url_new)
	csv_file = [f for f in os.listdir(url_new) if f.endswith('.CSV')]
	print(len(csv_file))
	if (len(csv_file)==1):
		url=csv_file[0]
		data_csv_frame = pd.read_csv(url);
		data_csv_frame.drop(['TDCLOINDI','NET_TURNOV','NO_OF_SHRS','NO_TRADES','PREVCLOSE','SC_GROUP','SC_TYPE','LAST'], axis = 1, inplace = True)
		data_csv_frame['CHANGE_PER'] = ((data_csv_frame.CLOSE - data_csv_frame.OPEN)/data_csv_frame.OPEN)*100;
		top_10_loss_stock=data_csv_frame.nsmallest(10, 'CHANGE_PER');
		top_10_loss_stock.drop(['OPEN','CLOSE','LOW','HIGH'], axis = 1, inplace = True)
	top_10_loss_stock=top_10_loss_stock.to_json(orient='records');
	return HttpResponse(top_10_loss_stock, content_type='application/json')

def csv_data_all(request):
	url_new=os.getcwd();
	csv_file = [f for f in os.listdir(url_new) if f.endswith('.CSV')]
	print(len(csv_file))
	if (len(csv_file)==1):
		url=csv_file[0]
		data_csv_frame = pd.read_csv(url);
		data_csv_frame.drop(['TDCLOINDI','NET_TURNOV','NO_OF_SHRS','NO_TRADES','PREVCLOSE','SC_GROUP','SC_TYPE','LAST'], axis = 1, inplace = True)
		data_csv_frame['CHANGE_PER'] = ((data_csv_frame.CLOSE - data_csv_frame.OPEN)/data_csv_frame.OPEN)*100;
		all_stock=data_csv_frame
		# all_stock.drop(['OPEN','CLOSE','LOW','HIGH'], axis = 1, inplace = True)
	all_stock=all_stock.to_json(orient='records');
	return HttpResponse(all_stock, content_type='application/json')

def stock_index(request,stock_id):
	t1 = get_template('home/stock_index.html')
	html1 = t1.render()
	print(stock_id)	
	return HttpResponse(html1)

def stock_info(request,stock_id):
	url_new=os.getcwd();
	csv_file = [f for f in os.listdir(url_new) if f.endswith('.CSV')]
	# print(len(csv_file))
	if (len(csv_file)==1):
		url=csv_file[0]
		data_csv_frame = pd.read_csv(url);
		data_csv_frame['CHANGE_PER'] = ((data_csv_frame.CLOSE - data_csv_frame.OPEN)/data_csv_frame.OPEN)*100;
		stock_full_info=data_csv_frame[data_csv_frame["SC_CODE"] == int(stock_id)];
	stock_full_info=stock_full_info.to_json(orient='records');
	return HttpResponse(stock_full_info, content_type='application/json')


