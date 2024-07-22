# note this only works on unix/linux systems
# also not to make this script executable by running the following command in the terminal 

#! chmod +x setup.sh

# run the script on unix/linux system using the following command

#! ./setup.sh

echo 'first let us create a env directory to hold the configuration of our project'
python -m venv env

echo 'now let us activate it the env directory'
source env/bin/activate

echo 'now let us install the dependencies of our project'
pip install -r requirements.txt
