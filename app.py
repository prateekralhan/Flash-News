from flask import Flask,render_template,request
#from newsapi import NewsApiClient
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error 
#while parsing #the link to download the article.
 
app = Flask(__name__)
 
#nltk.download('punkt')

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
googlenews = GoogleNews(period = 'd') 

 
@app.route('/')
def home():
    return render_template('home.html',news='')
 
  
@app.route('/results/',methods=['POST']) 
def get_results():
    googlenews.search(request.form['keyword'])
    result=googlenews.result()
    df=pd.DataFrame(result)
    #print(df.head())ss
    """
    for i in range(2,20):
        googlenews.getpage(i)
        result=googlenews.result()
        df=pd.DataFrame(result)
    """
    list=[]
    for ind in df.index:
        dict={}
        article = Article(df['link'][ind],config=config)
        try:
            article.download()
            article.parse()
            article.nlp()
        except:
            continue

        dict['Date']=df['date'][ind]
        dict['Media']=df['media'][ind]
        dict['Title']=article.title
        #dict['Article']=article.text
        #dict['Summary']=article.summary
        dict['Link']=df['link'][ind]
        list.append(dict)

    return render_template('index.html',news=list)#news['articles'])
 
 
if __name__ == "__main__":
    app.run(debug=True)