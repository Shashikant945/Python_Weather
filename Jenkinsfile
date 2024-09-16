pipeline {
    agent any
    
    stages {
        stage("Clone Code") {
            steps {
                git url: "https://github.com/Shashikant945/Python_Weather.git", branch: "main"
                echo "Aaj toh LinkedIn Post bannta hai boss"
            }
        }
        stage("Build & Test") {
            steps {
                sh "docker build -t weather_app ."
            }
        }
        stage("Push to DockerHub") {
            steps {
                echo "Pushing image to DockerHub"
                withCredentials([usernamePassword(credentialsId: "dockerhub", passwordVariable: "dockerHubPass", usernameVariable: "dockerHubUser")]) {
                    
                    sh "docker tag weather_app ${env.dockerHubUser}/weather_app:latest"
                    
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker push ${env.dockerHubUser}/weather_app:latest"
                }
            }
        }
        stage("Deploy") {
            steps {
                echo "Deploying the container"
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}
