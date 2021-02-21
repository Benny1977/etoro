# eToro home exam

## bin
#### A script in Python that fails two out of three times (when BUILD_NUMBER % 3 == 0)


## Jenkinsfile:

- Pull latest from https://github.com/Benny1977/etoro (main)
- Run the script /bin/fail-on-3.py - retry three times before failing
- If runstep was successful (otherwize this job will be skeeped) prints the BUILD_NUMBER


## Server details

| Jenkins-Host | 3.64.89.173 |
| Genkins URL | http://3.64.89.173 |
| jenkins-user | admin |
| jenkins-password | Benj123$ |

