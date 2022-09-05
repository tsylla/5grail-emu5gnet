# Comment installer mininet wifi from clean ubuntu

1. sudo apt install mininet
2. sudo apt install git python3
3. sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
4. git clone https://github.com/intrig-unicamp/mininet-wifi
5. cd mininet-wifi
6. sudo util/install.sh -Wlnfv
7. test wifi sudo mn --wifi

# Installer containernet-wifi + vim-emu compatible
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



