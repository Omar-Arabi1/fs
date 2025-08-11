# fs
a fuzzy search for files and diretories

## searching
to start the fuzzy search use the `fs` command it takes two arguments a directory to search in it's contents
and a pattern to search with, example

    fs . gi

> [!NOTE]
> *the '.' in the first argument is the directory it stands for current working directory, use it to search within the directory you are*
> *already in*

in this example it loops through all the contents of the given directory '.' (current working directory) and searches
for entries that start with the given pattern 'gi' if it finds any file or directory with this pattern in their name
it will be printed to the console

> ![NOTE]
> *by default the application doesn't search through hidden entries as well, if you want it to search through hidden entries*
> *use the [hidden](#hidden-option) option*