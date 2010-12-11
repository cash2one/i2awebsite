<?php
  $main_node = node_load(array('nid'=>'8'));
  $pnode=node_load(array('nid'=>$node->nid)); 
?>

<?php
  echo'<div class="col-right project">';
    //echo'<h1 id="project-name">'.$pnode->title.'</h1>';
    echo'<div>'.$pnode->body.'</div>';
    echo'<div id="project-gallery">';
      if(!empty($pnode->field_screen_image[0])){
        foreach($pnode->field_screen_image as $image){
            echo'<div>';
                $image_file=imagecache_create_url($pnode->field_th_scale_p[0]['value'], $image['filepath']);
                $file_size=getimagesize($image_file);
                //$css='style="padding-top:'.((120-$file_size[1])/2).'px;"';
                echo'<a href="'.imagecache_create_url('portfolio-lightbox', $image['filepath']).'" title="'.$pnode->title.'">
                        <img '.$css.' src="'.$image_file.'" alt="'.$pnode->title.'" class="lightbox" />
                    </a>';
              echo'</div>';
        }
      }
  echo'</div>';
  echo'<div class="clear"></div>';
                 
  if(!empty($pnode->field_www[0]['value']))
    echo'<br /><b>See online:</b> <a href="'.$pnode->field_www[0]['value'].'" title="See onlline: '.$pnode->title.'">'.$pnode->field_www[0]['value'].'</a>';
  echo'<br /><br />';
  echo'<a href="'.base_path().drupal_lookup_path('alias',"node/8").'" title="back" class="back-link"> back</a>';
  echo'</div>';
  
  echo'<div class="clear"></div>';  
?>

<script type="text/javascript">
  $(function(){
    $("#breadcrumbs").html('<b style="color: rgb(0, 138, 173);">Home</b> &raquo; Portfolio &raquo <?php echo $pnode->title; ?></h1>')
  });
</script>