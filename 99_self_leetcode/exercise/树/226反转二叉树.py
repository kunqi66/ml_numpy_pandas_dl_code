def invertTree1(tree, p):
    if p >= len(tree):
        return None
    if p<<1 >= len(tree):
        return tree[p]
    elif p<<1|1 >= len(tree):
        tree.append(tree[p<<1])
        tree[p<<1] = None
    tree[p<<1],tree[p<<1|1] = tree[p<<1|1],tree[p<<1]
    invertTree1(tree,p<<1)
    invertTree1(tree, p<<1|1)
    
    return p
if __name__ == "__main__":
    tree = [0, 2, 3, 4, 5, 6, 7, 8]
    invertTree1(tree, 1)
    print(tree)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree2(root):
    if root == None:
        return None
    else:
        root.left,root.right = root.right,root.left
        invertTree2(root.left)
        invertTree2(root.right)
        return root