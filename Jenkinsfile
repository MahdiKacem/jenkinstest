pipeline {
	agent { docker { image 'python:3.13.5-alpine3.22' } }
	parameters {
		choice(name: 'SERVICE', choices: ['service1', 'service2'], description: 'Select the service')
	}
	stages {
		stage('build') {
			steps {
				echo "Building ${params.SERVICE}..."
				dir("${params.SERVICE}")
				sh 'python3 test.py'
			}
		}
	}
}
