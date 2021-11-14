# Challenge for AutoLab

## Running with docker

### Pre-requisites:
- docker
- docker-compose

### Steps
1. Create an `.env` file in the root with environment variables
2. Build with `docker-compose build`
2. Run with `docker-compose up`

### How to use
1. In terminal run: 
   - `docker-compose run api flask db upgrade`
   - `Go to http://localhost:5000/apidocs/`
   

### Environment variables
`FLASK_DEBUG=True` 
`FLASK_APP=run.py` 
`FLASK_ENV=development`
`FLASK_RUN_HOST=0.0.0.0`
`SECRET_KEY`=YOUR SECRET KEY 

### RUN TESTS
`docker-compose run api pytest` 