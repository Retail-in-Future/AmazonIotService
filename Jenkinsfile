#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage("Run Test") {
            steps {
                sh 'Script/ci/build.sh'
                sh 'Script/ci/test.sh'
            }
        }

        stage("Release") {
            steps {
                sh './release.sh'
            }
        }
    }
}