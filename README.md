# Emu5GNet : An Open-Source Emulator for 5G Software-Defined and NFV Networks
This emulation environment has been created to allow researchers/industrials to develop and deploy applications in complex 5G network architecture (SA and NSA) for enabling both emulations of the network and data processing in realistic E2E scenarios. They can propose and evaluate new solutions for future 5G networks, whatever the use case considered: Internet of Things, vehicular communication networks, railway communication networks, augmented reality, etc. Emu5GNet allows the execution of 5G RAN and Core using Mininet-Wifi environment and [containernet](https://containernet.github.io/). The 5G RAN and Core can be packed inside docker containers. Emu5GNet also allows the integration of full ETSI NFV compliant infrastructure based on [vim-emu] (https://github.com/containernet/vim-emu) platform. This last integration of an enhancement of **vim-emu** enables the interconnection of Mininet-Wifi Access points and vim-emu datacenters and, allows the network functions migration across edge datacenters.

## Acknowledgement
This environment has been developed within the project “5G for future RAILway mobile communication system” (5GRAIL). This project has received funding from the European Union’s Horizon 2020 research and innovation program, under grant agreement No 951725.

## Cite this work
If you use the emulation environment during your research and/or for your publications, please cite the following paper as reference to Emu5GNet :

> T. Sylla, L. Mendiboure, M. Berbineau, R. Singh, J. Soler and M. S. Berger, "Emu5GNet: an Open-Source Emulator for 5G Software-Defined Networks," 2022 18th International Conference on Wireless and Mobile Computing, Networking and Communications (WiMob), 2022, pp. 474-477, doi: 10.1109/WiMob55322.2022.9941588.

## Getting started with Emu5GNet VM
The Emu5GNet virtual machine aims to help the future users to quickly start working with this emulated 5G multi-connectivity and Edge Computing environment. Due to versions upgrades, installing the environment from scratch is a challenging task. For more details on the platform, please refer to this paper : [Emu5GNet](https://ieeexplore.ieee.org/document/9941588).

1. Download the Emu5GNet VM from this [link](https://mega.nz/file/RB5jyL5J#qudKffPlHrlWxocBUFW5SLknEtKcpy4Vp3T5UmOiJbw) and import it to VirtualBox. You can also create a VMWare VM using only the disk file in vmdk format. We recommend to keep the VM configuration as given : 4 vCPU, 16 Gb and 80 Gb storage. 
2. The VM is provided with two examples of multi-connectivity 5G/Wifi. These examples are located in the ~/mn-wifi-cnet-vimemu-install/codes_example directory. To keep testbed working smoothly and to not have troubles with paths, an environment variable TESTBED_DIR with emulation code directory path have been coded in hard in the ~/.bashrc file.
3. At the VM startup, you need to run the custom Linux static routing commands in order to enable communication between the different component of the emulation environment : such as Mininet-Wifi and Open5GS, and Open5GS tunnel towards Internet. We created two scripts to do these tasks. To do so, open a terminal and run the following script :
```
cd ~/mn-wifi-cnet-vimemu-install
sudo ./setup_host_network_interfaces_for_emu.sh 
sudo ./5gs_tun_setup.sh 
```
4. Start the Open5GS 5GC core container named open5gsl with running command in a new terminal :
```
docker start -i open5gsl 
```
The username and password are admin/admin.
5. Once logged inside the Open5GS 5G core container, you need to configure the IPv4 routing to enable Open5GS establishing Internet connection for 5G UE. You need to also setup NAT for Open5GS Tunnel and an IP address in the docker range (172.20.0.0/16). This IP address will be configured on the Open5GS-UPF for PDU session management. We prepared a script for this task : startup_config.sh  :
```
sudo ./startup_config.sh
```
After running this script, check if the following IP addresses are configured :
```
eth0@xxxxx : 172.20.0.2 (Container and AMF, etc.) and 172.20.0.10 (UPF)
ogstun : 10.45.0.1/16 and 2001:db8:cafe::1/48.
```
6. 5G and Wifi basic scenario :

You are ready to run you first example. Use Visual Studio Code to visualize the python script named multi_connectivity_5G_wifi.py inside the codes_example directory. This code follow a general Mininet/Mininet-Wifi and Containernet code structure. If you are not familiar with these environments, please read their documentations and examples : [Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet), [Mininet-Wifi](https://usermanual.wiki/Pdf/mininetwifidraftmanual.577244160/html), [Containernet](https://github.com/containernet/containernet/wiki/Tutorial:-Getting-Started).
Once done, start the emulation in a new terminal :
```
sudo python multi_connectivity_5G_wifi.py
```
Once the emulation is successfully launched, open a terminal for node named car1 from mininet term :
```
xterm car1
```
Display network interfaces and Ping Internet using the UERANSIM 5G UE interface uesimtun0 :
```
ifconfig
ping -I uesimtun0 8.8.8.8
```
You can find out more about the UERANSIM 5G UE tools (nr-ue, nr-cli) [here](https://github.com/aligungr/UERANSIM/wiki/Usage).
Let play with Wifi connection also. Check the Wifi connectivity :
```
iw dev car1-wlan0 link 
```
If the Wifi is connected, ping the wifi gateway : 
```
ping -I car1-wlan0 192.168.0.1
```
Display the routing table to see the different routes :
``` ip route ```

7. 5G and Wifi VANET scenario using SUMO simulator for train communications : 
We prepare a script for VANET+SUMO 5G based network emulation. 

You can this code multi_connectivity_5G_wifi_sumo.py and see the results.

8. UE configuration for Open5GS
In this VM you have 10 5G UE configured in the UDM of Open5GS. These UE (t1 to t10) are configured with UERANSIM and their configurations are located under UERANSIM config directory : ~/mn-wifi-cnet-vimemu-install/ueransim/UERANSIM/config. The UE keys were generated using [Ki/OPc Generator](https://github.com/PodgroupConnectivity/kiopcgenerator) tool.
So you can generate the number of 5G UE you want and register in Open5GS UDM. To do so, proceed as follow. 
  - Open the web browser and enter : http://172.20.0.02:8080/
  - Enter username : admin and password : 1234
  - Then add a new UE.
 9. After each run, you need to clean docker containers created by containernet library integrated within the testbed. We prepared a script for this cleaning task and create an alias for it. Run the ```clean``` command to clean mininet and docker.
Enjoy research with **Emu5GNet** !!!
 
## Environment installation and configuration  step by step
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

https://hub.docker.com/r/tidiosky/5grail-wp6-repo
