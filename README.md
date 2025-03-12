# 🔧 Predictive Maintenance System

A **machine learning-based web application** that predicts potential equipment failures based on input sensor data.  
The system utilizes **Random Forest, ANN, and LSTM models** to provide failure predictions.  

🚀 **Live Demo**: [Hugging Face Space](https://huggingface.co/spaces/ZainFaisal/Predictive-Maintenance-System)  


## 📌 **Project Overview**
Predictive maintenance helps prevent unexpected machine failures by analyzing real-time sensor data.  
This project takes **5 key features** from industrial equipment and predicts whether failure is likely to occur.  

The models included are:  
✔ **Random Forest Classifier**  
✔ **Artificial Neural Network (ANN)**  
✔ **Long Short-Term Memory (LSTM) Network**  

Each model takes preprocessed input data and predicts **Failure (1) or No Failure (0)**.


## 📌 **Features**
✅ User-friendly **Flask-based Web App**  
✅ **Multiple Models for Predictions** (Random Forest, ANN, LSTM)  
✅ **Interactive UI** with a responsive form  
✅ **Live Deployment on Hugging Face Spaces**  


## 📌 **Tech Stack Used**
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask  
- **Machine Learning:** Scikit-Learn, TensorFlow/Keras  
- **Deployment:** Docker, Hugging Face Spaces  


## 📌 **Installation & Running Locally**
### 🛠 **1. Clone the Repository**
```sh
git clone https://github.com/ZainFaisal005/Predictive-Maintenance-System.git
cd Predictive-Maintenance-System
```

### 🛠 **2. Create a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 🛠 **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### 🛠 **4. Run the Flask App**
```sh
python app.py
```
The app will run on **http://127.0.0.1:5000/**.


## 📌 **How to Use the Web App**
1️⃣ **Enter the following sensor values**:
   - Air Temperature [K]  
   - Process Temperature [K]  
   - Rotational Speed [rpm]  
   - Torque [Nm]  
   - Tool Wear [min]  

2️⃣ **Click "Predict"**  
3️⃣ The app will show **predictions from all three models**:
   - ✅ **Random Forest Prediction**
   - ✅ **ANN Prediction**
   - ✅ **LSTM Prediction**  
4️⃣ If failure is likely, the result will display: **"Failure Detected (1)"**  
   Otherwise: **"No Failure (0)"**  


## 📌 **Deploying on Hugging Face Spaces**
This project is deployed on **Hugging Face Spaces** using **Docker**.  
Follow these steps if you want to redeploy:

### 🔹 **1. Create a New Hugging Face Space**
- Go to [Hugging Face Spaces](https://huggingface.co/spaces)
- Create a **new Space**
- Select **Docker** as the environment  

### 🔹 **2. Push Your Code**
```sh
git add .
git commit -m "Deploying on Hugging Face"
git push origin main
```

### 🔹 **3. Configure the `Dockerfile`**
Make sure the `Dockerfile` is set up like this:

```dockerfile
# Use a lightweight Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7860 for Hugging Face
EXPOSE 7860

# Run the app
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
```

### 🔹 **4. Wait for the Build to Complete**
Once the build is done, your app will be live at:  
🔗 **[Hugging Face Space](https://huggingface.co/spaces/ZainFaisal/Predictive-Maintenance-System)**  


## 📌 **Future Improvements**
🔹 **Improve UI Design** (Make it more interactive & modern)  
🔹 **Add Real-Time Streaming Data Support**  
🔹 **Deploy on Other Platforms** (AWS, GCP, Heroku)  
🔹 **Enhance Model Accuracy** (Try other ML models like XGBoost)  


## 📌 **Contributing**
Want to improve this project?  
✅ Fork the repo  
✅ Create a feature branch  
✅ Submit a Pull Request  


## 📌 **Contact**
💡 **Developer:** [Zain Faisal](https://www.linkedin.com/in/zain-faisal-593b05239)  
📩 **Email:** zainfaisal280@gmail.com

🔗 **GitHub:** [ZainFaisal005](https://github.com/ZainFaisal005)  
🔗 **Kaggle:** [ZainFaisal005](https://www.kaggle.com/zain280)  


⭐ **If you find this project helpful, please give it a star!** ⭐
