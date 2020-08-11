var proposals = ['百度1', '百度2', '百度3', '百度4','a1','a2','a3','a4','b1','b2','b3','b4'];
$('#search-form').autocomplete({
    hints: proposals,
    width: 300,
    height: 30,
    onSubmit: function(text){
        $('#message').html('Selected: <b>' + text + '</b>');
    }
});





