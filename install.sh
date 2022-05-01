apt update
apt install net-tools
sudo apt install speedtest-cli
sudo apt-get install -y adduser libfontconfig1
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_8.5.1_amd64.deb
sudo dpkg -i grafana-enterprise_8.5.1_amd64.deb
sudo systemctl status grafana-server
sudo systemctl enable grafana-server.service
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
sudo apt-get update
sudo apt-get install grafana-enterprise
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl enable grafana-server.service
apt install mysql-server
clear
mysql-secureinstallation
pip install mysql-connector-python
chmod 777 test.py 
cp test.py /bin/stest.py
ufw allow 3006
sudo systemctl restart mysql
clear
echo “Edit crontab to make this run at boot. With sudo crontab -e and the file location is: /bin/stest.py.”
sleep(1)
echo “Rebooting in 5”
sleep(1)
echo “Rebooting in 4”
sleep(1)
echo “Rebooting in 3”
sleep(1)
echo “Rebooting in 2”
sleep(1)
echo “Rebooting in 1”
sleep(1)
echo “Rebooting”
reboot
