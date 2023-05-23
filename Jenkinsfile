pipeline {
  agent any
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Build App'
        sh 'sudo apt intall pip'
        sh 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        echo 'Test Start'
        sh 'pytest -v -s tests'
      }
    }

  }
}