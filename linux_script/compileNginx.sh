#!/bin/bash

./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --with-http_stub_status_module --with-http_ssl_module

make & make install
