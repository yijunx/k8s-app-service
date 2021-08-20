# About the web app #

* to run the webapp, need to 2 environment variables
```
    COLOR=some_color
    DOMAIN_NAME=dev
```

# to start the webapp in docker
```
    docker build -t yijunx/simple_flask:0.0.2 .
    docker run --rm -p xxxx:8000  yijunx/simple_flask:0.0.2
    # visit localhost:xxxx, will show the COLOR and DOMAIN_NAME

    # for docker pull
    docker pull yijunx/simple_flask:0.0.2
```