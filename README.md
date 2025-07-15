# Shoplytics

**Shoplytics** is a fully containerized, end-to-end data pipeline that simulates an e-commerce analytics platform. It integrates API-based data ingestion, data modeling with dbt, orchestration with Airflow, automated testing, and visualization with Metabase — all managed with Docker Compose.

This project is built to demonstrate real-world data engineering skills and can be used as a portfolio piece or foundation for client work.

---

## Features

- **FastAPI**: Simulates an e-commerce sales API with dynamic order generation using Faker.
- **PostgreSQL**: Central data warehouse for raw and modeled data.
- **dbt**: Cleans, transforms, and aggregates raw data into analytics-ready models.
- **Airflow**: Orchestrates the pipeline with manual and scheduled DAGs.
- **Metabase**: Visualizes sales KPIs via interactive dashboards.
- **Docker Compose**: Runs the entire stack with a single command.
- **GitHub Actions**: CI/CD with API and data layer tests.

---

## Tech Stack

| Layer         | Tool           |
|---------------|----------------|
| API           | FastAPI        |
| Data Storage  | PostgreSQL     |
| Modeling      | dbt            |
| Orchestration | Airflow        |
| Testing       | Pytest, dbt tests |
| CI/CD         | GitHub Actions |
| Dashboarding  | Metabase       |
| Containerization | Docker Compose |

---

## Setup Instructions

### Prerequisites

- Docker & Docker Compose installed
- Python 3.10+ (for local development)

### Clone and Launch

```bash
git clone https://github.com/your-username/shoplytics.git
cd shoplytics
docker-compose up --build
```

Services:
- FastAPI: http://localhost:8000/sales
- Airflow: http://localhost:8080
- Metabase: http://localhost:3000
- Postgres: http://localhost:5432

---

## Pipeline Flow

1. Airflow DAG is scheduled or triggered manually
2. DAG calls FastAPI to generate new fake orders
3. Orders are stored in the `raw_sales` table (Postgres)
4. dbt models clean and aggregate the data
5. Metabase reads from final tables for dashboarding

---

## dbt Models

- `stg_sales`: Cleans and typecasts raw API data
- `sales_by_day`: Aggregates orders by day
- `sales_by_product`: Aggregates orders by product
- `total_revenue`: Shows total revenue without any filter

---

## CI/CD

- GitHub Actions run `pytest` on API endpoints and data loading scripts
- GitHub Actions run `dbt test` on the dbt models to ensure that the models are still functional
- Ensures pipeline remains functional with each commit

---

## Sample Dashboard Metrics

- Daily revenue trends
- Top 5 products by revenue
- Average order value
- Total number of orders

Metabase connects directly to the Postgres models created by dbt.

---

## Roadmap

- [x] FastAPI sales simulation
- [x] PostgreSQL integration
- [x] dbt transformations and tests
- [x] Dockerized deployment
- [x] GitHub Actions with tests
- [x] Metabase dashboards
- [ ] Finalize Airflow DAGs (API call → dbt → Metabase refresh)
- [ ] Optional: Trigger Metabase card refresh via API
- [ ] Deploy to cloud (Render, Railway, etc.)

---

## Author

Built by Mirel Popa, Data Engineer.

This project was developed as a portfolio piece to demonstrate the design and implementation of a full-stack data pipeline using modern tools.
