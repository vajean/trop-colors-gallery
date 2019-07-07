# trop-colors-gallery

A simple google app engine gallery for interactive canvases, animations.

Each project gets its own `/project_name` url without revealing the site structure.

Just copy your project / animation in
`/templates/projects/[new_project_name]`. See below the structure needed.


### Each project folder ###

* **must** be uniquely called

* **must** have `index.html` in root project folder `/`

* **must** have `thumb.png` and `flavicon.ico` in `/somefolder` or `/` folder

* *image*, *javascript*, *css*  files in `/respective_folders` or `/` folder - though the former is recommended for good housekeeping 



After a folder has been added in the `/templates/project/[your_project]`
it will automatically be added to the main gallery using the project folder
as the name and the thumb image as the thumbnail.

Please open an issue for any problems you might encounter, or features we
could add.

