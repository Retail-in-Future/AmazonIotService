#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage("Run Test") {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}