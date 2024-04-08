$(document).ready(function() {
    $('#addPara').click(function(event) {
      var paraIn = $('#paraIn').val();
      if (paraIn !== '') {
        event.preventDefault()
        $('#paraList').append('<li>' + taskInput+'</li>');
        $('#paraIn').val('');
      }
    });
  
    // Delete Task button click event
    $(document).on('click', '.deleteTaskBtn', function() {
      $(this).parent().remove();
    });
  });
  