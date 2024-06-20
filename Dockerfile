FROM artifactory.***/docker/testrail/autotests-web/testrail-autotests-web:latest

COPY . .

ENTRYPOINT ["/bin/bash", "run.sh"]
