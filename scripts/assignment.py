import requests
import logging
import os
import os.path
import pandas as pd


def url_check(url_test, string):
	try:
		response = requests.get(url_test, timeout = 10)
		if response.reason == 'OK':
			htmltext = response.text
			string = str(string).replace("'",'"')
			if string in htmltext:
				statement = 'Content requirements were fulfilled'
			else:
				statement = 'Content requirements were not fulfilled'
		else:
			statement = response.reason
	except:
		statement = 'Request timeout'
		response.elapsed = 'no response'
		response = '<Response [408]>'

	foo = [statement, response.elapsed, response]
	return foo


if __name__ == "__main__":

	##### reads json file as an input file containing http urls and corresponding requirements #####
	path = '/usr/local/airflow/scripts'
	os.chdir(path)
	df = pd.read_json('example.json') 


	##### checking logfile/logfile's folder existence in Docker #####
	path = '/usr/local/airflow/log'
	os.chdir(path)
	file_ex = os.path.exists('logfile.log')
	if file_ex:
		var = "a"
	else:
		var = "w"

	##### logging settings #####
	Format = "[%(asctime)s] [%(levelname)s] - %(message)s"
	logging.basicConfig(filename = "logfile.log",
                    filemode = var,
                    format = Format 
                    )
	logger = logging.getLogger()
	logger.setLevel(20)

	#### re-try if poor connection??? ####
	#### UTF-8 encodding??? (special characters) ####

	lst = []
	for x in df.index:
		lst = url_check(df['url'][x],df['requirement'][x])
		msg = str(lst[2]) + " " + str(df['url'][x]) + " " + str(lst[0]) + " " + str(lst[1])
		if lst[0] == 'Content requirements were fulfilled':
			logger.log(20, msg)
		else:
			logger.log(40, msg)


