## Изучите [README.md](README.md) файл и структуру проекта.

## Задание 1

![svg](./schemas/C4_container.svg)


## Задание 2

### 1. Proxy

[proxy](src/microservices/proxy)

### 2. Kafka

![tests.png](./screenshot/task2/tests.png)

![topics.png](./screenshot/task2/topics.png)

![consumer.png](./screenshot/task2/consumer.png)


## Задание 3

Команда начала переезд в Kubernetes для лучшего масштабирования и повышения надежности. 
Вам, как архитектору осталось самое сложное:
 - реализовать CI/CD для сборки прокси сервиса
 - реализовать необходимые конфигурационные файлы для переключения трафика.


### CI/CD

[api-tests.yml](.github/workflows/api-tests.yml)

### Proxy в Kubernetes

#### Шаг 1

#### Шаг 2

[events-service.yaml](src/kubernetes/events-service.yaml)
[proxy-service.yaml](src/kubernetes/proxy-service.yaml)
[ingress.yaml](src/kubernetes/ingress.yaml)

#### Шаг 3
![api_movies.png](./screenshot/task3/api_movies.png)
![tests.png](./screenshot/task3/tests.png)
![event_service_logs.png](./screenshot/task3/event_service_logs.png)

## Задание 4

[helm/values.yaml](src/kubernetes/helm/values.yaml)
[helm/templates/services/events-service.yaml](src/kubernetes/helm/templates/services/events-service.yaml)
[helm/templates/services/proxy-service.yaml](src/kubernetes/helm/templates/services/proxy-service.yaml)

![helm_deployment.png](./screenshot/task4/helm_deployment.png)
![api_movies.png](./screenshot/task4/api_movies.png)


# Задание 5

![fortio_distribution.png](./screenshot/task5/fortio_distribution.png)
![fortio_stats.png](./screenshot/task5/fortio_stats.png)
