"""
MIT License

Copyright (c) [2025] [Wendy Darby]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""Main module for customer segmentation analysis.

This module provides functionality for RFM (Recency, Frequency, Monetary) analysis 
and customer segmentation using K-means clustering.
"""

# main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Configuration parameters
CONFIG = {
    'random_state': 42,  # Seed for reproducibility
    'max_clusters': 10,  # Maximum number of clusters to try
    'scaling': 'standard'  # Scaling method ('standard' or 'minmax')
}

def validate_input(value, min_val, max_val, param_name):
    """Validate numeric input parameters.

    Args:
        value (int or float): Value to validate
        min_val (int or float): Minimum allowed value
        max_val (int or float): Maximum allowed value
        param_name (str): Name of parameter for error messages

    Raises:
        TypeError: If value is not numeric
        ValueError: If value is outside allowed range
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"{param_name} must be numeric")
    if value < min_val or value > max_val:
        raise ValueError(f"{param_name} must be between {min_val} and {max_val}")

def check_dataframe(df):
    """Validate DataFrame has required columns for RFM analysis.
    
    Args:
        df (pandas.DataFrame): Input DataFrame to validate

    Raises:
        ValueError: If required columns are missing
        
    Required columns:
        - Recency: Days since last purchase
        - Frequency: Number of purchases
        - Monetary: Total spend amount
    """
    required_cols = ['Recency', 'Frequency', 'Monetary']
    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"DataFrame must contain columns: {required_cols}")

# Add data sanitization
def sanitize_data(df):
    # Remove nulls
    df = df.dropna()
    # Remove negatives 
    df = df[df >= 0]
    return df

# Step 1: Load and prepare data
# For demonstration, create a synthetic dataset
np.random.seed(CONFIG['random_state'])

# Create a sample dataset with 200 customers
# Features: Recency (days since last purchase), Frequency (number of purchases), Monetary (total spend)
n_customers = 200
recency = np.random.randint(1, 100, n_customers)
frequency = np.random.randint(1, 50, n_customers)
monetary = np.random.randint(100, 5000, n_customers)

# Create a DataFrame
df = pd.DataFrame({
    'CustomerID': range(1, n_customers+1),
    'Recency': recency,
    'Frequency': frequency, 
    'Monetary': monetary
})

# Sanitize data
df = sanitize_data(df)

# Step 2: Feature scaling
# Standardize the data to have mean=0 and variance=1
features = ['Recency', 'Frequency', 'Monetary']
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

# Step 3: Determine optimal number of clusters using the Elbow Method
wcss = []  # Within-Cluster Sum of Square
for i in range(1, CONFIG['max_clusters'] + 1):
    kmeans = KMeans(n_clusters=i, init='k-means++',random_state=42)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='-')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.tight_layout()
plt.savefig('elbow_method.png')

# Step 4: Build the K-means model with the optimal number of clusters
# Based on the elbow method, let's choose 4 clusters (this would be determined from the plot)
optimal_clusters = 4

# Wrap core functionality in try-except
try:
    kmeans = KMeans(n_clusters=optimal_clusters)
    df['Cluster'] = kmeans.fit_predict(df_scaled)
except Exception as e:
    logger.error(f"Clustering failed: {str(e)}")
    raise