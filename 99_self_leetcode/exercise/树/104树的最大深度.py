def maxDepth(tree, root):
    if root > len(tree):
        return 0
    if tree[root] == None:
        return 0
    letf = maxDepth(tree,root<<1) + 1
    right =maxDepth(tree,root<<1 | 1) + 1
    return max(letf, right)
tree = [0,1,2,3,None,None,5,6,6,8,8,9,None,None,5,8]
print(maxDepth(tree, 1))


def maxDepth(root):
    if root.next == None:
        return 0
    left = maxDepth(root.left) + 1
    right = maxDepth(root.right) + 1
    return max(left,right)