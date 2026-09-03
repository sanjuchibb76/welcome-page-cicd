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
                bat 'sh test_page.sh'
            }
        }
        stage('Done') {
            steps {
                echo 'Welcome page built and tested successfully.'
            }
        }
    }
}
