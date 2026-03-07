pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Gayathrijayaprakash2001/mini-Devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t tesseris/mini-devops-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push tesseris/mini-devops-app'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }

    }
}