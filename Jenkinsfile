pipeline { 
    agent any 
    stages { 
        stage('Checkout') { 
            steps { 
                // We will update this URL in the next step!
                git branch: 'main', 
                    url: 'https://github.com/adityakumkar28-alt/SeleniumJenkinsProject.git' 
            } 
        } 
  
        stage('Install Dependencies') { 
            steps { 
                bat 'python -m pip install -r requirements.txt' 
            } 
        } 
  
        stage('Run Selenium Tests') { 
            steps { 
                bat 'python -m pytest -v --html=report.html --self-contained-html' 
            } 
        } 
    } 
  
    post { 
        always { 
            archiveArtifacts artifacts: 'report.html', 
                             allowEmptyArchive: true 
        } 
        success { 
            echo 'Selenium tests completed successfully.' 
        } 
        failure { 
            echo 'Selenium tests failed.' 
        } 
    } 
}
