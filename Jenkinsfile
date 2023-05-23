pipeline {
  agent any
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Build App'
        sh 'pip install -r requirements.txt'
        sh 'export PATH=$PATH:/var/jenkins_home/.local/bin'
      }
    }

    stage('Test') {
      steps {
        echo 'Test Start'
        sh '''export PATH=$PATH:/var/jenkins_home/.local/bin

pytest -v -s tests'''
      }
    }

  }
}