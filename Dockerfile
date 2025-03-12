# Use a lightweight Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 7860 for Hugging Face Spaces
EXPOSE 7860

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]
