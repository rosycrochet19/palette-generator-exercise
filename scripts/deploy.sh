#!/bin/bash

# Script requires the user running it to have sudo privileges
# Please edit the /etc/sudoers file accordingly using sudo visudo

# Set variables
install_dir=/opt/palette-generator

# Install apt Dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

# Create and source virtual environment
python3 -m venv venv
source venv/bin/activate

# Install pip requirements
pip3 install -r requirements.txt

# Create todo list working directory and make working directory
sudo chown -R $(whoami) /opt
rm -rf $install_dir
mkdir $install_dir
cp -r . $install_dir
cd $install_dir

# Create service script
cat << EOF > ${install_dir}/palette-generator.service
    [Unit]
    Description=Palette Generator
    [Service]
    User=$(whoami)
    WorkingDirectory=${install_dir}
    ExecStart=/bin/bash -c "source ${install_dir}/venv/bin/activate && gunicorn --bind=0.0.0.0:5000 --workers 2 app:app"
    [Install]
    WantedBy=multi-user.target
EOF

# Install the app service script
sudo cp $install_dir/palette-generator.service /etc/systemd/system/

# Start the systemd service
sudo systemctl daemon-reload
sudo systemctl stop palette-generator
sudo systemctl start palette-generator

# Output systemd status
sleep 5
sudo systemctl status palette-generator -l --no-pager