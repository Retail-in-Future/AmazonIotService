#!/usr/bin/env groovy
node {
    timestamps {
        stage 'Run Test'
        checkout scm
        sh 'Script/ci/build.sh'
        sh 'Script/ci/test.sh'

        stage 'Release'
        sh "EPOCH=1 VERSION=${env.BUILD_NUMBER} make release"
    }
}