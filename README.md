#### How to Use the Adhoc Python Environment 

Purpose: The adhoc python environment provides a quick way to do analysis with python and allows for a connection to our snowflake data. This allows one to easily do machine learning with sklearn, build visuals with seaborn or matplotlib or do analysis with scipy. It is also easy to set up and will ensure that code that is created on one person's machine can be run on another person's machine without dependecy issues. As long as both people have the same datateam-env file and the same version of python, the code will run the same.

Setup: This environment relies on pyenv to manage python versions and poetry to manage package versions so both of those will need to be installed.

#### download this github repo and navigate to the folder datateam-python-env
`git clone git@github.com:tasty-data/datateam-python-env`


#### Setup pyenv
Pyenv should already be installed if one followed the current onboarding instructions. However, these have changed and people's machines are different so that may not be true.

1. Check if pyenv is installed. If pyenv is installed the below line will run and you can skip to section "Setup poetry".:
`pyenv --version`

2. Install pyenv with brew by following the below instructions:\
https://github.com/pyenv/pyenv

3. Follow the instructions for Zsh in the section "Set-up Your Shell Environment for pyenv":\
https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv

4. Now you should be able to install a version of python. Confirm by running the below line which is the version of python the poetry shell is using:\
`pyenv install 3.11.11`

5. Then create a shell with the version of python you want. I like to work out of python shells because it is the first level pyenv checks when determining what version of python to use. Once you create the shell you will be running the version of python you specify:\
`pyenv shell 3.11.11`


#### Setup venv
1. venv should be already installed on your machine. To confirm this create the empty datateam virtual environment that we will install packages to
`python3.11 -m venv datateam-env`

If venv is not installed run 
`pip3 install virtualenv`

then run 

`python3.11 -m venv datateam-env`

#### Activate your virtual environment
source <YOUR DIRECTORY>/datateam-env/bin/activate

You should see the environment name "datateam-env" pop up in your terminal. This is needed before you install packages to the venv to ensure that the packages install in the right place.

<img width="818" alt="image" src="https://github.com/user-attachments/assets/53aaac21-5b0a-4af8-bebc-b256800efe88" />



#### install packages to venv and test it
1. Now that we have our virtual environment and our correct version of python, we just need to download the requirement.txt packages to the virtual environment.
`pip install -r requirements.txt`

2. Then run the test script. You will have to do 2FA via Duo. You should see your version of python followed by 10 rows of marts.fct_trades.
`python test_adhoc_env.py`

Check that you have the correct environment selected by navigating to the select interpreter section in the top middle and ensuring that 'datateam-env' is selected. The interpreter is also visable on the bottom right and that should also say "datateam-env".

![Screenshot 2025-03-18 at 10 19 01 AM](https://github.com/user-attachments/assets/01dc6f37-ae52-47a4-ba25-f8dbd9ff8abe)

![image](https://github.com/user-attachments/assets/b1e63bdb-e109-4e5e-b3cf-ad7a5ee1d862)



#### Note
To be able to connect to snowflake: you need environmental variables set up in your .zshrc. Go into your .zshrc which is in your root directory and add the following lines: \
Replace the username and password with your own.
`export SNOWFLAKE_ACCOUNT="wfa25515.us-east-1"` \
`export SNOWFLAKE_USER="your username"` \
`export SNOWFLAKE_PASSWORD = “your password"`

Then run `source .zshrc` in your terminal to reload your zshrc.

Also ensure your Code/snowflake_connector.py file is set up correctly. There are instructions for this in the onboarding script.

#### What should I do if I have the old poetry python environment set up.
The steps are very similar and you should already have pyenv and venv installed. 
1. Remove the pyproject.toml and then poetry.lock
2. Add the requirements.txt from this github repo to the location you are running adhoc python analyzes if it is different from this repo. You may need to add manually.
3. Run the lines that install the newest version of python and then install the virtual environment. Test by running a python script where you connect to snowflake.
`pyenv install 3.11.11`

`pyenv shell 3.11.11`

`python3.11 -m venv datateam-env`

`pip install -r requirements.txt`





