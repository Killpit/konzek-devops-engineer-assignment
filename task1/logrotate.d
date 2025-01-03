/var/log/http-server.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 644 http-server-user http-server
}

/var/log/http-server-error.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 644 http-server-user http-server
}