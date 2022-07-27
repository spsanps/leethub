/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */



struct llist {
    struct TreeNode* val;
    struct llist *left;
};

void append(struct TreeNode* elem, struct llist** end) {
    struct llist* new_elem = (struct llist*)(malloc(sizeof(struct llist)));
    new_elem->val = elem;
    new_elem->left = *end;
    *end = new_elem;
}

struct tn* pop(struct llist** end) {
    struct TreeNode* temp = (*end)->val;
    *end = (*end)->left;
    return temp;
}



void flatten(struct TreeNode* root){
    
    if (root == NULL) return;
    
    struct llist stack_end;
    struct llist* stack_end_p = &stack_end;
    struct llist** stack_end_pp = &stack_end_p;
    
    stack_end_p->left = NULL;
    stack_end_p->val = root->right;
    
    //append(root->right, &stack_end_p);
    append(root->left, &stack_end_p);
    
        
    struct TreeNode* prev = root;
    struct TreeNode* c;
    while (stack_end_p != NULL) {
        c = pop(&stack_end_p);
        if (c == NULL) continue;
        
        append(c->right, &stack_end_p);
        append(c->left, &stack_end_p);
      
        prev->right = c;
        prev->left = NULL;
        prev = c; 
    }
    
    
    //return root;  
    

}