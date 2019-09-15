#!/bin/bash

function get_chrome_drivers() {
    if [ ! -d "chrome" ]; then
        mkdir chrome
    fi
    cd chrome
    if [ ! -d "linux" ]; then
        mkdir linux
        cd linux
        wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_linux64.zip
        unzip chromedriver_linux64.zip
        rm chromedriver_linux64.zip
        cd ..
    fi

    if [ ! -d "mac" ]; then
        mkdir mac
        cd mac
        wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_mac64.zip
        unzip chromedriver_mac64.zip
        rm chromedriver_mac64.zip
        cd ..
    fi

    if [ ! -d "win" ]; then
        mkidr win
        cd win
        wget https://chromedriver.storage.googleapis.com/76.0.3809.126/chromedriver_win32.zip
        unzip chromedriver_win32.zip
        rm chromedriver_win32.zip
        cd ..
    fi
    cd ..
}

function get_firefox_drivers() {
    if [ ! -d "firefox" ]; then
        mkdir firefox
    fi
    cd firefox
    if [ ! -d "linux" ]; then
        mkdir linux
        cd linux
        wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
        tar xf geckodriver-v0.24.0-linux64.tar.gz
        rm geckodriver-v0.24.0-linux64.tar.gz
        cd ..
    fi

    if [ ! -d "mac" ]; then
        mkdir mac
        cd mac
        wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-macos.tar.gz
        tar xf geckodriver-v0.24.0-macos.tar.gz
        rm geckodriver-v0.24.0-macos.tar.gz
        cd ..
    fi

    if [ ! -d "win" ]; then
        mkdir win
        cd win
        wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win64.zip
        tar xf geckodriver-v0.24.0-win64.zip
        rm geckodriver-v0.24.0-win64.zip
        cd ..
    fi
    cd ..
}

get_chrome_drivers
get_firefox_drivers