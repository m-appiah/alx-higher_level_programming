$(document).ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.keyCode === 13) {
        translate();
      }
    });
  });
});
function translate () {
  const lang = $('INPUT#language_code').val();
  $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
    $('DIV#hello').text(data.hello);
  });
}
