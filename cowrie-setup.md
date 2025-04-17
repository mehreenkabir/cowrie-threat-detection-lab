# Cowrie Honeypot Setup Script

# Prerequisites:
# - Ubuntu/Debian or Raspberry Pi
# - Python 3.8+
# - Git installed

# Update package index
sudo apt update

# Install necessary packages
sudo apt install git python3-venv python3-pip -y

# Clone Cowrie from GitHub
git clone https://github.com/cowrie/cowrie.git

# Move into the Cowrie directory
cd cowrie

# Copy the default configuration
cp etc/cowrie.cfg.dist etc/cowrie.cfg

# Create Python virtual environment
python3 -m venv cowrie-env

# Activate the virtual environment
source cowrie-env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Start Cowrie
bin/cowrie start

# Notes:
# - Cowrie listens on port 2222
# - It simulates an SSH server and logs attacker activity

# Logs are stored here:
# ~/cowrie/var/log/cowrie/cowrie.json

# Next:
# Use Filebeat to forward these logs to Splunk
# (see filebeat-config.yml for instructions)
