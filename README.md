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

## Idea
- For this time,  we first care about the annotation and inCode (String, variable name) keyword, we should make judgement under these situation.
- After searching from the Internet, I decide using re module in python to match the basic function
- After Compelting level 1, the level can be easily extended if I design the logic clearly.
- For Worse considerasion,  dealling with the code with not annotation is needed (struct in one line)
- Easy way to think, dealling line by line is not good for complexity

## *Version* (Beta not include)
### Beta 0.2
### Beta 0.3
### Beta 0.6
### Beta 1.0
### 2.0

