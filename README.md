# Project Overview

This project is designed to analyze customer data using clustering techniques. It utilizes K-means clustering to segment customers based on their purchasing behavior, specifically focusing on recency, frequency, and monetary value.

## Features

- Synthetic dataset generation for customer analysis
- Data preprocessing with feature scaling
- Optimal cluster determination using the Elbow Method
- K-means clustering implementation

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [project-name]
   ```
2. Create and activate virtual environment:
   On Windows:
   ```
  python -m venv venv
   .\venv\Scripts\activate
   ```
   On macOs/Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required libraries:
   ```
   pip install -r requirements.txt
   ```
4. Run setup script:
   On Windows:
   ```
   .\setup_env.sh
   ```
   On MacOS/Linux:
   ```
   chmod +x setup_env.sh
   ./setup_env.sh
   ```
### Usage

To run the main script, execute the following command:
```
python src/main.py
```

This will generate the clustering results and save the Elbow Method plot as `elbow_method.png`. 

## Documentation

For detailed documentation, please refer to the `docs/README.md` file.