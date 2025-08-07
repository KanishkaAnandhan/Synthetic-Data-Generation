import sys
import os
import subprocess
from datetime import datetime

def install_packages():
    """Install required packages"""
    packages = ['python-dotenv', 'mostlyai', 'pandas']
    
    for package in packages:
        try:
            __import__(package.replace('-', '_') if package == 'python-dotenv' else package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    """Quick data generation"""
    print("Quick Mostly AI Test Data Generation")
    print("=" * 45)
    
    # Install packages
    install_packages()
    
    # Import after installation
    from dotenv import load_dotenv
    from mostlyai.sdk import MostlyAI
    import pandas as pd
    
    # Load environment
    load_dotenv()
    
    # Get API key
    api_key = os.getenv('MOSTLY_AI_API_KEY')
    if not api_key:
        api_key = "mostly-c146635b4d81e15a7097d3a44de15da8a8edd43c5af1f9746e9849d04887277b"
        if not api_key:
            print("API key required")
            return
        
    # seed_str = os.getenv('SYNTHETIC_DATA_SEED', '1234')
    # try:
    #     seed_value = int(seed_str)
    # except ValueError:
    #     print(f"Invalid SYNTHETIC_DATA_SEED '{seed_str}', falling back to 1234")
    #     seed_value = 1234

    
    print(f"Using API key: {api_key[:10]}...")
    # print(f"Using seed: {seed_value}")
    
    try:
        # Initialize client
        mostly = MostlyAI(api_key=api_key, base_url='https://app.mostly.ai')
        print("Client initialized")
        
        # Quick generation with census data
        print("Training generator...")
        generator = mostly.train(
            data='https://github.com/mostly-ai/public-demo-data/raw/dev/census/census.csv.gz'
        )

        # Download and clean training data
        # print("Downloading census data...")
        # data = pd.read_csv('https://github.com/mostly-ai/public-demo-data/raw/dev/census/census.csv.gz', compression='gzip')

        # print("Cleaning training data...")
        # cleaned_data = clean_training_data(data)

        # print("Training generator on cleaned data...")
        # generator = mostly.train(data=cleaned_data)

         # Obtain deterministic seed value for reproducibility
        # seed_value =int(os.getenv('SYNTHETIC_DATA_SEED', '1234'))
        # seed_value = '{"age": 30, "gender": "male"}'

        
        print(f"Generating 20 records...")
        synthetic_dataset = mostly.generate(generator, size=20)
        
        # Get and save datas
        data = synthetic_dataset.data()
        
        # Create output directory
        os.makedirs('data/output', exist_ok=True)
        
        # Save file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/output/quick_synthetic_data_{timestamp}.csv"
        data.to_csv(filename, index=False)

        # from ydata_profiling import ProfileReport

        # html_report_filename = f"data/output/quick_synthetic_data_report_{timestamp}.html"
        # profile = ProfileReport(data, title="Mostly AI Synthetic Data Profiling Report", explorative=True)
        # profile.to_file(html_report_filename)

        # print(f"HTML profiling report saved to: {html_report_filename}")
        
        print(f"Generated {len(data)} records")
        print(f"Saved to: {filename}")
        print(f"Columns: {list(data.columns)}")
        print(f"\nFirst 3 rows:")
        print(data.head(3))

        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()