
# TODO: see if this script is actually needed

# setup the virtual env
python3 -m venv venv
source venv/bin/activate

# install python requirements
pip install -r requirements.txt

# install node dependecies
cd apps/Discord_bot
npm install
