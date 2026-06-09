class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        for node in nodes:
            if node not in children:
                return nodes[node]