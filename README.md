# dockerswarm
#from centos7

#install docker

  curl -sSL https://get.docker.com/ | sh 

  sudo groupadd docker

  sudo gpasswd -a $USER docker

  systemctl start docker

#install docker-compose

  sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

  sudo chmod +x /usr/local/bin/docker-compose

  sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

#with all node
#open firewall port


  sudo firewall-cmd --zone=public --add-port=2377/tcp --permanent

  sudo firewall-cmd --zone=public --add-port=4789/udp --permanent

  sudo firewall-cmd --zone=public --add-port=7946/tcp --permanent

  sudo firewall-cmd --zone=public --add-port=7946/udp --permanent

  sudo firewall-cmd --reload

#with Leader node
#init docker swarm

  docker swarm init --advertise-addr <your_ip>

#with other node

  docker swarm join --token <your_token> <your_Leader_node_ip>:2377

#with Leader node
#find token

  docker swarm join-token -q worker

#ls node

  docker node ls

#with Leader node
#create lebal

  docker node update <your_leader_node_id> --label-add master=true

#show node info

  docker node inspect <your_node_id> --pretty

#run docker-compose.yml

  docker stack deploy --compose-file docker-compose.yml <your_stack_name>

#with all node

  docker ps

#with Leader node
#close stack

  docker stack rm <your_stack_name>
