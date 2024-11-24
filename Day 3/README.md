## COMMAND ## 


# Deploy a sample service
docker service create --name app1 --replicas 3 --publish 8000:80 kiran2361993/rollingupdate:v10

# Scale the service up
docker service scale app1=6

# Scale the service down
docker service scale app1=1

# Deploy service only on worker nodes
docker service create --name app1 --constraint node.role==worker --replicas 6 --publish 8000:80 kiran2361993/rollingupdate:v10

# Deploy a global service (runs on every node)
docker service create --name monitor --publish 9100:9100 --mode global prom/node-exporter

docker service create --name cadvisor --publish 8888:8080 --mode global google/cadvisor:latest



# Check service tasks
docker service ps app1

# Put a node in maintenance mode
docker node update <node-id> --availability drain

# Reactivate a node
docker node update <node-id> --availability active

