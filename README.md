# The Cardinal System
A program that can upgrade itself, maintain and fix in case of errors, with ai help


## How does it work

When starting the programm, cardinal will start some threads for each of theese scripts:
 - Logger
 - Flask Api
 - Ai Model trainer
 - Ai Model tester
 - other (to be implemented)

After that, Cardinal will listen for any data received or sent by the API and gather this data to train the AI model. 
The API will be structured to generate and send code snippets that aim to help users interface with the world of coding. 
Before training the model with the generated code, the code will be passed to another already-trained AI that will scan for errors. 
If errors are found in the code, or if the user reports that the code snippet is incorrect, the AI will retrain itself 
to fix errors and improve its database. Of course, users can send code snippets to the API, ensuring first that the code is correct, 
and then providing a specific description of what the code does. After that, the AI will check once more if the code is correct and report
any errors to the user if needed. The user can still force the code to be accepted as correct by the AI model for training purposes.

## TODO List: 
 - Cardinal base functions ( ! ) 1
 - Flask Api ( ! ) 1
 - Logger ( ! ) 3
 - AI Model to train ( ! ) 1
 - AI Model to test ( ! ) 1
 - Web Scraper ( ! ) 5
 - Game Server ( ? ) 10
 - Auth ( ! ) 3
 - Chat with Humans / Cardinal ( ! ) 4
 - Maps ( ? ) 10

#### Legenda:
 1. **?** : not sure;
 2. **!** : must do;
 3. **X** : completed;
 4. **< number >** : priority from 1 (max) to 10 (min)

### Cardinal Base Functions
For now cardinal will only start a thread for the api to check basic functionality of the flask env.
Then will be implemented the Logger inside cardinal.

## Utilities
 - ai model training test: https://www.w3schools.com/python/python_ml_train_test.asp
