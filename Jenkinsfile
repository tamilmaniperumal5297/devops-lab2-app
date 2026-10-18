pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'tamilmani5297'
        IMAGE_NAME      = 'devops-lab2-app'
        REGISTRY_CRED   = 'docker-hub-credentials'
    }

    stages {
        stage('1. Code Validation') {
            steps {
                echo 'Validating Python application syntax...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('2. Build & Tag Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}..."
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER} -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest ."
            }
        }

        stage('3. Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${REGISTRY_CRED}", usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh "echo \$PASS | docker login -u \$USER --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }

        stage('4. Deploy to Kubernetes') {
            steps {
                echo 'Applying Kubernetes Manifests...'
                sh 'kubectl apply -f configmap.yaml'
                sh 'kubectl apply -f secret.yaml'
                sh 'kubectl apply -f service.yaml'
                sh 'kubectl apply -f deployment.yaml'
            }
        }

        stage('5. Verify Rollout Status') {
            steps {
                echo 'Verifying deployment rollout status...'
                sh 'kubectl rollout status deployment/lab2-deployment --timeout=60s'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
    }
}