# Emu5GNet : An Open-Source Emulator for 5G Software-Defined and NFV Networks
This emulation environment has been created to allow researchers/industrials to develop and deploy applications in complex 5G network architecture (SA and NSA) for enabling both emulations of the network and data processing in realistic E2E scenarios. They can propose and evaluate new solutions for future 5G networks, whatever the use case considered: Internet of Things, vehicular communication networks, railway communication networks, augmented reality, etc. Emu5GNet allows the execution of 5G RAN and Core using Mininet-Wifi environment and [containernet](https://containernet.github.io/). The 5G RAN and Core can be packed inside docker containers. Emu5GNet also allows the integration of full ETSI NFV compliant infrastructure based on [vim-emu] (https://github.com/containernet/vim-emu) platform. This last integration of an enhancement of **vim-emu** enables the interconnection of Mininet-Wifi Access points and vim-emu datacenters and, allows the network functions migration across edge datacenters.

## Acknowledgement
This environment has been developed within the project “5G for future RAILway mobile communication system” (5GRAIL). This project has received funding from the European Union’s Horizon 2020 research and innovation program, under grant agreement No 951725.

## Cite this work
If you use the emulation environment during your research and/or for your publications, please cite the following paper as reference to Emu5GNet :
- T. Sylla, L. Mendiboure, M. Berbineau, R. Singh, J. Soler and M. S. Berger : Emu5GNet: an Open-Source Emulator for 5G Software-Defined Networks. 18th International Conference on Wireless and Mobile Computing, Networking and Communications, Thessaloniki, Grece, pp. doi. (2022)

## Environment installation and configuration
As this emulation environment allows building complex 5G architecture and data processing scenarios, it's installation require manual and individual element setup.

The original host on which the Emu5GNet has been build has the following specifications : 11th Gen Intel® Core™ i7-1185G7 @ 3.00GHz × 8, 32 GB of RAM and Ubuntu 20.04 as operating system. The python version required is 3.8. But any host with Intel i7 10th Gen and 16 GB of RAM can do the job.

### Prepare the environment
Follow the getting started instructions with Mininet-Wifi available a https://mininet-wifi.github.io/get-started/. Next, download the VM Image proposed on this page. The VM username/password is wifi. The VM comes with Mininet-Wifi 2.6 version. This version works perfectly with python 3.8 before June 2022 update. Block any update and upgrade requests that will be asked by Ubuntu.

#### Step 1 : Install containernet-wifi and make it compatible with vim-emu 
vim-emu is based on Containernet. But the wifi version of Containernet, [Containernet-Wifi](https://github.com/ramonfontes/containernet) adapted from Mininet-Wifi by Ramon Fontes is not compatible with vim-emu. This result in the impossibility to link a vim-emu datacenter to a wifi access point. We solve this problem in order to allow multi-connectivity in a 5G scenario in Emu5GNet.

```
1. sudo apt-get install ansible git aptitude.
2. git clone https://github.com/containernet/containernet (1).
3. git clone https://github.com/ramonfontes/containernet.
4. Replace the file util/install.sh of original Containernet (1) by the file Containernet-Wifi util/install.sh.
5. Build and install Contairnernet. Contairnernet installation instructions can be found [here](https://github.com/ramonfontes/containernet).
6. Remove the mininet installation folder /usr/local/lib/python3.8/dist-packages/mininet et copie the mininet folder from the original Containernet
7. Test if it works. In the case if the code don't run, reinstall by ignoring the step 6.
```

#### Step 2 : Install vim-emu, the NFVI
To be able to make vim-emu run smoothly, the following version of Flask and Flask-restful should be respected : Flask 2.1.0 et Flask-restful 0.3.9.
```
1. git clone https://github.com/tidiosky/vim-emu-wifi
2. cd ~/vim-emu-wifi/ansible
3. sudo ansible-playbook -i "localhost," -c local install.yml
4. cd ..
5. sudo python3 setup.py develop
6. Try the vim-emu command. If the command don't work, i.e. it gives error emuvim not found as result, this mean that emuvim library must be relocated. Go to step 7.
7. Go to /usr/lib/python3/dist-packages and run : sudo cp -rd /usr/lib/python3.8/site-packages/* .
8. Try vim-emu command it should work.
9. Copy the mininet_net.py file from this repository mininet folder to /usr/local/lib/python3.8/dist-packages/mininet/mininet/net.py
10. Copy the file mn_wifi_node.py from the same folder to /usr/local/lib/python3.8/dist-packages/mininet_wifixxxx/node.py, where xxxx is Mininet-wifi version.
```
### A 5G Core and RAN Integration (Open5GS and UERANSIM)

