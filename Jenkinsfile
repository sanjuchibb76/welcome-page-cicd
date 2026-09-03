pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                bat 'python test_page.py'
            }
        }
        stage('Done') {
            steps {
                echo 'Welcome page built and tested successfully.'
            }
        }
    }
}
