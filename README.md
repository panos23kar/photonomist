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

Photonomist just took its first breath. It is in version 0.1.0.

What makes it standing out:

- It automatically **extracts** your photos' metadata, **creates and names** directories using the extracted dates and **moves** the photos to the corresponding directory
- It ascertains the **validity** of user's input
- It verifies that the **provided input path contains** *.jpg*, *.jpeg*, *.nef* (*Nikon* raw), *.cr2* (*Canon* raw) photos
- It checks if you have *enough disk space* **ONLY** in case that the **input** and the **export** path point to different disks. I.e. if you move your photos from a cellphone to a hard drive! (Applies only to *Windows*)
- It **creates** and **writes** in the *not_transferred.txt*, all the photos that was not possible to be moved