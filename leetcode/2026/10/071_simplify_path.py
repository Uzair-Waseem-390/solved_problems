# Simplify Path
# Difficulty: Medium
# https://leetcode.com/problems/simplify-path/

# The problem involves processing path components, and a stack is a natural fit
# to handle '..' (parent directory) operations. Split the path, then iterate
# to build the canonical path on the stack.
class Solution:
    def simplifyPath(self, path: str) -> str:
        directory_stack = []
        path_segments = path.split('/')

        for segment in path_segments:
            if segment == "" or segment == ".":
                continue
            elif segment == "..":
                if directory_stack:
                    directory_stack.pop()
            else:
                directory_stack.append(segment)
        
        if not directory_stack:
            return "/"
        else:
            return "/" + "/".join(directory_stack)