## Binary Tree Paths

### Problem Link

https://leetcode.com/problems/binary-tree-paths/

### Problem Description 

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

```
Example 1:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

```

### Code (python)

[Approach 1: DFS] (87%) 

```c++
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if(!root)
            return {};
        
        vector<string> result {};
        DFS(root, "", result);
        
        return result;
    }
    
    void DFS(TreeNode *node, string path, vector<string>& result){
        
        path += to_string(node->val);
        
        if(!node->left && !node->right){
            result.push_back(path);
        }
        else{
            path += "->";
            if(node->left){
                DFS(node->left, path, result);
            }
            if(node->right){
                DFS(node->right, path, result);
            }
        }
        
    }
};
```

```c++
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> result;
        insertPaths(root, "", &result);
        return result;
    }
private:
	// simple recursive pre-order traversal
    void insertPaths(TreeNode* node, string str, vector<string>* res) {
        if (!node) return;  // base-case
        
        str += to_string(node->val);
        if (!node->left && !node->right) {
			// if the current node is a leaf, add string to result
            res->emplace_back(str);
        }
        
        insertPaths(node->left, str + "->", res);
        insertPaths(node->right, str + "->", res);
    }
};
```

[Approach 2: BFS] (87%) 

```c++
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if(!root)
            return {};
        
        queue<pair<TreeNode *, string>> q;
        vector<string> result;
        
        q.push({root, ""});
        
        while(!q.empty()){
            pair<TreeNode *, string> curr_node = q.front();
            q.pop();
            
            if(!curr_node.first->left && !curr_node.first->right){
                result.push_back(curr_node.second + to_string(curr_node.first->val));
            }
            else{
                if(curr_node.first->left){
                    q.push({curr_node.first->left, curr_node.second + to_string(curr_node.first->val) + "->"});
                }
                if(curr_node.first->right){
                    q.push({curr_node.first->right, curr_node.second + to_string(curr_node.first->val) + "->"});
                }
            }
        }
        
        return result;
    }
};
```

https://leetcode.com/problems/binary-tree-paths/discuss/328432/recursion-cpp-0ms