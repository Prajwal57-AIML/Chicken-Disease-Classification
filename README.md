# 🚀 End-to-End Chicken Disease Classification System  
**MLOps | Deep Learning | Multi-Cloud CI/CD Deployment**

---

## 📌 Overview  
This project presents a **production-grade end-to-end deep learning system** for detecting chicken diseases from images. It covers the complete lifecycle — from **data ingestion to deployment** — using modern **MLOps practices** and **multi-cloud CI/CD pipelines**.

The solution is designed to simulate a real-world ML system with **scalability, reproducibility, and automation** in mind.

---

## 🎯 Key Highlights  

- ✅ Built a **CNN-based image classifier** for chicken disease detection  
- ✅ Designed a **modular pipeline architecture** (training → evaluation → prediction)  
- ✅ Implemented **MLOps workflows using DVC + GitHub Actions**  
- ✅ Achieved **experiment tracking, versioning, and reproducibility**  
- ✅ Containerized the application using **Docker**  
- ✅ Deployed on **AWS (ECR + EC2)** and **Azure (Container Registry + Web App)**  
- ✅ Configured **CI/CD pipelines for automated build & deployment**  

---

## 🧠 Project Architecture  

The project follows a structured pipeline approach:

1. Data Ingestion  
2. Data Validation  
3. Data Transformation  
4. Model Training (CNN)  
5. Model Evaluation  
6. Prediction Pipeline (Flask App)  

---

## ⚙️ Tech Stack  

| Category | Tools & Technologies |
|----------|---------------------|
| Language | Python 3.10 |
| ML/DL | TensorFlow / Keras |
| MLOps | DVC, GitHub Actions |
| Deployment | Docker |
| Cloud | AWS (ECR, EC2), Azure (ACR, Web Apps) |
| Version Control | Git, GitHub |

---

## 📁 Project Structure  

```
├── config/                # Configuration files
├── src/                   # Core source code (components, pipelines)
├── dvc.yaml               # DVC pipeline configuration
├── params.yaml            # Model parameters
├── app.py                 # Flask application
├── requirements.txt       # Dependencies
```

---

## 🔄 MLOps Workflow  

- **DVC** used for:
  - Data versioning  
  - Pipeline orchestration  
  - Experiment tracking  

- **GitHub Actions** used for:
  - Continuous Integration (CI)  
  - Continuous Deployment (CD)  

---

## 🐳 Dockerization  

- Built a **lightweight Docker image** for the application  
- Ensured **environment consistency across local & cloud systems**  
- Enabled **seamless deployment to AWS & Azure**  

---

## ☁️ AWS Deployment Pipeline  

- Created **IAM roles & policies** for secure access  
- Used **ECR (Elastic Container Registry)** to store Docker images  
- Deployed on **EC2 instances**  
- Configured **self-hosted GitHub runner** for automation  

### Deployment Flow:
1. Build Docker Image  
2. Push to ECR  
3. Pull & Run on EC2  
4. Serve application  

---

## ☁️ Azure Deployment Pipeline  

- Used **Azure Container Registry (ACR)**  
- Deployed via **Azure Web Apps**  

### Deployment Flow:
1. Build Docker Image  
2. Push to ACR  
3. Deploy on Web App Service  

---

## 🚀 How to Run Locally  

```bash
# Clone repository
git clone https://github.com/entbappy/Chicken-Disease-Classification--Project

# Create environment
conda create -n cnncls python=3.8 -y
conda activate cnncls

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Open browser:
```
http://localhost:<port>
```

---

## 🔁 DVC Commands  

```bash
dvc init
dvc repro
dvc dag
```

---

## 📊 Resume Description  

**Automated End-to-End Chicken Disease Detection | MLOps & Multi-Cloud CI/CD**  

- Engineered a **CNN-based image classification system** for detecting poultry diseases with an end-to-end ML pipeline.  
- Designed and implemented **MLOps workflows using DVC and GitHub Actions** for reproducibility, versioning, and automation.  
- Containerized the application using Docker and deployed across **AWS (ECR, EC2)** and **Azure (ACR, Web Apps)**.  
- Built **CI/CD pipelines** for automated model deployment with secure IAM configuration and zero-downtime updates.  

---

## 📌 Future Improvements  

- Add **real-time monitoring & logging**  
- Integrate **model drift detection**  
- Improve model accuracy with advanced architectures (ResNet, EfficientNet)  

---

## 🔗 References  

- Inspired by industry-level MLOps pipelines  
- Deep learning and deployment best practices  
