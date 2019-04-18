### 1.1
* The software for collecting data is now decoupled from the web server
* In the event of a crash, the logger restarts automatically
* Improvement of the log file (it becomes even clearer what went wrong, incl. Timestamp)
* The system tries to generate a valid record three times. If the record is invalid after the third time, the RPi restarts and tries again.

### 1.1.1
* added second api to log error into the database

### 1.1.2
* remove median from scale dataset (default from scale measured 16 times)