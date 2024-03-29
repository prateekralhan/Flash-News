# Flash News ✨ ⚡️ [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)

A web application which gives us the latest news on the topic of interest of the user from multiple sources scattered across the web! 
## Live app available [here.](https://flash-news-python.herokuapp.com)
<kbd>
<img src="https://user-images.githubusercontent.com/29462447/92984723-e8d37f00-f4c9-11ea-9fee-374cd70f4d88.png" data-canonical-src="https://user-images.githubusercontent.com/29462447/92984723-e8d37f00-f4c9-11ea-9fee-374cd70f4d88.png"/> 
</kbd>

&nbsp;
<kbd>
<img src="https://user-images.githubusercontent.com/29462447/92984721-e709bb80-f4c9-11ea-9298-60fe5475bc77.png" data-canonical-src="https://user-images.githubusercontent.com/29462447/92984721-e709bb80-f4c9-11ea-9298-60fe5475bc77.png"/> 
</kbd>
<p float="center">
<kbd>
<img src="https://user-images.githubusercontent.com/29462447/92984400-7c578080-f4c7-11ea-996d-70a052ad29e8.jpg" data-canonical-src="https://user-images.githubusercontent.com/29462447/92984400-7c578080-f4c7-11ea-996d-70a052ad29e8.jpg" width="350" height="700" />
</kbd>
 &nbsp;
 &nbsp;
<kbd>
<img src="https://user-images.githubusercontent.com/29462447/92984929-c7739280-f4cb-11ea-84aa-3f5ea24aeb99.jpg" data-canonical-src="https://user-images.githubusercontent.com/29462447/92984929-c7739280-f4cb-11ea-84aa-3f5ea24aeb99.jpg" width="350" height="700" />
</kbd>
</p>

### Installation:
The command: ***pip install -r requirements.txt*** will do everything for us.

### Usage:
1. Clone this Repository to a directory and navigate to that directory.
2. Run the command: ***python app.py***
3. This will run the web-app on localhost and would look something like this. Feel free to play around with the codes, add more features, beautify it. :wink:

<hr>
<b>NOTE:</b>
<ul>
<li>The web app only displays the top 10 results of the topic of search by the user. This is because I am making usage of the opensource [GoogleNews] PyPi package which only 
 gives results of first 10 pages once you do the "google search" of anything on the web. You can loop across other pages as well to generate more results but I wanted to limit myself to 10 to keep the web app responsive enough otherwise it would give me a timeout error when I deploy it on Heroku.</li>
<li>Sometimes, you may see an <b>Application Error</b> as the response for certain search made by you. In this case, refresh the link and try to search again or restart your browser.</li>
<li>If you still face any queries, feel free to raise an issue :smile:.</li>
</ul>
<hr>

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build --tag google_news_app .
```
4. Run the docker:
```
docker run --publish 8000:8080 --detach --name bb2 google_news_app
```

This will launch the dockerized app. Navigate to ***localhost:8000*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
