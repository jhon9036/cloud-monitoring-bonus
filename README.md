# Monitoreo API Bonus

## Autor
**Nombre:** Jhon Alexander Vargas  
 

## Descripción del proyecto
Este proyecto implementa un sistema básico de **monitoreo y observabilidad en la nube** para una API REST desarrollada en **Python con Flask**, instrumentada con métricas en formato **Prometheus**, visualizada en **Grafana** y ejecutada completamente con **Docker Compose**.

La solución incluye:

- Una API REST con distintos endpoints
- Exposición de métricas en `/metrics`
- Recolección de métricas con Prometheus
- Visualización de datos en Grafana
- Generación de tráfico sintético para observar el comportamiento del sistema

## Objetivo
Demostrar el funcionamiento de un stack de monitoreo completo aplicado a una API, permitiendo observar métricas de tráfico, latencia y comportamiento por endpoint.

## Tecnologías utilizadas
- **Python 3.11**
- **Flask**
- **prometheus-client**
- **Prometheus**
- **Grafana**
- **Docker**
- **Docker Compose**

## Estructura del proyecto
```bash
cloud-monitoring-bonus/
├── docker-compose.yml
├── README.md
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── prometheus/
│   └── prometheus.yml
└── scripts/
    └── generate-traffic.py