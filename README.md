# Softeware Engineering: Dublin Bike
[Website: http://3.250.167.223:8080/](http://3.250.167.223:8080/)

## Desciption
This project design a website for Dublin Bikes. There are two main pages of this projet. 
One offers user a Dublin map which shows each Dublin station position and status. 
It gives users some suggestions about each station, which include the future bike predictions and weather conditions.
Additionally, the other is a registration page for user to signin and signup.

## Target
It's potential users are bike commuters and weekend leisure cycler, which is the main user of Dublin bikes.
This webisite give these users some suggestions about current and future condition. 
User can login to the website. They will be shown a map which full of spots. Each spots represent a station. 
When click on these spots. Informations about the current weather, avaliable bikes and stands will be given. 
In addition, it gives some prediction about the futures. There is a drop_down menu which include 4 selections. User can choose the future 4 hours prediction results.
When double click on these spots, the trend of this station will be shown with a line charts.

## Stucture
![alt text](https://github.com/Connor119/SE/blob/048d77e95d5580c3832b5f3c5783a3e123c4e21c/structure.png)
As the graph shown, our structure design have 5 parts. 
First part is how data are scrapped. Keep request and store data from API.

Second part is RDS, which include our designed 5 tables. 
Four of them store scrap data, dynamic weather, show front end in time update dynamic station, static station and dynamic staion.
One is futute weather and predict results, which give the front end prediction result directly and update every one hour.

Third part is the machine learning, we use the scrap result to set up and update model every hour. 
And the model will be saved as pickle files for the usage of predcition.

The fourth part is according to user behaviour to get predicted data from the RDS. 
Register router and convert the data format to JSON to show at the front end side.

The fifth part is show the data at the front end according to the user behaviour which is the station they choose.

The more details will show in the report.

## Feature
The main feature of this project is make predictions for the future bikes based on machine learning. 
It's different from some current websites which just request and get data from exist API.
In addition, the other important feature is update our models every hour unlike some weibsite make prediction based on old models.
Our project are deployed on AWS RDS and EC2 instance . They can keep running on cloud which confirm this project get the most recent data.
What's more, we use Google Map and Chart API to show each stations and their trend chart. And we also use jquery to make request and get data from the RDS.
And the web final design are as follows.
![alt text](https://github.com/Connor119/SE/blob/788d066888cfd96227d868a2a40860cf3ded365b/final_web.png)

## Division
* Qiyan Xuan (33%) 20211258 -- Front End, UI design, Documents and Java Script.
* Boshen Fan (33%) 20211152 -- Back End,Google map API,Google chart API.
* Miao Shi (34%) 20211104 -- Data Analyse, Data Scrap, Deploy scrap and update files and project on EC2 instance. 
