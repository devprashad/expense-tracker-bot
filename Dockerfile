# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container (optional, if using HTTP server)
EXPOSE 80

# Define environment variable (Optional: You can pass them via docker run too)
ENV BOT_TOKEN="7721911699:AAE-jJNg20G6i27RWh2bk1M0R2kY9Au7-6M"
ENV GOOGLE_SHEET_ID="1wqFxTWyV2WsvilTr5n0dsYAxUCUrJ9VFnjOoOPu4YpM"
ENV GOOGLE_SHEET_NAME="spend-expense-tracker"


# Run bot.py when the container launches
CMD ["python", "bot.py"]


