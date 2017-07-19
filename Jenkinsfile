#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage("Run Test") {
            steps {
                sh 'scripts/ci/build.sh'
                sh 'scripts/ci/test.sh'
            }
        }
    }
}