pipeline {
  agent any
  stages {
    stage('Build') {
      agent any
      steps {
        echo 'Build App'
        sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
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