
# AURA Epileptic Seizure Detection

This repository contains everything required to run the AURA Seizure detection ML process on ECGs.

It notably features:
* Pipelines for data cleaning and preparation, model training, prediction and visualisation.
* An Airflow orchestration setup to run the various pipelines locally via a local executor.
* An [AIBricks](https://ai4europe.eu) orchestration setup to run the pipelines in a kubernetes cluster.


## Introduction


### AURA

Aura is a not-for-profit organisation working on epileptic seizure detection.

The AURA workflow basically relies on a RandomForest Machine Learning model to detect epileptic seizures from ECGs data.


## Running with Airflow

TBD


## Running with AIBricks

See [README.md](aibricks/README.md) in `aibricks/`.


## Contributing

We try to keep the repository clean and well maintained. 

Pull Requests shall be accepted only if:

* The feature works and has been tested on a CI system.
* There are tests to run every new or updated code. Tests must be reproducible and automated as much as possible.
* Python code follows the default configuration of `flake8`. One can use `black` to automatically reformat Python files.
* Documentation is present and current. If a new feature is introduced it must be documented, and for a change to an existing feature the current documentation must be updated.

We use Travis for all Python code, and container-based tests are executed on a [Jenkins instance](https://art.castalia.camp/).



