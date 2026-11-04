
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {

        stage('Source Code Checkout') {
            steps {
                echo 'Fetching source code from GitHub'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing Python dependencies'

                sh '''
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Automated Testing') {
            steps {
                echo 'Running application test cases'

                sh '''
                    venv/bin/python -m unittest -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image'

                sh '''
                    docker build -t devops-flask-app:latest .
                '''
            }
        }

        stage('Deployment') {
            steps {
                echo 'Deploying application using Docker'

                sh '''
                    docker rm -f devops-flask-app || true

                    docker run -d \
                    --name devops-flask-app \
                    -p 5000:5000 \
                    devops-flask-app:latest
                '''
            }
        }

        stage('Deployment Verification') {
            steps {
                echo 'Verifying application deployment'

                sh '''
                    for i in $(seq 1 10); do
                        if curl -fsS http://localhost:5000/health; then
                            exit 0
                        fi
                        sleep 2
                    done

                    echo "Application health check failed"
                    exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
