# Cardinal's Structure (W.I.P.)
```
Cardinal/                                           - THE MAIN FOLDER
├── app/                                            - THE APPLICATION FOLDER
|    └── .../
|         ├── static/                               - STATIC FILES (IMAGES & OTHERS)
|         ├── templates/                            - TEMPLATES FOLDER
|         ├── _common.py                            - A COMMMON IMPORT FOR THE PROJECT
|         ├── api.py                                - ONLY API SCRIPT
│         ├── application.cfg                       - APPLICATION CONFIG
│         ├── cli.py                                - THE CLI TO IMPORT DATA
│         ├── forms.py                              - THE APPLICATION FORMS
│         ├── handlers.py                           - GENERIC FUNCTIONS
│         ├── menu.json                             - THE LEFT MENU
│         ├── models.py                             - THE MODELS FOR THE DATA
│         ├── README.md                             - THE APPLICAITON'S DOCUMENTATION
│         └── routes.py                             - MAIN ROUTES
├── core/                                           - THE CORE (not to touch)
|    ├── configs/                                   - THE CARDINAL CONFIGS
|    |    ├── __init__.py
|    |    ├── config.py                             - THE ACTUAL CONFIG SCRIPT
|    |    └── exceptions.py                         - SOME CUSTOM EXCEPTIONS
|    ├── decorators/                                - THE CARDINAL DECORATORS
|    |    ├── __init__.py
|    |    └── decorators.py                         - THE ACTUAL DECORATORS SCRIPT
|    ├── docs/                                      - CARDINAL'S DOCUMENTATION
|    |    ├── documentation/                        - HOW TO USE CARDINAL
|    |    |    ├── Contributing.md                  - HOW TO CONTRIBUTE THE PROJECT
|    |    |    ├── Creating a new Application.md    - HOW TO CREATE A NEW APP
|    |    |    ├── Creating the models.md           - [NOT SUPPORTED YET]
|    |    |    ├── Environment.md                   - HOW TO SETUP THE ENVS
|    |    |    ├── Ideas.md                         - A FILE CONTAINING THE IDEAS
|    |    |    ├── Structure.md                     - THE STRUCTURE FILE
|    |    |    ├── temp-models.json                 - [TEMP FILE]
|    |    |    ├── TODO.md                          - LIST OF TODOS
|    |    |    ├── Understanding the Commands.md    - [TO BE IMPLEMENTED]
|    |    |    └── Versions.md                      - INFOS ABOUT THE VERSIONS
|    |    ├── example/                              - AN EXAMPLE APP (TEMPLATE)
|    |    |    ├── static/
|    |    |    ├── templates/
|    |    |    ├── _common.py
|    |    |    ├── api.py
│    │    │    ├── application.cfg
│    │    │    ├── cli.py
│    │    │    ├── forms.py
│    │    │    ├── handlers.py
│    │    │    ├── menu.json
│    │    │    ├── models.py
│    │    │    ├── README.md
│    │    │    └── routes.py
|    |    └── images/                               - IMAGES FOR THE DASHBOARD
|    |         └── dashboard_example_v-a_0-1-2.png
|    ├── forms/                                     - CARDINAL FORMS FOLDER
|    |    ├── __init__.py
|    |    └── base.py                               - THE BASE FOR THE APPS
|    ├── handlers/                                  - CARDINAL HANDLERS FOLDER
|    |    ├── __init__.py
|    |    └── handlers.py                           - THE HANDLERS
|    ├── models/                                    - CARDINAL MODELS FOLDER
|    |    ├── __init__.py
|    |    ├── base.py                               - THE BASE FOR THE APPS
|    |    └── models.py                             - SOME CUSTOM MODELS
|    ├── system/                                    - THE CORE OF CARDINAL
|    |    ├── __init__.py
|    |    └── startup.py                            - MAIN APPLICATION CLASS
|    └── web/                                       - THE WEB FOLDER
|         ├── icons/                                - ICONS FOLDER
│         │    ├── favicon.ico
│         │    └── icon.png
|         ├── scripts/                              - THE SCRIPTS FOLDER
│         │    ├── index.js                         - THE PAGE COMPON. SCRIPT
│         │    ├── login.js                         - THE LOGIN PAGE SCRIPT
│         │    └── register.js                      - THE REGISTER PAGE SCRIPT
|         ├── styles/                               - THE STYLES FOLDER
│         │    ├── action.css                       - THE ACTION PAGE CSS
│         │    ├── card.css                         - THE CARD PAGE CSS
│         │    ├── index.css                        - THE PAGE COMPON CSS
│         │    ├── login.css                        - THE LOGIN PAGE CSS
│         │    ├── menu_item.css                    - THE MENU ITEMS CSS
│         │    ├── register.css                     - THE REGISTER PAGE CSS
│         │    └── section.css                      - THE SECTION PAGE CSS
|         ├── templates/                            - ALL THE HTML TEMPLATES
│         │    ├── sections/                        - THE SECTIONS HTML
|         │    │    ├── form.html                   - FORM SECTION HTML
|         │    │    ├── grid.html                   - GRID SECTION HTML
|         |    |    └── table.html                  - TABLE SECTION HTML
│         │    ├── action.html                      - THE ACTION TEMPLATE
│         │    ├── card.html                        - THE CARD TEMPLATE
│         │    ├── index.html                       - THE MAIN PAGE TEMPLATE
│         │    ├── login.html                       - THE LOGIN PAGE TEMPLATE
│         │    ├── menu_item.html                   - THE MENU ITEMS TEMPLATE
│         │    ├── register.html                    - THE REGISTER PAGE TEMPLATE
│         │    └── section.html                     - THE SECTION TEMPLATE
|         ├── widgets/                              - THE WIDGET FOLDER
│         │    ├── __init__.py
│         │    ├── _common.py                       - THE COMMON FILE
│         │    ├── calendar.py                      - A CALENDAR FOR THE PAGE
│         │    ├── datatable.py                     - A TABLE FOR THE PAGE
│         │    └── grid.py                          - A GRID FOR THE PAGE
|         ├── __init__.py
|         ├── api.py                                - CARDINAL'S WEB API
|         ├── handlers.py                           - CARDINAL'S WEB HANDLERS
|         ├── menu.json                             - CARDINAL'S DEFAULT MENU
|         ├── menu.py                               - CARDINAL'S WEB MENU
|         ├── pages.py                              - PAGE CREATIONS SCRIPTS
|         ├── routes.py                             - CARDINAL'S WEB ROUTES
|         └── users.py                              - W.I.P.
├── .gitignore
├── application.cfg                                 - CARDINAL DEFAULT CONFIG
├── cardinal.log                                    - SIMPLE LOGGER (W.I.P.)
├── database.sh                                     - DATABASE HANDLER EXEC
├── deploy.sh                                       - DEPLOY RUNNER EXEC
├── docker-compose.yml
├── dockerfile
├── LICENCE.txt                                     - THE LICENCE
├── README.md                                       - MAIN README
├── requirements.txt
├── run.py                                          - MAIN RUNNER
└── run.sh                                          - MAIN RUNNER EXEC
```
#