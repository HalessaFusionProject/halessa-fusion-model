# Halessa Fusion Model

This repository contains the data, code, and documentation for the research project described in the manuscript **“Halessa: A Harmonic Field Convergence Model for Sustainable Fusion Synthesis.”**

## Repository Structure

The repository is organised into a set of folders to separate code, data and documentation:

- `src/` – Python modules implementing the harmonic fusion model and supporting functions.
- `notebooks/` – Jupyter notebooks with examples showing how to run simulations and visualise results.
- `results/` – Simulation data. The file `simulation_results.csv` contains two columns (cycle and Q) for 2,000 simulation cycles used to validate the model.
- `figures/` – Generated figures such as conceptual diagrams of field convergence and energy output.
- `docs/` – The manuscript, cover letter and other documents prepared for journal submission.
- `papers/` – Additional papers, notes and references related to the project.

## Simulation Data

The `results/simulation_results.csv` file provides a sample dataset generated with the Halessa model. The **cycle** column identifies simulation cycles (0–1999), and the **Q** column contains the energy output parameter. These values were produced using a sinusoidal modulation around a baseline value of 5.0 with added Gaussian noise to simulate natural variability.

To reproduce or extend these simulations, please consult the example notebook in `notebooks/` or use the source code in `src/` (to be provided).

## Figures

The `figures` directory includes visualisations generated from the model. For instance, `conceptual_diagram.png` illustrates a hypothetical field convergence pattern and is provided for conceptual understanding.

## Citation

If you use this repository or its data and code in your research, please cite the accompanying manuscript. A citation file (`CITATION.cff`) is included with all necessary details. Please replace the DOI placeholder with the DOI assigned to the Zenodo record once a release is made.

## Licence

This project is released under the [MIT Licence](LICENSE). You are free to use, modify and distribute the code and data provided here, provided you include appropriate attribution.

## Contact

For questions, collaboration enquiries or to report issues with the model, please contact the authors at **halessa.fusion.project@gmail.com**.