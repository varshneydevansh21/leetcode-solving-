class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        
        while curr is not None:
            if curr.left is None:
                # Step 2: No left child. Process and move right.
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
                
            else:
                # Step 3: Find the In-order Predecessor
                pred = curr.left
                while pred.right is not None and pred.right != curr:
                    pred = pred.right
                    
                # Step 4: Build the bridge
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                    
                # Step 5: Destroy the bridge, process, and move right
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right