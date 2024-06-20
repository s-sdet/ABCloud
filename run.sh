#/bin/bash

supervisord -d /run/ && sleep 20 && python3 -m pytest -vs --headless
