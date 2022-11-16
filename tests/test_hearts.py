from conftest import JenkinsClient
from subprocess import run

CMD = 'docker logs prod'


def test_hearts():
    jenkins_client = JenkinsClient('http://localhost:8080', username='knave', password='rockme', useCrumb=True)
    config = {
        "name": 'test',
        "type": "hudson.slaves.DumbSlave",
        'json': {
            "name": 'test',
            "nodeDescription": "",
            "numExecutors": "1",
            "remoteFS": "/home/agent",
            "labelString": "",
            "mode": "NORMAL",
            "type": "hudson.slaves.DumbSlave",
            'nodeProperties' : {
                'stapler-class-bag': 'true'
            },
            "launcher": {
                "stapler-class": "hudson.plugins.sshslaves.SSHLauncher",
                "$class": "hudson.plugins.sshslaves.SSHLauncher",
                "host": 'prod',
                'port': 22,
                'user': 'agent',
                'credentialsId': 'ssh-creds-flag8',
                'sshHostKeyVerificationStrategy': {
                    "stapler-class": "hudson.plugins.sshslaves.verifiers.NonVerifyingKeyVerificationStrategy",
                    "$class": "hudson.plugins.sshslaves.verifiers.NonVerifyingKeyVerificationStrategy"
                }
            }
        }
    }
    jenkins_client.create_node_with_config('test', config)
    result = run(CMD, capture_output=True, text=True, shell=True)
    assert 'Accepted password for agent' in result.stdout or 'Accepted password for agent' in result.stderr
