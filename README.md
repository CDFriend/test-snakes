# Battlesnake 2019 Test Snakes  
[![Build Status](https://www.travis-ci.org/CDFriend/test-snakes.svg?branch=master)](https://www.travis-ci.org/CDFriend/test-snakes)

A couple of very dumb snakes to test against, written in Python and built to comply with the Battlesnake 2019 API. Both
snakes can be hosted on Apache web server using the included Dockerfile.

This was mostly an experiment to get some more experience with Apache and Docker. I also discovered that you can serve
multiple WSGI applications on the same server - yay for saving money on infrastructure!

## Building and Running

Build the image from the Dockerfile:  
`$ docker build -t apache_testsnakes .`

Run the server:  
`$ docker run --rm -it -p8080:80 apache_testsnakes`

Check that the snakes are working:  
```
$ curl -XPOST http://localhost:8080/snakes/food_finder/start
{"color": "#FF0000"}
```
