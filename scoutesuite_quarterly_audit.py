#SOC2 Quarterly AWS Access Review

git clone https://github.com/nccgroup/ScoutSuite
cd ScoutSuite
virtualenv -p python3 venv
.\\venv\Scripts\activate.bat #Windows
#source venv/bin/activate #macOS
pip install -r requirements.txt
python scout.py --help