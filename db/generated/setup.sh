#!/bin/bash

dropdb amazon
createdb amazon
psql -af ../create.sql amazon
psql -af load.sql amazon