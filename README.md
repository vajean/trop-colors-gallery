# trop-colors-gallery

A simple google app engine gallery for interactive canvases, animations.

Each project gets its own `/project_name` url without revealing the projects structure.

Just copy your project / animation in
`/templates/projects/[new_project_name]`. See below the structure needed.


### Each project folder ###

* **must** be uniquely called

* **must** have `index.html` in root project folder `/`

* **must** have `thumb.png` in `/img` folder

* all *image* files in `/img` folder

* all *javascript* files in `/js`folder

* all *css* files in `/css` folder

* *other* resources in `/other` folder


After a folder has been added in the `/templates/project/[your_project]`
it will automatically be added to the main gallery using the project folder
as the name and the thumb image as the thumbnail.

Please open an issue for any problems you might encounter, or features we
could add.

