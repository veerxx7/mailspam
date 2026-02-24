pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mailspam-api .'
            }
        }

        stage('Run Container Test') {
            steps {
                bat 'docker run -d -p 8000:8000 --name mailspam-test mailspam-api'
            }
        }

        stage('Stop Test Container') {
            steps {
                bat 'docker stop mailspam-test'
                bat 'docker rm mailspam-test'
            }
        }
    }
}