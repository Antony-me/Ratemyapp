// const form = getElementById('#n_form')
// form.addEventListner("submit", submitHandler);

// function submitHandler(e){
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: '/ajax/new_post',
//         data:$('#n_form').serialize(),
//         dataType:'json',
//         success: function(data){
//             if (data.msg === 'success'){
//                 alert('Your Form is submited')
//             }
//         }
//     })
// }
$(document).ready(function(){
    $('form').submit(function(event){
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
    }) // End of submit event
  
  }) // End of document ready function