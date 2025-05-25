# Project Overview

This project is designed to analyze customer data using clustering techniques. It utilizes K-means clustering to segment customers based on their purchasing behavior, specifically focusing on recency, frequency, and monetary value.

## Features

- Synthetic dataset generation for customer analysis
- Data preprocessing with feature scaling
- Optimal cluster determination using the Elbow Method
- K-means clustering implementation

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - pandas
  - numpy
  - matplotlib
  - scikit-learn

### Installation

1. Clone the repository:
   ```
   git clone [repository-url]
   ```
2. Navigate to the project directory:
   ```
   cd [project-name]
   ```
3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```

### Usage

To run the main script, execute the following command:
```
python src/main.py
```

This will generate the clustering results and save the Elbow Method plot as `elbow_method.png`. 

## Documentation

For detailed documentation, please refer to the `docs/README.md` file.