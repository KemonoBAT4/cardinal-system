# Cardinal System

### What is Cardinal 🔭
The idea of cardinal is to create a program that can help creating a backend structure with a complete dashboard to handle taks, manage possible webistes, bots or handle different datas.
Once its core features are completed, Cardinal will be, with some simple commands, able to completely create new applications in the interface, apply some defaults routes, handle users. Once the application is completed, a single Cardinal project installed will be able to run multiple applications simultaneously without, everything with its own database and configurations, but all on the same core.

### Here's an example of the Dashboard
![Cardinal Example Dashboard](/core/docs/images/dashboard_example_v-a_0-1-2.png)

## How to install Cardinal 🖥️

### Development Branch Installation
In this first version of Cardinal the first way to start as development an application is the following:

- download the application with the command on a terminal `git clone https://github.com/KemonoBAT4/Cardinal-System`
- enter the folder with `cd Cardinal`
- make sure to have the docker engine running

- now its possible to run Cardinal, for a list of arguments possible run `./run.sh --help`
- for a list of all the possible applications run the command `./run.sh app list`
- for a simple setup of an application, before running it, do `./run.sh <application name> setup`
- now its possible to run the command `./run.sh <application name> run`

<!-- - enabled the creation of a dedicated `docker-compose.yml` specific for every application -->

<!-- ## Contribute the project 📋
If you have access to this repository you are free to fork the dev branch to help the project.
When you are done developing pls make a pull request [here](https://github.com/KemonoBAT4/Cardinal/pulls) providing a detailed description of all the changes you made. A complete guide on how to make a standard pull request can be found [here](https://github.com/KemonoBAT4/Cardinal/blob/main/core/docs/Contributing.md). -->

## Versions 🗄️
Right now, Cardinal's version is `Release 1.0.0`, and wil be updated when there is a new important feature added or bugs fixed. More About Versions
[here](https://github.com/KemonoBAT4/Cardinal/blob/main/core/docs/Versions.md).

## Ideas & Suggestions 💡
A complete list of ideas that its currently in development / considered can be found [here](https://github.com/KemonoBAT4/Cardinal/blob/main/core/docs/Ideas.md) and in its related Issues (only for W.I.P. ideas).
