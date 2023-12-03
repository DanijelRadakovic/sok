#!/bin/bash

# This script is used to build all necessary python components
# and runt django website.

lay_egs() {
  # The directory path is sent as the first argument
  pip install $1
}

run_server() {
  # The Django website path is sent as the first argument
  cd $1
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
}


# build components
lay_egs ./D3Core
lay_egs ./UcitavanjeKod
run_server django_project
