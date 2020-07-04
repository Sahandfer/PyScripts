function create_project() {
    cd
    source env.
    python create_project.py $1
    cd $FILEPATH\\$1
    git init
    touch README.md
    git add README.md
    git commit -m "Project initialized"
    git remote add origin git@github.com:Sahandfer/$1.git
    git push -u origin master
    code .
}