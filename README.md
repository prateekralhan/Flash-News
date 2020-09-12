# Flash News ✨ ⚡️
A web application which gives us the latest news on the topic of interest of the user from multiple sources scattered across the web! 
## Live app available [here.](https://flash-news-python.herokuapp.com)

![home](https://user-images.githubusercontent.com/29462447/92984399-7b265380-f4c7-11ea-8c40-5e6ebae60656.png)

<img src="https://user-images.githubusercontent.com/29462447/92984400-7c578080-f4c7-11ea-996d-70a052ad29e8.jpg" data-canonical-src="https://user-images.githubusercontent.com/29462447/92984400-7c578080-f4c7-11ea-996d-70a052ad29e8.jpg" width="350" height="700" />



### Installation:
The command: ***pip install -r requirements.txt*** will do everything for us.

### Usage:
1. Clone this Repository to a directory and navigate to that directory.
2. Run the command: ***python app.py***
3. This will run the web-app on localhost and would look something like this. Feel free to play around with the codes, add more features, beautify it. :wink:

<hr>
<b>NOTE:</b>
 *  The web app only displays the top 10 results of the topic of search by the user. This is because I am making usage of the opensource [GoogleNews] PyPi package which only 
 gives results of first 10 pages once you do the "google search" of anything on the web. You can loop across other pages as well to generate more results but I wanted to limit myself to 10 to keep the web app responsive enough otherwise it would give me a timeout error when I deploy it on Heroku.
 * Sometimes, you may see an **Application Error** as the response for certain search made by you. In this case, refresh the link and try to search again or restart your browser.
 * If you still face any queries, feel free to raise an issue :smile:.
<hr>
