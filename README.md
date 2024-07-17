# The Cardinal System
A program that can upgrade itself, maintain and fix in case of errors, with ai help


## How does it work

When starting the programm, cardinal will start some threads for each of theese scripts:
 - Logger
 - Flask Api
 - Ai Model trainer
 - Ai Model tester
 - other (to be implemented)

After that Cardinal will listen if the api has recieved or sent some data and gather 
them inside the model to train the ai. The api will be structured to generate and
send code snippets that aim to help a user to interface the world of coding.
before training the model with the generated code, the code will be passed to another ai
already trained that will scan the code to find errors. If the errors are found about the code
or if the user says that the code snippet is coded wrongly, the ai will retrain itself to fix errors
and improve their database. Of course the user can send code snippets to the api ensuring first that 
code is correct, and then providing a specific description of what the code does.
After that the ai will check once more if the code is correct and report some errors to the user if needed.
The user can still force the code to be passed as true to the ai model to train

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
