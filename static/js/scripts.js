$(document).ready(function(){
    $('#new_post').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/ajax/new_ajaxpost/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_title').val('')
      $("#id_image").val('')
      $("#id_live_link").val('')
      $("#id_description").val('')
      $("#id_developer").val()
    }) // End of submit event
  
  }) // End of document ready function