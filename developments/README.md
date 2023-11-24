# development
## if you want to add a new model:
2 possible ways:
 - please make a new issue -> maintainer can add it
 - please make a pull request -> maintainer can review it

If you make a pull request, please follow the following steps:
 - please add a new model setting in development/models/<new-model>.json
 - To add information in the json file, please also see .template.json.temp and other files

## How to run the command to make leaderboaed:
Usually this opearation is done by maintainers:

Steps:
 - set run_settings/settings.json following settings.json.temp
 - make_run_commands.py
 - run the commands in the terminal
 - make_harness_sh.py
 - make_harness_sh_run_command.py
 - run the commands in the terminal
 - make_leaderboard.py
 