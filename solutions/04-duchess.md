Secrets are often pushed to the SCM unintentionally. This makes them accessible to any user with Read permission on the repository.

A common mistake when trying to mitigate the issue is to remove the secret from the branch where the secret was committed to, while the secret is left exposed in past commits - which are still accessible to anyone with access to the repository.

Finding secrets manually in past commits might be tedious, however there are plenty of secret scanners that can be used to automate the process.



1. Clone the repository.

    ```bash
    git clone http://localhost:3000/Wonderland/duchess.git
    ```


2. Download [Gitleaks](https://github.com/zricethezav/gitleaks), or any other repository secret scanner.
3. Run Gitleaks against the repository:

    ```bash
    gitleaks detect -v
    ```


4. Grab the pypi token.

    ```json
    {
    	"Description": "PyPI upload token",
    	"StartLine": 8,
    	"EndLine": 8,
    	"StartColumn": 13,
    	"EndColumn": 184,
    	"Match": "pypi-AgEIcHlwaS5vcmcCJGNmNTI5MjkyLWYxYWMtNDEwYS04OTBjLWE4YzNjNGY1ZTBiZAACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYg7T5yHIewxGoh-3st7anbMSCoGhb-U3HnzHAFLHBLNBY",
    	"Secret": "pypi-AgEIcHlwaS5vcmcCJGNmNTI5MjkyLWYxYWMtNDEwYS04OTBjLWE4YzNjNGY1ZTBiZAACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYg7T5yHIewxGoh-3st7anbMSCoGhb-U3HnzHAFLHBLNBY",
    	"File": ".pypirc",
    	"Commit": "43f216c2268a94ff03e5400cd4ca7a11243821b0",
    	"Entropy": 5.538379,
    	"Author": "Asaf",
    	"Email": "asaf@cidersecurity.io",
    	"Date": "2021-11-16T09:22:31Z",
    	"Message": ".",
    	"Tags": [],
    	"RuleID": "pypi-upload-token"
    }
    ```