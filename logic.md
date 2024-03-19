# logic

## POC1 requirements

### backend

- data in sqlite
- data can only be added to sqlite db using SQL commands from backend
- prepare a flask backend route that serves all the data to the frontend in JSON format. basically each json element inside the array is a row of the db. None of the flask routes to be protected by login.

```json
{
    "all-data": [
        {
            "start_time": "",
            "end_time": "",
            "task_description": "",
            "record_type": ""
        }, 
        {
            "start_time": "",
            "end_time": "",
            "task_description": "",
            "record_type": ""
        } 
    ]
}
```
### frontend

- frontend to display the calendar without much UI / UX nonsense
- show the task_description inside the chunk
- show all in one go on same page

### deploy

- to be deployed for personal use
- use standard flask run command. not wsgi or anything else.
- to run on rpi
- to deploy ONLY on tailscale network. NOT on LAN or localhost
- to deploy on rpi, not git stuff config on rpi or anything like that. this is a public repo. just zip the code from here. `scp` there. unzip there. create virtual env there. install dependencies using `pip` and `requirements.txt`. 
- in order for it to run in background after ssh disconnects, use `tmux`.
- if RPi shutdowns for whatsoever reason, the job ceases to run anymore. 

### misc notes

![misc poc 01](./notes-assets/logic001.excalidraw.png)

