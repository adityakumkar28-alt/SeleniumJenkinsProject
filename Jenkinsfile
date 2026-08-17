pipeline { 
    agent any 
    stages { 
        stage('Checkout') { 
            steps { 
                git branch: 'main', 
                    url: 'https://github.com/adityakumkar28-alt/SeleniumJenkinsProject.git' 
            } 
        } 
  
        stage('Install Dependencies') { 
            steps { 
                bat '"C:\\Users\\fe\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt' 
            } 
        } 
  
        stage('Run Selenium Tests') { 
            steps { 
                // Changed from --html to --alluredir to collect data for the dashboard
                bat '"C:\\Users\\fe\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v --alluredir=allure-results' 
            } 
        }
    } 
  
    post { 
        always { 
            // Tells Jenkins to compile the data into the animated Allure UI
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        } 
        success { 
            echo 'Selenium tests completed successfully.' 
        } 
        failure { 
            echo 'Selenium tests failed.' 
        } 
    } 
}
