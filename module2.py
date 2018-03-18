from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
import scrapper1 
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Win64dows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

app=Flask(__name__)
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/results' , methods=['GET','POST'])
def google_results():
	weblinks=[]
	if request.method=='POST':
		query_str=request.form['query']
		number_results=request.form['number_results']
		#assert isinstance(query_str, str) #Search term must be a string'
    	#assert isinstance(number_results, int) #Number of results must be an integer'
		escaped_search_term = query_str.replace(' ', '+')
		
		query_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results,'en')
		response = requests.get(query_url,headers=USER_AGENT)
		response.raise_for_status()
		
		 #to check the status of the response
		return scrapper1.parse_results(response.text) 


		
if __name__ == '__main__':
	app.run(debug=True)

 #
