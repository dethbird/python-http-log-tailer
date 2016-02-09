
# HTTP Log Tailer

A Python3 based log file tailing service. Opens a specified port and sends the last `n` lines of either the error or access log over the wire on http request.

## Configure

Copy the shadow file to `.env` and edit. Take note to specify where your access and error log files live.

```bash
cp .env.shadow .env
vim .env
```

source the `.env` to set the environment vars
```bash
source .env
```

## Run
activate python environment
```bash
pyvenv env
source env/bin/activate
```

run
```bash
python service.py
```

verify output:
```bash
* server running at localhost:8080
```


## Try it
try tailing last 10 lines of error log via cURL
```bash
curl "localhost:8080?secret=<my_secret?&type=error&num=10"
```
