# running
* start [gateway](./gateway)
* start [scheduler](./scheduler)

# Debug
## add_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/add_job/",
    "data": "{\"func\":\"project.tasks:ping\",\"trigger\":\"interval\",\"id\":\"project.tasks.ping\",\"seconds\":15}"
}
```
## get_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/get_job/",
    "data": "{\"job_id\": \"project.tasks.ping\"}"
}
```
## get_jobs
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/get_jobs/",
    "data": "{}"
}
```
## pause_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/pause_job/",
    "data": "{\"job_id\": \"project.tasks.ping\"}"
}
```
## resume_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/resume_job/",
    "data": "{\"job_id\": \"project.tasks.ping\"}"
}
```
## modify_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/modify_job/",
    "data": "{\"job_id\": \"project.tasks.ping\", \"next_run_time\": null}"
}
```
## reschedule_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/reschedule_job/",
    "data": "{\"job_id\": \"project.tasks.ping\", \"trigger\": \"interval\", \"seconds\": 5}"
}
```
## remove_job
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/remove_job/",
    "data": "{\"job_id\": \"project.tasks.ping\"}"
}
```
## remove_all_jobs
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/remove_all_jobs/",
    "data": "{}"
}
```
## search_job_logs
```shell script
http://127.0.0.1/api/dispatch/
-
POST
-
{
    "path": "/scheduler/search_job_logs/",
    "data": "{\"conditions\": {\"job_id\": \"project.tasks.ping\"}, \"offset\": 0, \"limit\": 15}"
}
```
