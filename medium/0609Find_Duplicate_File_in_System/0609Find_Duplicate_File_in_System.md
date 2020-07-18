## Find Duplicate File in System

### Problem Link

https://leetcode.com/problems/find-duplicate-file-in-system/

### Problem Description 

directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

```
Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

```

**Note:**

1. No order is required for the final output.
2. You may assume the directory name, file name and file content only has letters and digits, and the length of file content is in the range of [1,50].
3. The number of files given is in the range of [1,20000].
4. You may assume no files or directories share the same name in the same directory.
5. You may assume each given directory info represents a unique directory. Directory path and file info are separated by a single blank space.
 

**Follow-up beyond contest:**

1. Imagine you are given a real file system, how will you search files? DFS or BFS?
2. If the file content is very large (GB level), how will you modify your solution?
3. If you can only read the file by 1kb each time, how will you modify your solution?
4. What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
5. How to make sure the duplicated files you find are not false positive?


### Code (python)

[Approach 1] (98.5%) 

```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        hash_dict = collections.defaultdict(list)
        
        for path in paths:
            s = path.split(" ")
            curr_path = s[0]
            for j in range(1, len(s)):
                file_name, file_content = s[j].split("(")
                hash_dict[file_content].append(curr_path + "/" + file_name)
            
        result = []
        for val in hash_dict.values():
            if len(val) > 1:
                result.append(val)
                
        return result

# class Solution:
#     def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
#         hash_dict = collections.defaultdict(list)
        
#         for path in paths:
#             curr_path = ""
#             j = 0
#             while j < len(path):
#                 if path[j] == " ":
#                     file_name = ""
#                     j += 1
#                     while path[j] != "(":
#                         file_name += path[j]
#                         j += 1
                    
#                     file_content = ""
#                     j += 1
#                     while path[j] != ")":
#                         file_content += path[j]
#                         j += 1
                    
#                     hash_dict[file_content].append(curr_path + "/" + file_name)
#                 else:
#                     curr_path += path[j]
                    
#                 j += 1
            
#         result = []
#         for val in hash_dict.values():
#             if len(val) > 1:
#                 result.append(val)
                
#         return result
```

```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = collections.defaultdict(list)
        for path in paths:
            temp = path.split()
            dir = temp[0]
            for file in temp[1:]:
                idx = file.index('(')
                content = file[idx + 1:-1]
                duplicates[content].append(dir + '/' + file[:idx])
        res = []
        for val in duplicates.values():
            if len(val) > 1:
                res.append(val)
        return res
```

[Approach 2: A Python solution using re]

```python
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        regex = re.compile(
            r"""
                ([0-9a-zA-Z.]+)     # The filename
                \(
                ([0-9a-zA-Z]+)      # The contents
                \)
            """,
            re.VERBOSE
        )
        table = collections.defaultdict(set)
        for path in paths:
            words = path.split(' ')
            directory, files = words[0], words[1:]
            for file in files:
                match = regex.match(file)
                name, contents = match.group(1, 2)
                table[contents].add(f"{directory}/{name}")
        return [
            list(filepaths)
            for (contents, filepaths) in table.items()
            if len(filepaths) > 1
        ]
```