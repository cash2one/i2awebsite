

<?php
  if(strlen($node->body)){
    echo'<div class="col-left">'.$node->body.'</div>';
  }
  
  echo'<div class="col-right">';

  
  if($portfolio_data){
    $i=0;
    echo'<div id="result">';
    foreach($portfolio_data as $pd){
      
        echo'<div class="portfolio-box '.(($i%2==0)?'portfolio-box-margin':null).'">';
          echo'<h1>'.$pd['title'].'</h1>';
          echo'<div class="clear"></div>';
          if(!empty($pd['filepath'])){
            $f=base_path() .'/'.$pd['filepath'];
            echo'<img src="'.$f.'" alt="" />';
          }
          else
            echo'<div class="img-box">&nbsp;</div>';
          echo'<ul class="portfolio-opt">';
            echo'<li class="left-p"><a href="" title="'.$pd['title'].'">'.$pd['www'].'</a></li>';
            echo'<li class="right-p"><a href="" title="" class="more-link">more</a></li>';
          echo'</ul>';
        echo'</div>';
        
       
      $i++;
    }
    echo'<div class="clear"></div>';
    echo'</div>';
  }
  echo'</div>';
  echo'<div class="clear"></div>';
  
?>