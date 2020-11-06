
def HOST_NAME= '3.237.40.210'

def USER_ID= 'dockeradmin'

pipeline {
  agent { label 'master' }
  stages {
    stage('Source') { // Get code
      steps {
        // get code from our Git repository
       // git 'https://github.com/saikrishna2653/crud_examples.git'
	checkout scm      
      }
    }   
   stage('Deploy in to Kubernetes pods') { 
	 steps {   
      dir('kubernetes-my-appln') {
        sh '''        
          
          #
          # copy files to server
          #
          chmod +x k8s-deploy.sh
	  sed -i -e 's/\r$//' k8s-deploy.sh
          ./k8s-deploy.sh HOST_NAME USER_ID 
        '''		
      }
    }
  }

   
  }
}
