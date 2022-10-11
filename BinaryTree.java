import java.util.LinkedList;  
import java.util.Queue;  
   
public class BinaryTree {  

      public static class Node{  
        int data;  
        Node left;  
        Node right;  
          
        public Node(int data){  
          this.data = data;  
          this.left = null;  
          this.right = null;  
        }  
      }  
      public Node root;  
        
      public BinaryTree(){  
        root = null;  
      }
      public void insertNode(int data) {  
          Node newNode = new Node(data);  
          if(root == null){  
              root = newNode;  
              return;  
          } 
          else {  
             Queue<Node> queue = new LinkedList<Node>();  
             queue.add(root);  
               
             while(true) {  
                 
                 Node node = queue.remove();  
                 if(node.left != null && node.right != null) {  
                     queue.add(node.left);  
                     queue.add(node.right);  
              }  
                
                else {  
                    if(node.left == null) {  
                         node.left = newNode;  
                         queue.add(node.left);  
                     }
                     else {  
                         node.right = newNode;  
                         queue.add(node.right);  
                     }  
                     break;  
                 }  
             }  
          }  
      }
   public void inorder(Node node) {
          if(root == null){  
              System.out.println("Tree is empty");  
              return;  
          }  
          else {   
              if(node.left!= null)  
                  inorder(node.left);  
              System.out.print(node.data + " ");  
              if(node.right!= null)  
                  inorder(node.right);      
              }        
          }  
   
      public static void main(String[] args) {  
        BinaryTree bt = new BinaryTree();
        bt.insertNode(10); 
        System.out.println("Binary tree after first Insertion : "); 
        bt.inorder(bt.root);  
          
        bt.insertNode(15);  
        bt.insertNode(20); 
        System.out.println("\nBinary tree after second Insertion : ");
        bt.inorder(bt.root);  
          
        bt.insertNode(11);  
        bt.insertNode(14);
        System.out.println("\nBinary tree after third Insertion : ");
        bt.inorder(bt.root);  
          
        bt.insertNode(17);  
        bt.insertNode(19); 
        System.out.println("\nBinary tree after fourth Insertion : ");
        bt.inorder(bt.root);
      }  
    }
