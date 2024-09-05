# Chest Cancer Classification

This project implements a deep learning model for classifying chest cancer using TensorFlow and MLflow.

## Project Structure

The project follows a modular structure with the following main components:

- `src/ccc`: Main package containing all the project code
- `config`: Configuration files
- `artifacts`: Directory for storing model artifacts
- `research`: Jupyter notebooks for experimentation
- `templates`: HTML templates for the web interface

## Workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mxiid/ChestCancerClassification.git
   cd ChestCancerClassification
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. To run the entire pipeline:
   ```bash
   python main.py
   ```

2. To run the web application:
   ```bash
   python app.py
   ```

3. To retrain the model:
   ```bash
   dvc repro
   ```

## Model Training

The model is based on the VGG16 architecture and is trained on chest X-ray images. The training process includes data augmentation and fine-tuning of the base model.

## Model Evaluation

The trained model is evaluated using MLflow for experiment tracking. Metrics such as accuracy and loss are logged for each run.

## Web Interface

The project includes a Flask-based web interface for making predictions on new images. The interface can be accessed by running the `app.py` file.

## Docker Support

A Dockerfile is provided for containerizing the application. To build and run the Docker image:

```
docker build -t chest-cancer-classification .
docker run -p 8080:8080 chest-cancer-classification

```

## CI/CD

The project uses GitHub Actions for continuous integration and deployment. The workflow is defined in `.github/workflows/main.yaml`.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

