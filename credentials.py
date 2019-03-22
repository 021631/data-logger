class Credentials:
    app_path_name = "data_logger"

    activity_path = "/var/www/upload/{}/log.txt".format(app_path_name)  # logging activity
    credentials_path = "/boot/credentials.ini"  # user credentials (client ID und secret)
    config_path = "/var/www/upload/{}/config/config.ini".format(app_path_name)  # config file
    log_path = "/var/www/upload/{}/log/".format(app_path_name)  # logging file for dataset
    ondo_path = "http://api.ondo.one/beemo"  # logging activity api
