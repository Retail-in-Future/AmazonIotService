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
                sh 'EPOCH=1 VERSION=${env.BUILD_NUMBER} make release'
            }
        }
    }
}