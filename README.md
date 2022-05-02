# CSC_493_Travel_Chatbot

Covid has caused trouble in all of our lives, one of the consequences of the ongoing
pandemic is that it has made domestic and international travel much more complicated.
Travelers now have to research each country's COVID restrictions and have to dig
through convoluted and messy government websites to find what restrictions they have
in place. It is hard and time consuming to find the most up to date Covid restrictions
from different countries.

We are proposing a chatbot that can assist travelers by delivering them accurate
information regarding COVID-19 restrictions and cases of a respective country.
Chatbots are widely used in many business industries to increase the efficiency of
communication between the customer and business.
This chatbot will support natural language and will be built with Microsoft Azure’s bot
SDK.

## Deliverables:
● Webapp so users can interact with our chatbot

● chatbot that works and gives accurate information

### Setting/Context:
Working with microsoft azure bot sdk. The project will live on github and be
coded with javascript and react js.
Schedule:

	01/29/22 : Get Microsoft Azure

	02/05/22 : Setup Environment

	02/12/22 : Work on the chatbot

	02/19/22 : Get the bot running

	02/26/22 : Change the bot as needed

	03/05/22 : Work on visualization for the bot

	03/12/22 : Improve bot as needed

	03/19/22 : Verify & Collect Data

	03/26/22 : Cleanup Data

	04/02/22 : Mock run to check implementation

	04/09/22 : Usability testing

	04/16/22 : Fix any issues caught by the users

	04/23/22 : Final testing
	
## Materials:
### Software:
Github, Visual Studio, Microsoft Azure

### Hardware:
PC

## Data:
Waiting on advisor’s response for data
This is a unclean data from google
https://docs.google.com/spreadsheets/d/1Q6Zfp3C6hhUg2V3tUYJPc5RUSElIshd5_Z6k
hvo3wkU/edit#gid=984168076
Looking to get more better and accurate data.

## Problem and Rationale:
The problem we are going to face soon is getting accurate data from trustworthy
sources. We don’t know how the chatbot will react to our data and how long it will
take to train the chatbot. One more thing we are looking forward to making at the
moment is a working chatbot. We need to create it first and check if it is working
as we want it to

## Deploying the bot locally
First clone the directory locally with ssh or https

cd into the directory

once inside the directory create and activate a virtual environment and download all dependencies with 

pip install -r requirements.txt

Once all dependencies are dowloaded open 

CSC_493_Travel_Chatbot/venv/lib/python3.6/site-packages/chatterbot_corpus/corpus.py

change line 58 

from

return yaml.load(datafile)

to

return yaml.load(datafile, Loader=yaml.FullLoader)

Save the file and return to the projects root directory

cd into the bot directory

in the command line type 

python3 chatbot.py

open the local host on your browser.

