# MAXONE Genetic Algorithm

This repository contains a Python implementation of the **MAXONE problem** using a **Genetic Algorithm (GA)**. The goal is to maximize the number of ones (`1s`) in a binary string of length **10**.

## 📌 Problem Description

The **MAXONE problem** is a classic genetic algorithm example where:
- Each individual is represented as a binary string (chromosome).
- The **fitness function** counts the number of `1s` in the string.
- The algorithm applies **selection, crossover, and mutation** to evolve better solutions.

## 🚀 How It Works

1. **Initialize** a population of random binary strings.
2. **Evaluate fitness**: Count the number of `1s` in each string.
3. **Selection**: Use **roulette wheel selection** to choose parents.
4. **Crossover**: Perform **single-point crossover** on selected parents.
5. **Mutation**: Each bit has a small chance of flipping (`PMUT = 0.1`).
6. **Iteration**: The process repeats for `MAX_GEN` generations or until an all-ones solution is found.

## 🛠️ Implementation Details

- Uses **Genetic Algorithm (GA)** principles:
  - **Selection**: Roulette Wheel Selection.
  - **Crossover**: Single-point crossover (60% probability).
  - **Mutation**: Random bit flip (10% probability).
- Implemented using Python’s `random` module.

## 📄 Code Structure

- `maxone_ga.py` → Python script containing the implementation.
- `README.md` → This file (documentation).

## 🔧 Requirements

This script runs in **Python 3.x** and requires no external libraries.

## 🏃‍♂️ Running the Program

Clone the repository and execute the script:

```bash
git clone https://github.com/your-username/maxone-ga.git
cd maxone-ga
python maxone_ga.py
