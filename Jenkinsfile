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
						echo "Building ${params.SERVICE}..."
						dir("${params.SERVICE}"){
							sh 'python3 test.py'
						}
					}
				}
			}
		}
	}
}
