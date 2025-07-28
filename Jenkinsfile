pipeline {
    agent any

    environment {
        // Inject Mostly AI API key securely stored in Jenkins Credentials (Secret Text)
        MOSTLY_AI_API_KEY = credentials('MOSTLY_AI_API_KEY')
    }

    stages {
        stage('Setup and Test') {
            steps {
                script {
                    // Use Windows bat commands (adjust paths if using Linux agent, then use sh instead)
                    bat '''
                        cd "C:\\Users\\kanishka.ananthan\\mostlyaidata"
                        venv\\Scripts\\python.exe -m pip install --upgrade pip
                        venv\\Scripts\\python.exe -m pip install -r requirements.txt
                        venv\\Scripts\\python.exe quick-generate.py
                    '''
                }
            }
        }
    }

    post {
        always {
            // Archive generated CSV files as build artifacts (adjust path if needed)
            archiveArtifacts artifacts: 'data/output/*.csv', allowEmptyArchive: true
            
            // Clean workspace after build (optional)
            cleanWs()
        }
    }
}
