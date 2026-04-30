pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "akshaysalamwade/aceest-app:v2"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/2024tm93682-Akshay/ACEest_Fitness_Assignment_II.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/aceest-devops-deployment aceest-container=$DOCKER_IMAGE
                '''
            }
        }
    }
}