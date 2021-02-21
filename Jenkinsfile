pipeline{
    agent any
    stages{
        stage("Get Script From GitHub"){
            steps{
                echo "Pulling Latest from git"
                git branch: 'main',
                credentialsId: 'jenkinsSrv',
                url: 'git@github.com:Benny1977/etoro.git'

                sh "tree"
            }
        }

        stage("Run script"){
            options{
		  retry(3)
		}
            steps{
                echo "running the script"
                sh "python bin/fail-on-3.py"
            }            
        }
    }
}
