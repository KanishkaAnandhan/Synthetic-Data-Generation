import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}")
    print(f"Command: {command}")
    print("-" * 50)
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=False)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed with exit code {e.returncode}")
        return False

def main():
    """Run complete workflow"""
    print("🚀 Mostly AI CI/CD Complete Workflow")
    print("=" * 60)
    
    # Ensure we're in the right directory
    if not os.path.exists('src'):
        print("❌ Please run this script from the project root directory")
        return False
    
    # Step 1: Create sample data (for testing)
    if not run_command("python generate_sample_data.py", "Creating sample data"):
        return False
    
    # Step 2: Test API connection
    if not run_command("python src/test-api.py", "Testing API connection"):
        print("⚠️  API test failed, but continuing with sample data...")
    
    # Step 3: Validate the sample data
    if not run_command("python src/validate-data.py", "Validating generated data"):
        return False
    
    # Step 4: Deploy to development environment
    if not run_command("python src/deploy-data.py --env=development", "Deploying to development"):
        return False
    
    print("\n🎉 Complete workflow finished successfully!")
    print("\n📋 Generated files:")
    print("   - Sample data: data/output/")
    print("   - Validation report: reports/data-validation-report.html")
    print("   - Deployment report: reports/deployment-report.html")
    print("   - Deployed data: deployments/dev/")
    
    print("\n🔧 Next steps:")
    print("1. Configure your Mostly AI API key in .env file")
    print("2. Run: python src/jenkins-data-generator.py --size 1000 --env development")
    print("3. Set up Jenkins pipeline using the provided Jenkinsfile")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)