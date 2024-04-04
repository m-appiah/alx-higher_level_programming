$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
