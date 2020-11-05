pipeline {
  agent { label 'master' }
  stages {
    stage('Source') { // Get code
      steps {
        // get code from our Git repository
        git 'https://github.com/saikrishna2653/crud_examples.git'
      }
    }   
   stage('Deploy in to Kubernetes pods') {    
    // "jenkins_token" is the id for the sonar token
    withCredentials([
            usernamePassword(credentialsId: 'jenkins_host_user', passwordVariable: 'MYUSER_PASSWORD', usernameVariable: 'MYUSER_USERNAME')
    ]) {
      dir('kubernetes-my-appln') {
        sh '''        
          
          #
          # copy files to server
          #
          chmod +x k8s-deploy.sh
          ./k8s-deploy.sh $MYUSER_USERNAME $MYUSER_PASSWORD                  
          
        '''
      }
    }
  }

   
  }
}