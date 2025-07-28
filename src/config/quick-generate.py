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
    print("🚀 Quick Mostly AI Test Data Generation")
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
        api_key = input("Enter your Mostly AI API key: ").strip()
        if not api_key:
            print("❌ API key required")
            return
    
    print(f"🔑 Using API key: {api_key[:10]}...")
    
    try:
        # Initialize client
        mostly = MostlyAI(api_key=api_key, base_url='https://app.mostly.ai')
        print("✅ Client initialized")
        
        # Quick generation with census data
        print("🔄 Training generator...")
        generator = mostly.train(
            data='https://github.com/mostly-ai/public-demo-data/raw/dev/census/census.csv.gz'
        )
        
        print("🔄 Generating 1000 records...")
        synthetic_dataset = mostly.generate(generator, size=1000)
        
        # Get and save data
        data = synthetic_dataset.data()
        
        # Create output directory
        os.makedirs('data/output', exist_ok=True)
        
        # Save file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/output/quick_synthetic_data_{timestamp}.csv"
        data.to_csv(filename, index=False)
        
        print(f"✅ Generated {len(data)} records")
        print(f"💾 Saved to: {filename}")
        print(f"📊 Columns: {list(data.columns)}")
        print(f"\nFirst 3 rows:")
        print(data.head(3))
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()