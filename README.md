# C-Keyword-Extract
# C语言关键词提取计数
---
EE302 Lab2
Extract the Keyword from a C/C++ file， 
## Requirements
Program Requirements
1. Basic requirement: output "keyword" statistics

2. Advanced requirement: output the number of "switch case" structures, and output the number of "case" corresponding to each group

3. Uplifting requirement: output the number of "if else" structures

4. Ultimate requirement: output the number of "if, else if, else" structures

---
## Blog Ref
https://blog.csdn.net/Waiting_fade/article/details/120354565?spm=1001.2014.3001.5501
## Idea
- For this time,  we first care about the annotation and inCode (String, variable name) keyword, we should make judgement under these situation.
- After searching from the Internet, I decide using re module in python to match the basic function
- After Compelting level 1, the level can be easily extended if I design the logic clearly.
- For Worse considerasion,  dealling with the code with not annotation is needed (struct in one line)
- Easy way to think, dealling line by line is not good for complexity
- Level 1 using dynamic array

## Coding standard
**Variable Name:**
- abbreviation for loop iter name, not exactly meaning
- dash(_) for verb combination
**Indentation**
- python standard

## *Version* (Some version not include)
### Beta 0.2
initial version for coding _20min_ 
### Beta 0.3
bug fixed: string and Multiline-string ignore
### Beta 0.4 
bug fixed: _do_ and _double_ will rematch
### Beta 0.5
bug fixed: annotation ignore
### Beta 1.0
function added: level 1 simple realization
### ver 2.0
function added: level 2 simple realization
### ver 2.5
function added：'switch num' output formatted  
### ver 3.0
function added: level 3 logical realization, simple and incorret
### ver 4.0
remake for level 3&4 method(_detail in blog_), match the problem requirement basicaly
Still have bug, keep updating utill ddl and found question



