pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('Docker-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Chinnadurai31/streamlit.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                   
                    def imageTag = "chinnadurai123/jenkins:ci_cd-${BUILD_NUMBER}"
                    
                    docker.build(imageTag)
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    
                    def imageTag = "chinnadurai123/jenkins:ci_cd-${BUILD_NUMBER}"
                   
                    docker.withRegistry('https://index.docker.io/v1/', 'Docker-credentials') {
                        docker.image(imageTag).push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image successfully built and pushed to Docker Hub.'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
