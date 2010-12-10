<?php 
  if($node->nid==3){
    $expertise_data=array();
    $type="'expertise_cs'";
    $sql = "SELECT * FROM {node} WHERE type = $type";
    $result = db_query($sql); 
    while($row = db_fetch_object($result)){              
      $port_node = node_load(array('nid'=>$row->nid));
      if($port_node->status){
        //print_r($port_node);
        array_push($expertise_data,array(
          'nid'=>$port_node->nid,
          'title'=>$port_node->title,
          'body'=>$port_node->body,
          'filepath'=>$port_node->field_image_file[0]['filepath'],
          'www'=>$port_node->field_www[0]['value'],
          'short_description'=>$port_node->field_short_description[0]['value'],
          'order'=>$port_node->field_order_list[0]['value'],
          'field_fi_scale'=>$port_node->field_fi_scale[0]['value'],
          'field_th_scale'=>$port_node->field_th_scale[0]['value']
        ));
      }
    }
  }
  
  if(strlen($node->body)){
    echo $node->body;
    //echo'<div class="col-left">'.$node->body.'</div>';
  }
  echo'<div class="col-right" style="width:656px;">';
  if($expertise_data){
    /* order */
    $ord=array();
    for($i=0,$ii=count($expertise_data);$i<$ii;$i++){
        $ord[$i]=$expertise_data[$i]['order'];
    }
    array_multisort($ord, SORT_ASC, $expertise_data);
    /* END order */
  
    $i=0;
    echo'<div id="result">';
    foreach($expertise_data as $pd){
        if(!empty($pd['filepath'])){
            $f=base_path() .'/'.$pd['filepath'];   
               
        echo'<div id="p'.$i.'" class="portfolio-box '.(($i%2==0)?'portfolio-box-margin':null).'" style="background:url('.imagecache_create_url($pd['field_fi_scale'], $pd['filepath']).') center center no-repeat;">';
           
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