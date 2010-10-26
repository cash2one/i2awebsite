


<?php
  if(strlen($node->body)){
    echo $node->body;
    //echo'<div class="col-left">'.$node->body.'</div>';
  }
  
  echo'<div class="col-right" style="width:656px;">';

  
  if($portfolio_data){
    $i=0;
    echo'<div id="result">';
    foreach($portfolio_data as $pd){
        if(!empty($pd['filepath'])){
            $f=base_path() .'/'.$pd['filepath'];   
            
        
      
         
        echo'<div id="p'.$i.'" class="portfolio-box '.(($i%2==0)?'portfolio-box-margin':null).'" style="background:url('.imagecache_create_url('portfolio-scale', $pd['filepath']).') top left no-repeat;">';
           
          echo'<div class="in-portfolio p'.$i.'">';
            echo'<h1>'.$pd['title'].'</h1>';
            echo'<p>'.$pd['short_description'].'</p>';
            echo'<ul class="portfolio-opt">';
              echo'<li class="left-p"><a href="'.$pd['www'].'" title="'.$pd['title'].'">'.$pd['www'].'</a></li>';
              echo'<li class="right-p"><a href="'.base_path().drupal_lookup_path('alias',"node/".$pd['nid']).'" title="'.$pd['title'].'" class="more-link">more</a></li>';
            echo'</ul>';
          echo'</div>';
          
          
        echo'</div>';
        }
       
      $i++;
    }
    echo'<div class="clear"></div>';
    echo'</div>';
  }
  echo'</div>';
  echo'<div class="clear"></div>';
  
?>