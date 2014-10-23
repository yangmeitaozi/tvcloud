�   J a v a S c r i p t   D o c u m e n t  
  
 f u n c t i o n   v a l i d a t a N o n E m p t y ( i n p u t F i e l d , h e l p T e x t ) {  
 	 i f ( i n p u t F i e l d . v a l u e . l e n g t h   = =   0 ) {  
 	 	 i f ( h e l p T e x t   ! =   n u l l ) {  
 	 	 	 h e l p T e x t . i n n e r H T M L   = "请坚持输入的值 " ; 	 	  
 	 	 }  
 	 	 r e t u r n   f a l s e ;  
 	 }  
 	 e l s e {  
 	 	 i f ( h e l p T e x t   ! =   n u l l ) {  
 	 	 	 h e l p T e x t . i n n e r H T M L   =   " " ;  
 	 	 }  
 	 }  
 	 r e t u r n   t r u e ;  
 }  
 f u n c t i o n   s e t d i s a b l e d ( i n p u t F i e l d ) {  
 	 i f ( d o c u m e n t . g e t E l e m e n t B y I d ( ' t y p e s ' ) . v a l u e   = =   2 ) { 	 	  
 	 	 d o c u m e n t . g e t E l e m e n t B y I d ( ' u r l ' ) . s e t A t t r i b u t e ( ' d i s a b l e d ' ,   ' d i s a b l e d ' ) ;  
 	 	 d o c u m e n t . g e t E l e m e n t B y I d ( ' c h a n n e l ' ) . r e m o v e A t t r i b u t e ( ' d i s a b l e d ' ) ;  
 	 	  
 	 }  
 	 i f ( d o c u m e n t . g e t E l e m e n t B y I d ( ' t y p e s ' ) . v a l u e   = =   1 ) {  
 	 	 d o c u m e n t . g e t E l e m e n t B y I d ( ' c h a n n e l ' ) . s e t A t t r i b u t e ( ' d i s a b l e d ' , ' d i s a b l e d ' ) ;  
 	 	 d o c u m e n t . g e t E l e m e n t B y I d ( ' u r l ' ) . r e m o v e A t t r i b u t e ( ' d i s a b l e d ' ) ;  
 	 	  
 	 }  
 }  
  
 f u n c t i o n   p l a c e O r d e r ( f o r m )   {  
 	 i f ( v a l i d a t a N o n E m p t y ( f o r m [ ' a l i a s ' ] , f o r m [ ' a l i a s _ h e l p ' ] )    
 	 & &   v a l i d a t a N o n E m p t y ( f o r m [ ' a p p n a m e ' ] , f o r m [ ' a p p n a m e ' ] )    
 	 & &   v a l i d a t a N o n E m p t y ( f o r m [ ' l o g o ' ] , f o r m [ ' l o g o _ h e l p ' ] )    
 	 & &   v a l i d a t a N o n E m p t y ( f o r m [ ' u r l ' ] , f o r m [ ' u r l _ h e l p ' ] ) ) {  
 	 f o r m . s u b m i t ( ) ;  
 	 }  
 	 e l s e {  
 	 a l e r t ( '请检查输入的值'); 
 	 }  
 }