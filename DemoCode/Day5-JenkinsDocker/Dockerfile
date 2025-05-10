FROM python:3.11-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --upgrade pip

# Copy code
WORKDIR /app
COPY . /app

# Install Python packages
RUN pip install -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install --with-deps

# Ensure the test script is executable
RUN chmod +x /app/run_tests.sh

# Set entrypoint
CMD ["bash", "run_tests.sh"]