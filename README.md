# Benchmark Authoring Tool  

This is an API for extracting test information based on FAIR Metrics described in Benchmark metadata, following [FTR](https://github.com/OSTrails/FAIR_assessment_output_specification) model. The API is built with **FastAPI** and connects to an **SPARQL endpoint** to retrieve relevant data.

---

## Features  

- Extracts FAIR Metrics from benchmark metadata.  
- Queries a FAIR Data Point (FDP) to retrieve associated tests.  
- Provides a **FastAPI** interface with automatic OpenAPI documentation.  
- Ready for **Docker** deployment.  

---

## Installation

### Running with Docker  

Use the pre-built Docker image from Docker Hub:  

```bash
docker run -p 8000:8000 pabloalarconm/benchmark-authoring-tool:0.0.1
```

Alternatively, use **Docker Compose**:  

```yaml
services:
  api:
    image: pabloalarconm/benchmark-authoring-tool:0.0.1 # Check the latest
    ports:
      - "8000:8000"
```

Then start the container:  

```bash
docker-compose up -d
```

---

## API Documentation  

FastAPI automatically generates OpenAPI documentation.  

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)  
- **Raw OpenAPI JSON**: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)  

---

## Endpoints  

### **POST /benchmark/**  

**Description**: Extracts tests related to FAIR Metrics from a given benchmark.  

**Request Body (JSON)**:  

```json
{
  "web_benchmark": "URL_TO_TURTLE_FILE",
  "creator": "CREATOR_NAME"
}
```

**Response (JSON)**:  

```json
{
    "web_benchmark": "https://oeg-upm.github.io/fair_ontologies/doc/benchmark/ALL/ALL.ttl",
    "creator": "https://orcid.org/0000-0003-0454-7145"
}
```

---

## How It Works  

1. The API receives a **benchmark metadata file (Turtle format)** via `/benchmark/`.  
2. It extracts **FAIR Metrics** from the file.  
3. It queries a **SPARQL endpoint** (`https://tools.ostrails.eu/repositories/fdpindex-fdp`) to retrieve the tests associated with each FAIR Metric.  
4. The response is a list of **test URLs**.