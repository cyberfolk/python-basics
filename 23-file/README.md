## 20. File
- file handle
  - r &rarr; Read: open a file to read, error if not exist
  - a &rarr; Append: open a file to append, crea il file if not exist
  - w &rarr; Write: open a file to write, crea il file if not exist
  - x &rarr; Create: create a file, error if exist

## ex fw pos
**Exercise File Writing Positional**  
An exercise to writing a new-line of text in a file at a given position indicate with line-number It takes as input:
1. The new string to insert (str)
2. The location to insert it (int)

It works by opening 2 files: one in writing and another in reading. Line by line I read and copy the current-line, when I get to the target-line I insert the new-line and then continue copying the other lines.