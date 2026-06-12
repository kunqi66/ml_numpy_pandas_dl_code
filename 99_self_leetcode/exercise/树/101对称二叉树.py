def isSymmetric(tree, k):
    def dfs(tree1, k, g):
        if k >= len(tree1) and g >=len(tree1):
            return True
        elif k >= len(tree1) or g >=len(tree1):
            return False
        else:
            a = dfs(tree1, k<<1, g<<1|1)
            b = dfs(tree1, k<<1|1, g<<1)
            if tree1[k] == tree1[g]:
                return True and a and b
            else:
                return False
    return dfs(tree, k<<1, k<<1|1)

if __name__ == "__main__":
    tree1 = [0,1,2,2,3,4,4,3]
    tree2 = [0,0,1,1,3,3,5,5,None,None,8,8,9,9,6,6]
    print(isSymmetric(tree2, 1))
    
def isSymmetric2(root):
    def dfs(left, right):
        if left == None and right == None:
            return True
        elif left ==None or right ==None:
            return False
        else:
            a = dfs(left.left, right.right)
            b = dfs(left.right, right.left)
            if left.val == right.val:
                return True and a and b
            else:
                return False
    dfs(root.left , root.right)