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
