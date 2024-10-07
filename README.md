# The Cardinal System

### What is the Cardinl-System

Cardinal is a fan-made project that aims to recreate cardinal's management system within the Sword Art Online anime, removing its gameplay-focused features and moving more on the more managerial activities, such as moderation, user management and information gathering and processing. As you can tell [here](https://github.com/KemonoBAT4/cardinal-system/blob/dev/docs/TODO.md) there are so much work to do so there is not a release date yet.

I will be putting out an Alpha of the project when at least the core features are completed.

### Cardinal Base Functions
For now cardinal will only start a thread for the api to check basic functionality of the flask env.
Then will be implemented the Logger inside cardinal.

## Getting Started
### How to run Cardinal

 - install all the requirements with ```pip install -r requirements.txt```
 - run the program with ```python run.py```

### Idea of the project

Cardinal will listen for any data received or sent by the API and gather this data to train the AI model. 
The API will be structured to generate and send code snippets that aim to help users interface with the world of coding. 
Before training the model with the generated code, the code will be passed to another already-trained AI that will scan for errors. 
If errors are found in the code, or if the user reports that the code snippet is incorrect, the AI will retrain itself 
to fix errors and improve its database. Of course, users can send code snippets to the API, ensuring first that the code is correct, 
and then providing a specific description of what the code does. After that, the AI will check once more if the code is correct and report
any errors to the user if needed. The user can still force the code to be accepted as correct by the AI model for training purposes.


### Contribute the project
 
If you have access to this repository you are free to fork the dev branch.
When you are done developing pls make a pull request [here](https://github.com/KemonoBAT4/cardinal-system/pulls) providing all the changes you made
