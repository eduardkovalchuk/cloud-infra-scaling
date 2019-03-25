# cloud-infra-scaling
Service that simulates CPU load and allows to scale it in order to distribute the load.

Copy project to local machine 
```{bash}
git clone https://github.com/eduardkovalchuk/cloud-infra-scaling.git
cd cloud-infra-scaling
```
Build image and run a container
```{bash}
docker build -t cloud-infra-scaling .
docker run -p 5000:5000 -d cloud-infra-scaling
```
Send POST http request to start job to `localhost:5000/start` with json that has `exec_time` (int time of execution in seconds) and `proc_num` (int number of processes):
Payload:
```{json}
{
	"exec_time": 10,
	"proc_num": 2
}
```
Response:
```{json}
2 processes launched for 10 seconds
```

To check info about running processes send GET http request to `localhost:5000/`:
Response:
```{json}
{
    "19": {
        "exec_time": 10,
        "is_alive": true
    },
    "20": {
        "exec_time": 10,
        "is_alive": true
    }
}
```
