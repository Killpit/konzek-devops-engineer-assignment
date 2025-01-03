# Base image
FROM python:3.10-slim

# Argument for setting UID
ARG UID=10001

# Create a non-root user
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Set the working directory
WORKDIR /app

# Copy application code
COPY . .

# Create and set up venv
RUN python3 -m venv /venv \
    && . /venv/bin/activate \
    && pip install --upgrade pip 
# Change ownership of the working directory to appuser
RUN chown -R appuser:appuser /app /venv

# Set the PATH to use the venv by default
ENV PATH="/venv/bin:$PATH"

# Use the non-root user
USER appuser

# Expose the application port (if necessary)
EXPOSE 3000

# Define the command to run the application
CMD ["python", "main.py"]
