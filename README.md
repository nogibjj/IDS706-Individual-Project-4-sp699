![Sentiment Analysis CICD](https://github.com/nogibjj/IDS706-Individual-Project-4-sp699/actions/workflows/cicd.yml/badge.svg)</br>
# IDS-706-Data-Engineering :computer:

## Individual Project 4 :page_facing_up:

## :ballot_box_with_check: Requirements
* __`README.md`__: This should clearly explain what the project does, its dependencies, how to run the program, and conclude with actionable and data-driven recommendations to a hypothetical management team.
* __`GitHub Repo`__: A complete GitHub Repo that contains all required scripts and documentation to run your application.
* __`Flask App`__: Achieve functionality within Docker or a platform, and creativity and sophistication are particularly recognized for successfully embedding a functioning Large Language Model within a Flask application.
* __`Use of DockerHub (Or equivalent)`__: Hosting your functioning container on DockerHub.
* __`Azure Web App (Or equivalent)`__: Successfully deploying your container via Azure Web App to a public endpoint. This can be done either directly from Docker or through Azure container registry.
* __`Video Demo`__: A YouTube link in README.md showing a clear, concise (2-5min) walkthrough and demonstration of your application.

## :ballot_box_with_check: To-do List
* __Flask App__: Learn web application development, server-side scripting, and integration of advanced features like Large Language Models.
* __Docker Hub__: Functionality within Docker or a platform is assessed, and embedding a functioning Large Language Model in Flask is valued for creativity and sophistication.
* __Azure Web App__: Learn cloud-based application hosting, scaling, and management, along with integrating cloud services and mastering deployment strategies through the use of Azure Web App.

## :ballot_box_with_check: Web Application
`Sentiment Analysis`
 Sentiment analysis is a natural language processing technique used to determine the emotional tone behind words, enabling the understanding of attitudes, opinions, and emotions expressed in written language. It's commonly applied in business and social media monitoring to gauge public opinion and customer feedback.</br>
1. Index
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/243a70e3-634b-46a4-8c0c-e99037a35d0c)</br>
2. Positive Sentiment
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/4b5bf09b-f4c9-47f2-9a1f-3af34bd3de5b)
![image](https://github.com/nogibjj/IDS706-Mini-Project-1-sp699/assets/143478016/ee522be0-50a9-45f1-a418-5b0264d5fe96)
3. Negative Sentiment
![image](https://github.com/nogibjj/IDS706-Individual-Project-4-sp699/assets/143478016/35792936-791a-4abe-9e96-563c544a321e)
![image](https://github.com/nogibjj/IDS706-Individual-Project-4-sp699/assets/143478016/62a68c34-4e49-4b62-a2d2-66c461d837d0)


## :ballot_box_with_check: Main Progress
#### `Section 1` Rust Source Code with SQLite Database
##### Create Rust source code to perform CRUD operations on an SQLite database.
* `lib.rs`
  - __extract__: Read the CSV file using the file's link.
  - __transform__: Convert the CSV data to a format suitable for the database.
  - __create__: Insert data into the database.
  - __read__:  Retrieve all entries from the database.
  - __update__: Modify existing entries in the database.
  - __delete__: Remove specific entries from the database.
* `main.rs`
  - Extract the CSV file, convert it to a database file, and then perform CRUD operations using it.
* `test.rs`
  - Test all the functions in 'lib.rs' and verify that the operations execute correctly.
 
#### `Section 2` Install Dependencies
