<?php
  if(strlen($node->body)){
    echo $node->body;
    //echo'<div class="col-left">'.$node->body.'</div>';
  }
  
  echo'<div class="col-right" style="width:656px;">';

  
  /* order */
  $ord=array();
  for($i=0,$ii=count($portfolio_data);$i<$ii;$i++){
      $ord[$i]=$portfolio_data[$i]['order'];
  }
  array_multisort($ord, SORT_ASC, $portfolio_data);
  /* END order */
  
  if($portfolio_data){
    $i=0;
    echo'<div id="result">';
    
    foreach($portfolio_data as $pd){
        if(!empty($pd['filepath'])){
            $f=base_path() .'/'.$pd['filepath'];   
            $image_file=imagecache_create_url($pd['field_fi_scale'], $pd['filepath']);

            //$file_size=getimagesize($image_file);
            //$css_top=((180-$file_size[1])/2).'px';
            //$css_left=((305-$file_size[0])/2).'px';
            echo'<div id="p'.$i.'" class="portfolio-box '.(($i%2==0)?'portfolio-box-margin':null).'" style="background:url('.$image_file.') center center no-repeat;">';

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