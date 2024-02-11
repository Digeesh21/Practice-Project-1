pipeline {
agent {
  label 'LAPTOP-A8CQ62JK'
}
stages {
stage ('checkout') {
  steps {
    checkout scm
  }
}
stage('Python') {
steps{
  powershell """
    python.exe asterisk.py
  """
  }
}
}
}

