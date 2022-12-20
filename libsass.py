import sass

# Compile SCSS to CSS
css = sass.compile(filename='templates/upload_file.scss')

# Write the CSS code to a file
with open('templates/upload_file.css', 'w') as f:
    f.write(css)