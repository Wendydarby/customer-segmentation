# Project Documentation

## Overview
This project is designed to analyze customer data using clustering techniques. It utilizes K-means clustering to segment customers based on their purchasing behavior, specifically focusing on recency, frequency, and monetary value.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone [repository-url]
   cd [project-name]
   ```

2. **Install required packages**:
   Ensure you have Python installed, then install the necessary libraries using pip:
   ```
   pip install pandas numpy matplotlib scikit-learn
   ```

3. **Run the main script**:
   Execute the main script to perform the clustering analysis:
   ```
   python src/main.py
   ```

## Usage Guidelines
- The main script will generate an elbow method plot to help determine the optimal number of clusters.
- The results will be saved in the specified output directory.
- Modify the parameters in `src/main.py` as needed to adjust the analysis.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.