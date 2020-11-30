$(document).ready(function(){
    $('#n_form').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/ajax/new_post/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_title').val('')
      $("#id_live_link").val('')
      $("#id_description").val('')
      $("#id_image").val('')
    })

    $('#np_form').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/project/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_design_vote').val('')
      $("#id_ux_vote").val('')
      $("#id_content_vote").val('')
      $("#id_review").val('')
    }) // End of submit event
  
  }) 

  