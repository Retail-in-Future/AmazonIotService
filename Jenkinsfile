#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage("Run Test") {
            steps {
                sh 'sudo Script/ci/build.sh'
                sh 'sudo Script/ci/test.sh'
            }
        }
    }
}