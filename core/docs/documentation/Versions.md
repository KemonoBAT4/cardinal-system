# Versions in Cardinal
Here's an explenation of the versions and patches of Cardinal with all the features developed for a specific version or patch.

## Release 1.0.0: (September 6, 2026)
Updated cardinal scripts, with new functionalities:
- new features for the login & register: now properly responds with an error with the action was not completed
- new features for the docker interaciton: now properly stops the container before executing any action (reset or setup)
- new commands for docker: now `./run.sh <project_name> stop` launches a command to stop both the applicaiton and DB containers

## Alpha 0.1.4: (August 24, 2026)
Updated cardinal scripts, with new functionalities:
- implemented docker with a `development` and `production` environment
- all commands are available in the ./run.sh file explanation
- implemented first release for `login`, `register` and `logout` interactions

## Alpha 0.1.3: (May 19, 2026)
Updated cardinal scripts, with new functionalities:
- made a small refactor of cardinal by rebuilding the structure with more organized scripts
- added the possibility to add arguments for customize the runners / setup / deploy & migrate commands
- updated the user dashboard with new widgets being implemented and multiple adjustments on the pages style
- updated some test projects with new implemented features

## Alpha 0.1.2 (May 14, 2025):
Updated cardinal scripts, with new functionalities:
- introduced database support, with a specific string in the `application.cfg`
- implemented sqlalchemy structure with base models + custom models

## Alpha 0.1.1: (January 3, 2025)
Updated cardinal scripts, with new functionalities:
- implemented logging methods for the core
- implemented threads methods for the core
- added new scritps for the configurations

## Alpha 0.1.0: (July 31, 2024)
Base Cardinal setup, no specific routes, no database, just some tests for the basic functionalities for the core



