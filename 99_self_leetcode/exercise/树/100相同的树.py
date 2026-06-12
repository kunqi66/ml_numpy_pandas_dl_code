ans = True
def isSametree(tree1, tree2 , p, q):
    if p >= len(tree1) or q >= len(tree2):
        return True
    if tree1[p] == None and tree2[q] == None:
        return True
    elif tree1[p] == tree2[q]:
        pass
    else:
        return False
    left = isSametree(tree1, tree2, p << 1, q << 1)
    right = isSametree(tree1, tree2, p << 1 | 1, q << 1 | 1)
    return left and right
if __name__ == "__main__":
    tree1 = [0,1,2,3,None,None,5,6,6,8,8,9,None,6,5,8]
    tree2 = [0,1,2,3,None,None,5,6,6,8,8,9,None,6,5,8]
    print(isSametree(tree1, tree2, 1, 1))

def isSametree_l(p, q):
    if p == None and q == None:
        return True
    elif p.val == q.val:
        pass
    else:
        return False
    left = isSametree( p.left, q.left)
    right = isSametree( p.right, q.right)
    return left and right