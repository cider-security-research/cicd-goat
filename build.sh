TAG=1.4

if [$1 -eq "build"]
then 
    cd jenkins_server
    docker build --build-arg TAG=$TAG -t cidersecurity/workshop_js:$TAG .
    docker push cidersecurity/workshop_js:$TAG
    cd .. && cd jenkins_agent
    docker build --build-arg TAG=$TAG -t cidersecurity/workshop_ja:$TAG .
    docker push cidersecurity/workshop_ja:$TAG
elif [$1 -eq "publish"]
then
    docker tag cidersecurity/workshop_js:$TAG cidersecurity/workshop_js:latest
    docker push cidersecurity/workshop_js:latest
    docker tag cidersecurity/workshop_ja:$TAG cidersecurity/workshop_ja:latest
    docker push cidersecurity/workshop_ja:latest
fi