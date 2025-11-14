# Water Pump Monitor

A demonstration project showing how to build a monitoring workflow
for a water pumping station using Python.

This project illustrates a structured, mindset-first approach to engineering
software, and includes:

- A FastAPI backend for ingesting sensor readings and serving data
- Simple alert logic based on pressure, flow and pump status
- An in-memory store for recent readings and alerts
- A sensor simulator that generates fake readings without hardware
- A Streamlit dashboard to view latest readings and alerts

## Project structure

- `app/`  
  FastAPI application, models, alert logic and storage.

- `simulator/`  
  Script to generate simulated sensor readings and send them to the API.

- `dashboard/`  
  Streamlit dashboard for visualising readings and recent alerts.

## Installation and usage

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
