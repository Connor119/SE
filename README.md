# Softeware Engineering: Dublin Bike
[Website: http://3.250.167.223:8989/](http://3.250.167.223:8989/)

## Description
This project designed a website for Dublin Bikes. There are two main pages of this project. 
One offers users a Dublin map that shows each Dublin station's position and status. 
It gives users some suggestions about each station, which include the future bike predictions and weather conditions.
Additionally, the other is a registration page for users to sign in and signup.

## Target
Its potential users are bike commuters and weekend leisure cycler, which is the main user of Dublin bikes.
This website gives these users some suggestions about current and future conditions. 
Users can log in to the website. They will be shown a map full of spots. Each spot represents a station. 
When clicking on these spots. Information about the current weather, available bikes and stands will be given. 
In addition, it gives some predictions about the future. There is a drop_down menu that includes 4 selections. Users can choose the future 4 hours prediction results.
When double click on these spots, the trend of this station will be shown with line charts.

## Structure
![alt text](https://github.com/Connor119/SE/blob/048d77e95d5580c3832b5f3c5783a3e123c4e21c/structure.png)
As the graph shows, our structure design has 5 parts. 
The first part is how data are scrapped. Keep requests and store data from API.

The second part is RDS, which includes our designed 5 tables. 
Four of them store scrap data, dynamic weather, show front end in time update dynamic station, static station and dynamic station.
One is future weather and predicts results, which give the front end prediction result directly and update every one hour.

The third part is machine learning, we use the scrapping result to set up and update the model every hour. 
And the model will be saved as pickle files for the usage of prediction.

The fourth part is according to user behaviour to get predicted data from the RDS. 
Register router and convert the data format to JSON to show at the front end side.

The fifth part shows the data at the front end according to the user behaviour which is the station they choose.

More details will show in the report.

## Feature
The main feature of this project is to make predictions for future bikes based on machine learning. 
It's different from some current websites which just request and get data from existing API.
In addition, the other important feature is updating our models every hour, unlike some websites that make predictions based on old models.
Our project is deployed on AWS RDS and EC2 instance. They can keep running on the cloud which confirms this project gets the most recent data.
What's more, we use Google Map and Chart API to show each station and its trend chart. And we also use jquery to make requests and get data from the RDS.
And the web final design is as follows.
![alt text](https://github.com/Connor119/SE/blob/788d066888cfd96227d868a2a40860cf3ded365b/final_web.png)

## Division
* Qiyan Xuan (33%) 20211258 -- Front End, UI design, Documents and Java Script.
* Boshen Fan (33%) 20211152 -- Back End, Google map API, Google chart API.
* Miao Shi (34%) 20211104 -- Data Analyse, Data Scrap, Deploy scrap and update files and project on the EC2 instance. 
