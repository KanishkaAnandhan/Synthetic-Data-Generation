import os
import pandas as pd
from datetime import datetime
import numpy as np

def create_sample_data():
    """Create sample synthetic data for testing"""
    print("🎯 Creating sample synthetic data for testing...")
    
    # Ensure output directory exists
    output_dir = 'data/output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate sample data similar to census data
    np.random.seed(42)  # For reproducible results
    
    sample_size = 1000
    
    # Create sample dataset
    data = {
        'age': np.random.randint(18, 80, sample_size),
        'workclass': np.random.choice(['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov'], sample_size),
        'education': np.random.choice(['Bachelors', 'Some-college', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate'], sample_size),
        'education_num': np.random.randint(1, 16, sample_size),
        'marital_status': np.random.choice(['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed'], sample_size),
        'occupation': np.random.choice(['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty'], sample_size),
        'relationship': np.random.choice(['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'], sample_size),
        'race': np.random.choice(['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'], sample_size),
        'sex': np.random.choice(['Female', 'Male'], sample_size),
        'capital_gain': np.random.randint(0, 100000, sample_size),
        'capital_loss': np.random.randint(0, 5000, sample_size),
        'hours_per_week': np.random.randint(1, 99, sample_size),
        'native_country': np.random.choice(['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany'], sample_size),
        'income': np.random.choice(['<=50K', '>50K'], sample_size)
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Add some realistic correlations
    # Higher education tends to correlate with higher income
    high_education_mask = df['education'].isin(['Bachelors', 'Masters', 'Doctorate', 'Prof-school'])
    df.loc[high_education_mask, 'income'] = np.random.choice(['<=50K', '>50K'], sum(high_education_mask), p=[0.3, 0.7])
    
    # Add some missing values to make it realistic
    missing_indices = np.random.choice(df.index, size=int(0.02 * len(df)), replace=False)
    df.loc[missing_indices, 'workclass'] = np.nan
    
    # Save to file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"synthetic_data_development_1000_{timestamp}.csv"
    output_path = os.path.join(output_dir, filename)
    
    df.to_csv(output_path, index=False)
    
    print(f"✅ Sample data created: {output_path}")
    print(f"📊 Dataset info:")
    print(f"   - Rows: {len(df):,}")
    print(f"   - Columns: {len(df.columns)}")
    print(f"   - Missing values: {df.isnull().sum().sum()}")
    print(f"   - File size: {os.path.getsize(output_path) / 1024:.1f} KB")
    
    return output_path

if __name__ == "__main__":
    create_sample_data()