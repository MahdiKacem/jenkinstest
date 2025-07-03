pipeline {
	agent { docker { image 'python:3.13.5-alpine3.22' } }
	parameters {
		choice(name: 'SERVICE', choices: ['all','service1', 'service2'], description: 'Select the service')
	}
	stages {
		stage('build') {
			steps {
				script {
					def services = []
					if(params.SERVICE == 'all') {
						services = ['service1', 'service2']
					} else {
						services = [params.SERVICE]
					}
					for (service in services) {
						echo "Processing ${service}..."
						dir(service){
							echo "Building ${service}"
						}
					}
				}
			}
		}
		stage("Fetch logs locally"){
			steps{
				script{
					def logPaths = ['service1':'service1/logs/service1.log', 'service2':'service1/logs/service2.log']
					def logFile = logPaths[params.SERVICE]
					echo "fetching logs from ${logFile}"
					sh """
						if [ -f "${logFile}" ]; then 
							tail -n 100 ${logFile}
						else echo "No logs found"
						fi
					"""
				}
			}
		}
	}
}
