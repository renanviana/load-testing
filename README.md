# Load Testing with locust

Sample project for creation load testing using [locust framework](https://locust.io/)

## Prerequisites

- Docker
    - [Linux](https://docs.docker.com/desktop/install/linux-install/)
    - [MacOS](https://docs.docker.com/desktop/install/mac-install/)
    - [Windows](https://docs.docker.com/desktop/install/windows-install/)

## Usage

Run this command to create containers

```bash
docker compose up
```

Ready! 

Note you can now access the API via browser:

```
http://localhost:8000
```

Access the locust interface to execute load testing:

```
http://localhost:8089
```

Include the number of users to test, and spawn rate to each user, start test.

After tests, you can remove all containers: (**WARNING**: This command will remove all containers in your docker!)

```shell
docker rm $(docker ps -aq)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

* *Renan Viana* - [renanviana](https://github.com/renanviana)
