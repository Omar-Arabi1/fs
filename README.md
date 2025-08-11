# fs
a fuzzy search for files and diretories

## searching:
to start the fuzzy search use the `fs` command it takes two arguments a directory to search in it's contents
and a pattern to search with, example

    fs . gi

> [!NOTE]
> *the '.' in the first argument is the directory it stands for current working directory, use it to search within the directory you are*
> *running the tool from*

in this example it loops through all the contents of the given directory '.' (current working directory) and searches
for entries that start with the given pattern 'gi' if it finds any file or directory with this pattern in their name
it will be printed to the console

> [!NOTE]
> *by default the application doesn't search through hidden entries as well, if you want it to search through hidden entries*
> *use the [hidden](#hidden-flag) option*

## hidden flag:
the hidden flag allows you to see through hidden entries as well as non-hidden entries, example

    fs . gi --hidden/-H

in this example it will search through all the files in the given directory and any file that has 'gi' in its
name will be printed to the console, but because we included the `--hidden` flag it will also print hidden
entries that have 'gi' in their name
