# 🔐 DevSecOps Pipeline for FastAPI Application

## 📖 Overview

This project demonstrates the implementation of DevSecOps practices throughout the Software Development Life Cycle (SDLC).

The application is built using FastAPI and integrates automated security controls, containerization, CI/CD, vulnerability scanning, and monitoring.

### Key Features

* REST API built with FastAPI
* Docker containerization
* CI/CD pipeline with GitHub Actions
* Static Application Security Testing (SAST)
* Software Composition Analysis (SCA)
* Container vulnerability scanning
* Dynamic Application Security Testing (DAST)
* Monitoring and observability with Prometheus
* Automated security reporting

---

# 🏗 Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions Pipeline
    │
    ├── Unit Tests
    ├── SAST (Bandit)
    ├── SCA (pip-audit)
    ├── Docker Build
    ├── Trivy Scan
    ├── OWASP ZAP Scan
    └── Docker Push
             │
             ▼
         Docker Hub
             │
             ▼
      FastAPI Container
             │
             ├── REST API
             └── Prometheus Metrics
```

---

# 🛠 Technologies

| Category           | Technology     |
| ------------------ | -------------- |
| Language           | Python 3.11    |
| Framework          | FastAPI        |
| Containerization   | Docker         |
| CI/CD              | GitHub Actions |
| Testing            | Pytest         |
| SAST               | Bandit         |
| SCA                | pip-audit      |
| Container Security | Trivy          |
| DAST               | OWASP ZAP      |
| Monitoring         | Prometheus     |
| Version Control    | Git            |

---

# 📂 Project Structure

```text
.
├── app/
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
│
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone https://github.com/yourusername/devsecops-.git

cd devsecops-
```

## Create Virtual Environment

Linux/MacOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Application

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker

## Build Image

```bash
docker build -t devsecops-fastapi .
```

## Run Container

```bash
docker run -d -p 8000:8000 devsecops-fastapi
```

Verify:

```bash
curl http://localhost:8000
```

---

# 🧪 Testing

Run unit tests:

```bash
pytest -v
```

---

# 🔒 Security Controls

## SAST - Bandit

Static code analysis to identify security issues in Python code.

```bash
bandit -r .
```

---

## SCA - pip-audit

Dependency vulnerability analysis.

```bash
pip-audit
```

---

## Container Security - Trivy

Container image vulnerability scanning.

```bash
trivy image devsecops-fastapi
```

---

## DAST - OWASP ZAP

Automated dynamic security testing executed against the running application.

Security checks include:

* Missing security headers
* Sensitive information disclosure
* Common web vulnerabilities
* Configuration weaknesses

---

# 📊 Monitoring

Prometheus metrics endpoint:

```text
http://localhost:8000/metrics
```

Example metrics:

```text
http_requests_total
http_request_duration_seconds
prediction_requests_total
prediction_errors_total
```

---

# 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically performs:

### 1. Build

* Checkout source code
* Install dependencies
* Validate project structure

### 2. Test

* Execute unit tests with Pytest
* Generate code coverage reports
* Upload coverage artifacts
* Validate application quality

### 3. SAST

* Run Bandit securiy scan
* Detect insecure codig patters
* Upload SARIF report to Github Security

### 4. SCA

* Run pip-audit dependency scan
* Detect vulnerable third-party packages
* Upload SARIF report to Github Security

### 5. Container Security

* Build Docker image
* Scan image using Trivy
* Generate HTML report

### 6. DAST

* Deploy container
* Execute OWASP ZAP Baseline Scan
* Generate HTML report

### 7. Release

* Push image to Docker Hub
* Store security artifacts

---

# 📑 Generated Reports

| Tool            | Report Type |
| --------------- | ----------- |
| Pytest Coverage | HTML/XML|
| Bandit          | SARIF       |
| pip-audit       | SARIF       |
| Trivy           | HTML        |
| OWASP ZAP       | HTML        |

Reports are stored as GitHub Actions artifacts and security findings are uploaded to GitHub Security whenever applicable.

---

# 🎯 Quality Gates

The pipeline enforces several automated quality and security controls before a release can be published:

* Successful execution of all unit tests
* Code coverage report generation
* Static code security analysis (SAST)
* Dependency vulnerability assessment (SCA)
* Container image vulnerability scanning
* Dynamic application security testing (DAST)
* Automated artifact generation and reporting

These controls help ensure that only validated, tested, and security-scanned software reahces production environments.

---

# 🎯 DevSecOps Practices Implemented

* Shift Left Security
* Infrastructure as Code Ready
* Continuous Integration
* Continuous Delivery
* Vulnerability Management
* Secure Containerization
* Automated Security Testing
* Monitoring and Observability

---

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-black)
![Trivy](https://img.shields.io/badge/Security-Trivy-red)
![OWASP ZAP](https://img.shields.io/badge/DAST-OWASP_ZAP-orange)

---

# 📈 Future Improvements

* SonarQube Integration
* Kubernetes Deployment
* Helm Charts
* Terraform Infrastructure
* Secrets Management with Vault
* SBOM Generation
* Policy as Code with OPA

---

# 👨‍💻 Author

David Rojas

DevOps | DevSecOps | Cloud Engineer

Technologies:

* AWS
* Docker
* Kubernetes
* Terraform
* GitHub Actions
* Python
* Security Automation
