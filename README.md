# Photonomist

Photonomist aims at helping photo-lovers (or simply photo-owners :D) with tidying their photos.
Given a path that contains photos, photonomist will extract the dates of your photos, 
create directories and group photos according to their dates.

Photonomist took its name from the words:

- Photo..  --> Photography (art of captruring the light)                (Greek root: (Φως) Φωτογραφία)
- ..nomist --> Taxonomist  (person who groups entities into categories) (Greek root: Ταξινομία ή Ταξινόμηση)

## Motivation
As both a photo-owner and a photo-lover, I found myself struggling with grouping my photos in a 'sustainable' way.

I kept creating different directories, with different name patterns to store my photos in a meaningfull way.
Each time I was sure that after 3 months I would remember when, where and with whom I had captured each bunch of photos.


Except for that, I was always failing with grouping them criteria-wise. 
I know that proffs and semi-proffs tend to group photos according to their rating (1 star.. 5 stars), 
but in my case the time aspect proved to be the most meaningful one.

It was impossible, though, to check the date of each photo and create a directory for each date and
then manually move the photos to the corresponding directory. 
Especially, when I was supposed to "tidy" photos of 2 years time-span!!!!

That's why I decided to build this cool app, which does the dirty work for me!!

## Features

Photonomist just took its first breath. It is in version 1.0.0

What makes it standing out:

- It automatically **extracts** your photos' metadata, **creates and names** directories using the extracted dates and **moves** the photos to the corresponding directory
- It ascertains the **validity** of user's input
- It verifies that the **provided input path contains** *.jpg*, *.jpeg*, *.nef* (*Nikon* raw), *.cr2* (*Canon* raw) photos
- It checks if you have *enough disk space* **ONLY** in case that the **input** and the **export** path point to different disks. I.e. if you move your photos from a cellphone to a hard drive! (Applies only to *Windows*)
- It **creates** and **writes** in the *not_transferred.txt*, all the photos that was not possible to be moved


# Developer Edition

## Project Setup

## Create the project directory
    mkdir photonomist
    cd photonomist

## Clone Repo

    git clone https://github.com/panos23kar/photonomist.git

## Create a virtual environment to isolate our package dependencies locally
    cd photonomist

Create virtual env

    python3 -m venv env

On Windows:

    python -m venv env

## Activate Virtual Environment
    source env/bin/activate

On Windows use

    env\Scripts\activate

## Install Requirements
Make sure that the `requirements.txt` is listed under your current directory

    ls
On Windows use 

    dir

Then

    pip install -r requirements.txt

Verify

    pip freeze

## Install Project In Editable Mode

Make sure that the `setup.py` is listed under your current directory

    ls
On Windows use 

    dir

Install Project

    pip install -e .

## Run Tests

    pytest test

## Build Documentation

    cd doc

    make html

### Verify

In the `doc` dir

-   Open `_build` dir
-   Open `html` dir
-   Open `index.html`

## Build Application (Windows only)

    cd ..

Make sure that the `src` dir is listed

    dir

Build App

    pyinstaller --onefile --noconsole src\GUI\gui.py

### Verify

In the `photonomist` dir

-   Open `dist` dir
-   Double click `gui.exe`
