# Emu5GNet : An Open-Source Emulator for 5G Software-Defined and NFV Networks
This emulation environment has been created to allow researchers/industrials to develop and deploy applications in complex 5G network architecture (SA and NSA) for enabling both emulations of the network and data processing in realistic E2E scenarios. They can propose and evaluate new solutions for future 5G networks, whatever the use case considered: Internet of Things, vehicular communication networks, railway communication networks, augmented reality, etc. Emu5GNet allows the execution of 5G RAN and Core using Mininet-Wifi environment and [containernet](https://containernet.github.io/). The 5G RAN and Core can be packed inside docker containers. Emu5GNet also allows the integration of full ETSI NFV compliant infrastructure based on [vim-emu] (https://github.com/containernet/vim-emu) platform. This last integration of an enhancement of **vim-emu** enables the interconnection of Mininet-Wifi Access points and vim-emu datacenters and, allows the network functions migration across edge datacenters.

## Prepare the environment
Follow the getting started instructions with Mininet-Wifi available a https://mininet-wifi.github.io/get-started/. Next, download the VM Image proposed on this page. The VM username/password is wifi. The VM comes with Mininet-Wifi 2.6 version. This version works perfectly with python 3.8 before June 2022 update. Block any update and upgrade requests that will be asked by Ubuntu.

## Installer containernet-wifi + vim-emu compatible
1. sudo apt-get install ansible git aptitude
2. git clone https://github.com/containernet/containernet(1)
3. git clone https://github.com/ramonfontes/containernet
4. remplacer le fichier util/install.sh de containernet(1) par le fichier install.sh de ce dépôt git (3.)
5. installer containernet
6. supprimer le dossier "mininet" installer /usr/local/lib/python3.8/dist-packages/ et copier le dossier mininet de containernet(1) (ignorer cette étape)
7. tester que ça fonctionne

#Installer vim-emu
#Prérequis : version Flask : 2.1.0 et Flask-restful 0.3.9
1. git clone https://osm.etsi.org/gerrit/osm/vim-emu.git
cd ~/vim-emu/ansible
sudo ansible-playbook -i "localhost," -c local install.yml
cd ..
sudo python3 setup.py develop
2. tester la commande vim-emu. Si ça marche pas (erreur emuvim introuvable) c'est que la libraire emuvim doit être replacer
3. se placer dans le repertoir /usr/lib/python3/dist-packages et exécuter : sudo cp -rd /usr/lib/python3.8/site-packages/* .
4. essayer vim-emu
5. copier le fichier mininet_net.py du repertoire mininet de ce répo vers /usr/local/lib/python3.8/dist-packages/mininet/mininet/net.py
6. copier le fichier mn_wifi_node.py du même repertoire vers /usr/local/lib/python3.8/dist-packages/mininet_wifixxxx/node.py

#Integration Open5GS et UERANSIM

