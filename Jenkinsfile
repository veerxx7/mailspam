pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\veers\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\veers\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat '"C:\\Users\\veers\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" src\\train_backend.py'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '*.pkl', fingerprint: true
        }
    }
}