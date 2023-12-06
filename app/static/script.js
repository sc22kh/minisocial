$(document).ready(function() {
   var like_button = $('.like-button');
   like_button.click(
      function() {
         var current_like_button = $(this);
         $.ajax({
            url: '/like-post/' + $(this).data('post-id'), //Add post-id to URL so view knows it
            type: 'POST',
            data: JSON.stringify({ response: $(this).attr('id') }),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(response) {
               current_like_button.text("Like "+response.likes); //Change the text in like button
            },
            error: function(error) {
               console.log(error);
            }
         });
      });
});




