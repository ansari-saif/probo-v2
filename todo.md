trade wala nahi chal rha yaarrr ....
call get user balance api
toast on order

containerized all services
    backend
    websocket
    consuemrs
    frontend

go through all k8 session and done it  your self
    https://github.com/codes30/k8s-week-3
    https://projects.100xdevs.com/tracks/kubernetes-1/Kubernetes-Part-1-1
    --https://github.com/code100x/staging-ops/tree/main

docker run -p 8000:8000 --env-file ../.env probo-backend
docker run -p 3000:3000 probo-fronted


backend docker build {cm:2024-11-13}
frontend docker done {cm:2024-11-13}
websocket docker build {cm:2024-11-13}
consumers docker build

push to dockerhub
deploy to k8
change urls 
deploy again