pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/Gayathrijayaprakash2001/mini-Devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t tesseris/mini-devops-app .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push tesseris/mini-devops-app'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }

    }
}